from .models import Article
from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id","title","author","email"]
    