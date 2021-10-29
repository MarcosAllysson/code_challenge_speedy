from rest_framework.serializers import ModelSerializer
from productsimportationapp.models import ProductsImportationHistory


class ProductsImportationHistorySerializer(ModelSerializer):

    class Meta:
        model = ProductsImportationHistory
        fields = (
            "id",
            "is_connection_good",
            "last_time_cron_ran",
            "time_online",
            "memory_usage"
        )
