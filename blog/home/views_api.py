from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .helpers import generate_random_string, send_mail_to_user
from django.contrib.auth import authenticate, login

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key username not found'
                raise Exception('Key username not found')
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('Key password not found')
            
            check_user = User.objects.filter(username=data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid username, user not found'
                raise Exception('Invalid username, user not found')
            
            if not Profile.objects.filter(user=check_user).first().is_verified:
                response['message'] = 'Your Profile is not Verified'
                raise Exception('Profile not Verified.')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid password'
                raise Exception('Invalid password')
        except Exception as e:
            print(e)
        
        return Response(response)

class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key username not found'
                raise Exception('Key username not found')
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('Key password not found')
            
            check_user = User.objects.filter(username=data.get('username')).first()
            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')
            user_objs = User.objects.create_user(**data)
            # user_objs = User.objects.create(username = data.get('username'))
            # user_objs.set_password = (data.get('password'))
            user_objs.save()

            token = generate_random_string(20)
            Profile.objects.create(user=user_objs, token=token)
            send_mail_to_user(token, data.get('email'))
            response['status'] = 200
            response['message'] = 'Verify your account through email sent to your respective Email id.'

        except Exception as e:
            print(e)
        
        return Response(response)