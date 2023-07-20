from django.urls import path
from .views import login_view, logout_view, user_profile,register_view
from django.contrib.auth import views


urlpatterns = [
    path('password-reset/',
         views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password-reset'),
    path('password-reset-done/',
         views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/',
         views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),
    path('password-change-done/',
         views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),


    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('login1/', views.LoginView.as_view(), name='login1'),
    path('logout1/', views.LogoutView.as_view(), name='logout1'),
    path('users/<str:username>/', user_profile, name='user-profile'),

]
