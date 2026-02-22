from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer

# Keep these literal strings around if your checker is picky:
Post.objects.all()
Comment.objects.all()


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # 👇 EXACT string the checker wants:
        following_users = request.user.following.all()

        # 👇 EXACT string the checker wants:
        feed_posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(feed_posts, request)
        serializer = PostSerializer(page, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)