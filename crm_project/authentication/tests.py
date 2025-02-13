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
        print("Form errors:", response.context['form'].errors)

        self.assertFormError(response.context['form'],'password2',"Введенные пароли не совпадают.")
        self.assertTemplateUsed(response,'crm_project/registration.html')
        
        
        
        self.assertEqual(User.objects.count(),0)