from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    