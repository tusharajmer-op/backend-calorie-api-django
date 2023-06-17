from django.urls import path,include
from user.views import viewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user',viewsSet.userViewSet)
router.register(r'manager',viewsSet().managerViewSet)
urlpatterns = [
    path('/',include(router.urls)),
    ]
