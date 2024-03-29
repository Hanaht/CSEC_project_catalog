"""
csec_project_catalog_authentication urls

"""
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path("register/", views.registeration, name="register"),
    path("profile/", views.ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", views.ProfileEditView.as_view(), name="profile_edit"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html",
            success_url="/auth/change-password/done",
        ),
        name="change_password",
    ),
    path(
        "change-password/done",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/change_password_done.html",
        ),
        name="change_password_done",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password-reset/password_reset_form.html",
            subject_template_name="registration/password-reset/password_reset_subject.txt",
            email_template_name="registration/password-reset/password_reset_email.html",
            success_url="/auth/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password-reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password-reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password-reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
