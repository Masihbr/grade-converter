from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.UserSignUpAPIView.as_view(), name='sign-up'),
]