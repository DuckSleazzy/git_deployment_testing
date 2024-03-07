from django.urls import path
from AppThree import views

# template tagging
app_name = "AppThree"

urlpatterns = [
    path("relative/",views.relative, name="relative"),
    path("other/",views.other, name="other"),
    path("register/",views.register, name="register"),
    path("user_login/",views.user_login, name="user_login"),
    
]