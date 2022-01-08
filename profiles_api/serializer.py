from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIVIEWS"""
    #email         = models.EmailField(max_length=255, unique=True)
    name          = serializers.CharField(max_length=10)
    #is_active     = models.BooleanField(default=True)
    #is_staff      = models.BooleanField(default=False)
