from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from src.tasks.models import Task
from src.users.models import User


class TaskViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            due_date=timezone.now()
        )

    def test_create_task(self):
        url = reverse('create_task')
        data = {
            "title": "TestTitle",
            "description": "TestDescription",
            "due_date_timestamp": int(timezone.now().timestamp()) + 60*60*24,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_details(self):
        url = reverse('get_task_details', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        url = reverse('update_task', args=[self.task.id])
        data = {
            'title': 'Updated Task'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('get_task_details', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_explore_task(self):
        url = reverse('explore_task')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
