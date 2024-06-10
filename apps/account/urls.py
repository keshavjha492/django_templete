from django.urls import path
from . import views


urlpatterns = [
    path("user-register/", views.UserRegisterView.as_view(), name="user_register"),
    path("user-login/", views.UserLoginView.as_view(), name="user_login"),
    path("user-logout/", views.UserLogout, name="user_logout"),
    path("activate/<str:username>/<str:key>/", views.UserAccountActivationView.as_view(), name="ac_activation"),
    path("resend_activation_url/<int:id>/", views.ResendActivation.as_view(), name="resend_ac_activation"),
    path("user_profile/<int:id>/", views.UserProfileView.as_view(), name="user_profile"),
]