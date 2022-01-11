from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework.settings import api_settings

from profiles_api import serializer
from profiles_api import models
from  profiles_api import permissions

#from rest_framework import authentication, permissions
#from django.contrib.auth.models import User


class HelloApiView(APIView):
    """Test APIVIEW"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API features """
        an_apiview = [
            'User an HTTP(get, post, patch, put, delete)',
            'is similar to a tradational Django view'    ,
            'gives you the most control over your app logic' ,
            'mapped manually'
        ]

        return Response({
                        'message' : 'hello world',
                        'an_apiview' : an_apiview
                        })

    def post(self, request):
        """post hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            name =  serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message' : message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """modify name"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """partial update"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """delete"""
        return Response({'method' : 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """create a viewset that is differnte from the above"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """ return a hello message"""
        view_set = [
                        'Uses action, list, create, partial_update, retreive',
                        'automatically maps to urls using routers',
                        'provides mose functionality with less code',
                        ]

        return Response({
                            'message': 'hello',
                            'view_set' : view_set
        })

    def create(self, request):
        """ create a new message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =  serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message' : message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ handle getting an object by id"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """updates an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """ updates part of the object"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """ deletes an object"""
        return Response({'http_method' : 'DELETE'})



###########################################################
class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes    = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

###########################################################

class UserLoginApiView(ObtainAuthToken):
    """handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

###########################################################
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
                        permissions.UpdateOwnFeed,
                        IsAuthenticated,
                        )


    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
