from rest_framework import serializers
from products.models import Product, Tag, Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
