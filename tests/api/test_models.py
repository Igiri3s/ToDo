import unittest
from unittest.mock import patch, Mock
from api.views import Task, BackLog
from api.models import User


class BackLogTestCase(unittest.TestCase):
    @patch('api.views.BackLog.set_backlog_data')
    def test_set_backlog_data(self, mock_set_backlog_data):

        # before
        mock_user = Mock(spec=User)
        mock_user.email = "b@b.com"

        mock_task = Mock(spec=Task)
        mock_task.id = 1
        mock_task.name = "Zrobić pranie"
        mock_task.description = "Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania."
        mock_task.status = "NEW"
        mock_task.assignedUser = mock_user

        # when
        mock_backlog = Mock()
        mock_backlog.task_data = {
            'id': 1,
            'name': "Zrobić pranie",
            'description': "Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania.",
            'assignedUser': "b@b.com",
            'status': "NEW",
        }
        mock_set_backlog_data.return_value = mock_backlog

        backlog = BackLog.set_backlog_data(mock_task)

        # then
        self.assertEqual(backlog.task_data, {
            'id': 1,
            'name': "Zrobić pranie",
            'description': "Posortować ubrania, włożyć do pralki, dodać detergent i uruchomić program prania.",
            'assignedUser': "b@b.com",
            'status': "NEW",
        })


if __name__ == '__main__':
    unittest.main()
