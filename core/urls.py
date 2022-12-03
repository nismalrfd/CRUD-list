from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('', views.register, name='register'),
    # path('login_page', views.login_page, name='login_page'),

    path('update_task/<int:id>', views.update_task, name='update_task'),
    path('delete_taks/<int:id>', views.delete_taks, name='delete_taks'),

]