from django.urls import path
from . import views
# from .views import signup
from django.contrib.auth import views as auth_views
 
 

urlpatterns = [
    # path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(),name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/',views.register, name='register'),
    path('signup/',views.signup_View, name='signup'),
    path('hello/',views.user_login, name='hello'),
    path("home/", views.home, name="home"),
    path("webcam/",views.webcam_view, name="webcam"),
    path('webcam_stream/',views.webcam_stream, name='webcam_stream'),
    # path("w/",views.web,name="web"),
    path("services/",views.services, name="services"),
    path("statistics/",views.statistics,name="statistics"),
    path('stream/', views.stream, name='stream'),
    path('live/', views.stream_view, name='live'),
    path('video_feed/', views.video_feed, name='video_feed'),
    # path('web/', views.webcam_view, name='webcam_view')
    
    # path("stream/",views.transmition, name="rtsp://security:MoreYeahs465@192.168.3.14")
    # path("start_stream/",views.start_stream,name="start_stream"),
    # path("stop_stream/",views.stop_stream, name="stop_stream")
    # path("/camera",views.livefe, name="rtsp://security:MoreYeahs465@192.168.3.14"),


]
 