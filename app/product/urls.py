from django.urls import path
from product.views import CreateProductView
from product.views import ProductListView
from product.views import ProductDetailsView
from product.views import ProductUpdateView
from product.views import ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create", CreateProductView.as_view(), name="create-link"),
    path("product_list", ProductListView.as_view(), name="list-link"),
    path("product_details/<int:pk>", ProductDetailsView.as_view(), name="details-link"),
    path("product_delete/<int:pk>", ProductDeleteView.as_view(), name="delete-link"),
    path("product_update/<int:pk>", ProductUpdateView.as_view(), name="update-link"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
