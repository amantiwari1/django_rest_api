from .models import Article
from .serializer import ArticleSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


class SubscriberViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


# class ArticesAPI(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializers(articles, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ArticleSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class DetailsAPI(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(pk=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         articles = self.get_object(id)
#         serializer = ArticleSerializers(articles)
#         return Response(serializer.data)

#     def put(self, request,id):
#         articles = self.get_object(id)
#         serializer = ArticleSerializers(articles,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         articles = self.get_object(id)
#         articles.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





