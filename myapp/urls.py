from django.urls import include, path
from django.conf.urls import url
from . import views


urlpatterns = [    
    url(r'api/users/create/$', views.UserCreateAPIView.as_view(), name='create'),
    
    path('api/hello/', views.HelloAPI.as_view(), name = 'hello_api'),
    path('api/hello2/', views.hello_drf, name='hello_api2'), 

    # role-based
    path('api/hellorole/', views.HelloRoleAPI.as_view(), name = 'hello_role_api'),
    path('api/hellorole2/', views.hello_role_drf, name='hello_role_api2'), 
]