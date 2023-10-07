from django.urls import include, path
from rest_framework import routers

from api2.views import PostViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"post", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
