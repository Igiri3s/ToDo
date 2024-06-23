import unittest
from unittest.mock import patch, Mock
from api.views import Task


def list_tasks():
    return Task.objects.all()


class TestListTasks(unittest.TestCase):
    @patch('api.views.Task.objects.all')
    def test_list_tasks(self, mock):

        # before
        mock_task = Mock(spec=Task)
        mock_task.id = 1
        mock_task.name = "Zrobić pranie"
        mock_task.description = "Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania."
        mock_task.assignedUser.email = "b@b.com"
        mock_task.status = "NEW"

        # when
        mock.return_value = [mock_task]
        tasks = list_tasks()

        # then
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].name, "Zrobić pranie")


if __name__ == '__main__':
    unittest.main()
