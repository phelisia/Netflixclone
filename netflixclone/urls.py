"""netflixclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from netflix.views import index_view, login_view, register_view
from netflix.views import logout_view
from netflix.views import detail_view
 # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'), # Add this line
    path('login',login_view, name='login'),
    path('register',register_view,name='register'),
    path('logout', logout_view,name='logout'),
    path('movie_detail', detail_view,name='movie_detail')
]

# Add the lines below
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

