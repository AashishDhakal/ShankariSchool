"""ShankariSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .views import Homepage,NoticeDetailView,AboutDetailView,page_not_found_view,handler500,GalleryView,ParentInformationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage,name="home"),
    path('<slug>/',NoticeDetailView.as_view(),name="noticedetail"),
    path('about/<slug>/',AboutDetailView.as_view(),name="aboutdetail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('school/gallery/',GalleryView,name="gallery"),
    path('admission/',include('admission.urls'),name='admission'),
    path('survey/parent/',ParentInformationView,name='parentinformation'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = "Shankari School Admin"
admin.site.site_title = "Shankari School Portal"
admin.site.index_title = "Welcome to Shankari School Admin Portal"
