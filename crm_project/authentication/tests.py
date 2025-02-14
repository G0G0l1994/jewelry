from pprint import pprint

from django.test import TestCase
from django.urls import reverse

from .models import User
from .forms import CustomUserCreateForm

class RegistrationViewTest(TestCase):
    

    def setUp(self): #сначала пишем данные для проверки в функции setUp

        self.valid_data = {
            'username': 'testuser',
            'password1':'testUser123testUser',
            'password2':'testUser123testUser',
            'role': '3d'
        }
        self.invalid_data = {
            'username': 'testuser',
            'password1':'testUser123testUser',
            'password2':'testUser321testUser',
            'role': 'manager'
        }

    def test_registration_get_request(self):

        response = self.client.get(reverse('registrations'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'crm_project/registration.html')
        self.assertIsInstance(response.context['form'],CustomUserCreateForm)

    def test_registration_post_valid_data(self):
        response = self.client.post(reverse('registrations'), data=self.valid_data)
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,'/login/')
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.first().username,'testuser')
    
    def test_registration_post_invalid_data(self):
        response = self.client.post(reverse('registrations'),data=self.invalid_data)
        self.assertEqual(response.status_code,200)
        form = response.context['form']
        self.assertTrue(form.is_bound)
        self.assertFormError(response.context['form'],'password2',"Введенные пароли не совпадают.")
        self.assertTemplateUsed(response,'crm_project/registration.html')
        self.assertEqual(User.objects.count(),0)


class LoginTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser',password='testUser123testuser',role='3d')
        self.login_url = reverse('login')
        self.user_data = {
            'username':'testuser',
            'password' : 'testUser123testuser'
            }
        
        self.invalid_user = {
            'username' : 'wronguser',
            'password': 'testUser321testuser'
        }
    
    def test_success_login(self):
        response = self.client.post(self.login_url, data=self.user_data)
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    
    def test_unsuccess_login(self):
        response = self.client.post(self.login_url,data=self.invalid_user)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_authenticated_user_redirect(self):

        self.client.login(**self.user_data)
        response = self.client.get(self.login_url)
        
        self.assertRedirects(response,reverse('dashboard'))