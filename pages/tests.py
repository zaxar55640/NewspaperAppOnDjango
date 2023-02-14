from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class HomePageTests(SimpleTestCase):

    def testHomePageStatusCode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testViewUrlByName(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def testViewCorrectTemplateUsed(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def testSignupPageResponseCode(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def testViewUrlByName(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def testViewCorrectTemplateUsed(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def testSignupForm(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
