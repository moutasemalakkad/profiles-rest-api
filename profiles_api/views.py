from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework import authentication, permissions
#from django.contrib.auth.models import User


class HelloApiView(APIView):
    """Test APIVIEW"""

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
