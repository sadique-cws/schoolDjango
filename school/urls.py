from django.contrib import admin
from django.urls import path
from sms.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("accounts/login/",login,name="login"),
    path("accounts/register/",register,name="register")
]
