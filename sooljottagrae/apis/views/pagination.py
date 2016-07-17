from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class PostPageNumberPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
