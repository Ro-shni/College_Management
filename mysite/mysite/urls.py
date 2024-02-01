"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
#from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home',views.index,name='home'),
    #path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logoutpage, name='logout'),
    path('student1/',views.student1,name='student1'),
    path('student1/detail/<int:pk>/',views.studentdetail,name='studentdetail'),
    path('certi',views.certi, name='certi'),
    path('display',views.display, name='display'),
    path('profile',views.profile, name='profile'),
    path('favicon.ico', views.favicon, name='favicon'),
    path('certi/delete/<int:pk>/', views.certidel, name='certidel'),
    path('certi/update/<int:pk>/', views.certiupdate, name='certiupdate'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
