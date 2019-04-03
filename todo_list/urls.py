from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('list/delete/<int:pk>',views.delete, name = 'delete'),
    path('list/cross/<int:pk>',views.done, name = 'done'),
    path('list/uncross/<int:pk>',views.not_done, name = 'not_done'),
    path('list/edit/<int:pk>',views.edit, name = 'edit'),

]
