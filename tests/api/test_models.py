from django.test import TestCase
from api.models import BackLog

class Task:
    def __init__(self, id, name, description, status, assignedUser):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.assignedUser = assignedUser

class User:
    def __init__(self, email):
        self.email = email

class BackLogTestCase(TestCase):
    def test_set_backlog_data(self):
        #before
        user = User(email="b@b.com")
        example_task = Task(
            id=1,
            name="Zrobić pranie",
            description="Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania.",
            status="NEW",
            assignedUser=user
        )

        #when
        backlog = BackLog.set_backlog_data(example_task)

        #then
        self.assertEqual(backlog.task_data, {
            'id': 1,
            'name': "Zrobić pranie",
            'description': "Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania.",
            'assignedUser': "b@b.com",
            'status': "NEW"
        })