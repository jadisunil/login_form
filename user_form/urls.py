from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),  # Redirect to register view for the root URL
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # This is correct
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout view
    # Add your other URL patterns here
]
