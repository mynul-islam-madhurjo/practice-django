from rest_framework import serializers
from .models import Product


# We can have multiple serializers of the same model it can be used for data cleaning as well

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()