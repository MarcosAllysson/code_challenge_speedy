from rest_framework.viewsets import ModelViewSet
from productsimportationapp.api.serializers import ProductsImportationHistorySerializer
from productsimportationapp.models import ProductsImportationHistory


class ProductsImportationHistoryViewSet(ModelViewSet):
    queryset = ProductsImportationHistory.objects.all()
    serializer_class = ProductsImportationHistorySerializer
