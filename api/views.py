# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from .filters import TaskFilter, BackLogFilter
from .models import Task, BackLog, Status
from .serializer import TaskSerializer, BackLogSerializer, TaskPartialUpdateSerializer
from .permissions import IsAuthenticatedCustom
from rest_framework.permissions import IsAdminUser


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedCustom]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter


class BacklogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedCustom]
    filterset_class = BackLogFilter
    queryset = BackLog.objects.all()
    serializer_class = BackLogSerializer


class TaskCreateView(APIView):
    permission_classes = [IsAuthenticatedCustom]
    def post(self, request, *args, **kwargs):
        task_serializer = TaskSerializer(data=request.data)

        if task_serializer.is_valid():
            task = task_serializer.save()
            backlog_data = create_backlog(task.id)
            return Response(
                data={
                    'task': task_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                task_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class TaskPartialUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedCustom]
    queryset = Task.objects.all()
    serializer_class = TaskPartialUpdateSerializer

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            backlog_data = create_backlog(instance.id)
            return Response({
                'task': serializer.data,
                'backlog': backlog_data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedCustom, IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        try:
            task = Task.objects.get(id=self.kwargs['pk'])
            return task
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task_id = task.id
        if Task is not None:
            remove_task_and_adjust_backlog(task.id)
            task.delete()
            return Response({"message": f"Task nr {task_id} deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No such task"}, status=status.HTTP_404_NOT_FOUND)


def create_backlog(task_id):
    task = Task.objects.get(id=task_id)
    backlog = BackLog.set_backlog_data(task)
    backlog_serializer = BackLogSerializer(backlog)
    return backlog_serializer.data


def remove_task_and_adjust_backlog(task_id):
    task = Task.objects.get(id=task_id)
    task.status = Status.DELETED
    backlog = BackLog.set_backlog_data(task)
    backlog_serializer = BackLogSerializer(backlog)
    return backlog_serializer.data