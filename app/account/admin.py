from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    resource_class = Product
    list_display = (
        "name_product",
        "price",
        "description",
        "created",
        "image"
    )
    list_filter = (
        "price",
    )
    search_fields = (
        "name_product",
    )
    readonly_fields = (
        "name_product",
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Product, ProductAdmin)
