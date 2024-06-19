from rest_framework import serializers
from .models import Task, BackLog
from users.models import User
from users.serializer import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assignedUser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'assignedUser', 'status']

        extra_kwargs = {
            'assignedUser': {'required': False},
        }


class BackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackLog
        fields = ['id', 'task_data', 'modification_date']


class TaskPartialUpdateSerializer(serializers.ModelSerializer):
    assignedUser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'assignedUser', 'status']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'assignedUser': {'required': False},
            'status': {'required': False},
        }

