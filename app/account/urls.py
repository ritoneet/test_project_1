from django.contrib import admin
from django.urls import path, include
from account.views import MyPageView
from account.views import RegPageView
from account.views import ActivateView


urlpatterns = [
    path("auth/", include('django.contrib.auth.urls')),
    path("my-page/<int:pk>", MyPageView.as_view(), name="my-page-link"),
    path("reg-page", RegPageView.as_view(), name="reg-link"),
    path("activate/<username>/", ActivateView.as_view(), name="activate-link"),
]
