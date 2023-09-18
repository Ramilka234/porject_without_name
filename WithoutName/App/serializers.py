from rest_framework import serializers

from .models import Game, Review


class FilterReviewListSerializer(serializers.ListSerializer):
    """Вывод комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзывов"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('name', 'text', 'children',)


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'picture', 'cat_id')


class GameDetailSerializer(serializers.ModelSerializer):
    cat_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    review = ReviewSerializer(many=True, source='get_reviews')
    class Meta:
        model = Game
        exclude = ('draft',)
