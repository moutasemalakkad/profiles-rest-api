from django.urls  import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello_viewset')
router.register('h', views.HelloViewSet, base_name='hello_viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    #path('hello_view_set/', views.HelloViewSet.as_view()),
    path('', include(router.urls))
]
