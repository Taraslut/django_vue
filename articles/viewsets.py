from rest_framework import viewsets, status
from rest_framework.response import Response

from articles.models import Article
from articles.serializer import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

