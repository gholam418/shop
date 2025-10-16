from django.shortcuts import render
from rest_framework.views import APIView
from  django.http import JsonResponse
# Create your views here.
class Register(APIView):
    @staticmethod
    def get(self , request):
        return JsonResponse({"name":"Ali"})
    
    


class Login(APIView):
    pass


class ForgetPass(APIView):
    pass


class UpdateProfile(APIView):
    pass

