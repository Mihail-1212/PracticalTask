import datetime
import base64

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from . import models


User = get_user_model()

password = 'password'
username = 'username'

class TaskListViewTests(TestCase):
    """
    View need auth => username and password
    """

    @classmethod
    def setUpTestData(cls):
        # Create tasks for pagination tests
        number_of_tasks = 13
        new_user = User.objects.create(username=username,first_name='first_name', last_name='last_name')
        new_user.set_password(password)
        new_user.save()
        for task_number in range(number_of_tasks):
            models.Task.objects.create(name='Work with %s' % task_number, date_start=datetime.datetime.now(), user=new_user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username=username, password=password)
        resp = self.client.get('/tasks/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username=username, password=password)
        resp = self.client.get(reverse('task_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username=username, password=password)
        resp = self.client.get(reverse('task_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'webdiary/task_list.html')

    def test_pagination_is_ten(self):
        self.client.login(username=username, password=password)
        resp = self.client.get(reverse('task_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['tasks']) == 10)
