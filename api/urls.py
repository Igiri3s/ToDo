from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskCreateView, TaskViewSet, BacklogViewSet, TaskPartialUpdateView, TaskDeleteView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'backlogs', BacklogViewSet)

urlpatterns = [
    path('task/create/', TaskCreateView.as_view(), name='create-task'),
    path('task/<int:pk>/partial_update/', TaskPartialUpdateView.as_view(), name='partial-update-task'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('', include(router.urls)),  # Użycie routerów do obsługi ViewSet
]