from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('post/<str:pk>/', views.post, name='post'),

    # path('register-page/', views.register_page, name='register-page'),
    # path('login-page/', views.login_page, name='login-page'),
    # path('logout-user/', views.logout_user, name='logout-user'),

    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<str:pk>', views.update_post, name='update-post'),
    path('delete-post/<str:pk>', views.delete_post, name='delete-post'),
]
