import django_filters
from django_filters import filters
from .models import Task, BackLog


class TaskFilter(django_filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    description = filters.CharFilter(field_name='description', lookup_expr='contains')

    class Meta:
        model = Task
        fields = {
            'id': ['exact'],
            'status': ['exact'],
            'assignedUser': ['exact'],
        }


class JSONCharFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value in (None, ''): #jesli wartosc jest none albo pustym stringiem zwracamy niemodyfikowany queryset
            return qs
        lookup = f'{self.field_name}__icontains'
        return qs.filter(**{lookup: value})


class JSONExactFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value in (None, ''):
            return qs
        lookup = f'{self.field_name}__exact'
        return qs.filter(**{lookup: value})


class BackLogFilter(django_filters.FilterSet):
    name = JSONCharFilter(field_name='task_data__name')
    description = JSONCharFilter(field_name='task_data__description')
    status = JSONExactFilter(field_name='task_data__status')
    assignedUser = JSONExactFilter(field_name='task_data__assignedUser')
    task_id = JSONCharFilter(field_name='task_data__task_id')

    class Meta:
        model = BackLog
        fields = ['id', 'modification_date']
