from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
import json
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

def registerUser():
    #first put the user in the database
    data = {
        'email':'John.Doe@ibm.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'cnum':'123456789',
    }
    

    client = APIClient(enforce_csrf_checks=True)

    response = client.post('/manage/user/register/',json.dumps(data),content_type='application/json')

    return response


# Create your tests here.
class UserTest(TestCase):
    #this test will create user and assert the response status code
    def testWillCreateUser(self):
        response = registerUser()

        self.assertEqual(status.HTTP_200_OK, response.status_code)


    #this test will retrieve user and assert the response status code
    def testWillRetrieveUser(self):
        response = registerUser()

        #search the user and compare if this user exist 
        client = APIClient(enforce_csrf_checks=True)
        client.credentials(HTTP_AUTHORIZATION='123456789')

        response = client.get('/manage/user/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)


    #this test will update user tokens and assert the response status code
    def testWillUpdateUserTokens(self):
        registerUser()

        data = {
            'GH_TOKEN': env('TOKEN_GH'),
            'ZH_TOKEN': env('TOKEN_ZH'),
        }

        client = APIClient(enforce_csrf_checks=True)
        client.credentials(HTTP_AUTHORIZATION='123456789')

        response = client.post('/manage/tokens/',json.dumps(data),content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)