from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('addsub/', views.add_sub, name='addsub'),
    path('incatt/<int:id>', views.inc_att, name='incatt'),
    path('decatt/<int:id>', views.dec_att, name='decatt'),
    path('updateatt/<int:id>', views.update_att, name='updateatt'),
    path('delatt/<int:id>', views.del_att, name='delatt'),
]