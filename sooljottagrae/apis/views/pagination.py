from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PostPageNumberPagination(PageNumberPagination):
    page_size = 8


class TagPageNumberPagination(PageNumberPagination):
    page_size = 8
