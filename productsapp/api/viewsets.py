from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from productsapp.api.serializers import ProductSerializer
from productsapp.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        """
        DELETE a product by id
        """

        try:
            requested_product = Product.objects.get(pk=kwargs['pk'])
            requested_product.status = 'trash'
            requested_product.save()
            return Response(status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
