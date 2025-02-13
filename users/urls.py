from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("profile/", views.profile, name="profile"),
    # FOR LOGIN PAGE AND THE ROUTING IS DONE IN THE SETTINGS.PY
    path(
        "",
        auth_view.LoginView.as_view(template_name="users/login.html"),
        name="users-login",
    ),
    # FOR LOGOUT PAGE
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="users/logout.html"),
        name="users-logout",
    ),
        
    # FOR PASSWORD RESET
    path(
        "password_reset/",
        auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    # FOR PASSWORD RESET DONE
    path(
        "password_reset_done/",
        auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    # FOR PASSWORD RESET CONFIRM
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    # FOR PASSWORD RESET COMPLETE
    path(
        "password_reset_complete/",
        auth_view.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
        name="password_reset_complete",
    ),




]









    
    # # FOR PASSWORD RESET
    # path(
    #     "password_reset/",
    #     auth_view.PasswordResetView.as_view(),
    #     name="password_reset",
    # ),
    # # FOR PASSWORD RESET DONE
    # path(
    #     "password_reset_done/",
    #     auth_view.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # # FOR PASSWORD RESET CONFIRM
    # path(
    #     "password_reset_confirm/<uidb64>/<token>",
    #     auth_view.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # # FOR PASSWORD RESET COMPLETE
    # path(
    #     "password_reset_complete/",
    #     auth_view.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),