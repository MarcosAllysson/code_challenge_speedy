from django.contrib import admin
from django.urls import path, include
from productsapp.api.viewsets import ProductViewSet
from productsimportationapp.api.viewsets import ProductsImportationHistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductsImportationHistoryViewSet, basename='ProductsImportationHistory')
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]

admin.site.site_header = "Speedy"
admin.site.site_title = "Painel Admistrativo Speedy"
admin.site.index_title = "Painel Speedy"
