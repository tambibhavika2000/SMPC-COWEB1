from django.contrib import admin
from django.urls import path
from ECEapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index,name='dept'),
    path("index/",views.index,name='index'),
    path("student/",views.noticestudent,name='notice'),
    path("teacher/",views.noticeteacher,name='noticeteacher'),
    path("teacher/upload/",views.noticeupload,name='noticeupload'),
    path("delete/<str:pk>",views.delete,name="delete"),
    path("research/",views.research,name="research"),
    path("login/", views.loginpage, name='login'),
    path("register/", views.register, name='register'),
    path("update/",views.update,name='update'),
    path("profile/",views.profile,name='profile'),
    path("research/<str:pk>",views.see,name="see"),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)