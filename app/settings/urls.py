from django.contrib import admin
from django.urls import path, include
from product.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls")),
    path("", include("account.urls")),
    path("", include("currency.urls")),
    path('', HomeView.as_view(), name="home-link"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
