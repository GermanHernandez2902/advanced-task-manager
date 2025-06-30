from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Project, Task
from datetime import date

User = get_user_model()

class ProjectModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpass')
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            owner=self.user
        )

    def test_project_created_with_correct_data(self):
        self.assertEqual(self.project.title, 'Test Project', msg="Project title mismatch")
        self.assertEqual(self.project.description, 'Test Description', msg="Project description mismatch")
        self.assertEqual(self.project.owner, self.user, msg="Project owner mismatch")

    def test_task_created_under_project(self):
        task = Task.objects.create(
            title='Test Task',
            description='Task description',
            status='TODO',
            project=self.project,
            deadline=date.today(),
            owner=self.user,
        )
        self.assertEqual(task.project, self.project, msg="Task not linked to correct project")
        self.assertEqual(task.status, 'TODO', msg="Task status should be 'TODO'")
        self.assertEqual(task.title, 'Test Task', msg="Task title mismatch")

class ProjectViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.client.login(username='user1', password='pass123')
        self.project = Project.objects.create(title='User1 Project', description='...', owner=self.user)

    def test_dashboard_view_returns_200(self):
        url = reverse('project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, msg="Dashboard view did not return 200 for logged-in user")

    def test_redirect_to_login_if_not_logged_in(self):
        self.client.logout()
        url = reverse('project_list')
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}', msg_prefix="Unauthenticated user not redirected to login")
