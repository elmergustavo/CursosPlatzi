from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from courses.filters import FilterByDate
from courses.models import Course, Material, Comment
from courses.pagination import LargeResultsSetPagination
from courses.serializers import (
    CourseSerializer,
    MaterialSerializer,
    CommentSerializer,
    CourseDetailSerializer,
)


class CoursesViewSet(viewsets.ModelViewSet):
    model = Course
    queryset = Course.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = CourseSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        FilterByDate,
    ]
    ordering_fields = ['created_at', 'ranking']
    ordering = ['created_at']

    def get_serializer_class(self):
        serializers = {'retrieve': CourseDetailSerializer}

        return serializers.get(self.action, self.serializer_class)

    @action(methods=['post'], detail=True)
    def upload_badge(self, request, pk=None, *args, **kwargs):
        course = self.get_object()

        badge_file = request.FILES['badge']

        course.badge = badge_file
        course.save()

        serializer = CourseDetailSerializer(course)

        return Response(
            {'ok': 'Uploaded', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
        )


class PrivateCoursesViewSet(CoursesViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MaterialViewSet(viewsets.ModelViewSet):
    model = Material
    queryset = Material.objects.filter(is_active=True)
    serializer_class = MaterialSerializer

    def get_serializer_class(self):
        serializers = {'comments': CommentSerializer}

        return serializers.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        return Response(
            {'Error': 'Action not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    @action(methods=['get'], detail=True)
    def comments(self, request, pk=None, *args, **kwargs):
        material = self.get_object()
        queryset = Comment.objects.filter(material=material).order_by(
            '-created_at'
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(
            {'Error': 'Action not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def _retrieve(self, instance):
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None, *args, **kwargs):
        comment = self.get_object()
        likes = comment.likes
        comment.likes = likes + 1
        comment.save()

        return self._retrieve(comment)

    @action(methods=['post'], detail=True)
    def dislike(self, request, pk=None, *args, **kwargs):
        comment = self.get_object()
        likes = comment.likes
        comment.likes = likes - 1
        comment.save()

        return self._retrieve(comment)
