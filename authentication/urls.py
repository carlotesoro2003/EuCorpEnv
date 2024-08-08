from django.urls import path
from .views import EmailValidationView, LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', csrf_exempt(LoginView.as_view()), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('validate-email/', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
]
