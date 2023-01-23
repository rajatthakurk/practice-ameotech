from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.models import User
class HomeView(APIView):
    def get(self,request):
        return JsonResponse({
            "message":"Hello from django docker is working"
        })