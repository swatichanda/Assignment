from django.urls import path, include
from rest_framework import routers
from Api import views  #UserCreateAPIView

router = routers.DefaultRouter()
router.register('works',views.WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/'.as_view())#UserCreateAPIView.as_view()),
]
