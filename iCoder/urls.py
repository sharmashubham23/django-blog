"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from blog.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name="Contact"),
    path('about/', views.about, name="About"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('blog/', include('blog.urls')),
    path('', views.home, name="home"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]

admin.site.site_header="iCoder Admin"
admin.site.site_title="iCoder Admin Panel"
admin.site.index_title="Welcome to iCoder Admin Panel"
