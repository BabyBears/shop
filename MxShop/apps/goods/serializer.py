from rest_framework import serializers

from .models import Goods,GoodsCategory

class CategorySerializer3(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Goods.objects.create(**validated_data)
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name','click_num','market_price','add_time')
        fields = "__all__"


