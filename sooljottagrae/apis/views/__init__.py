from .post import (
        PostListAPIView,
        PostCreateAPIView,
        PostDetailAPIView,
        PostUpdateAPIView,
        PostDeleteAPIView,
)

from .user import (
        UserCreateAPIView,
        UserLoginAPIView,
        UserListAPIView,
        UserDetailAPIView,
)

from .comment import(
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentGeneralListAPIView,
    CommentSpecificListAPIView,
)

from .tag import(
    AlcoholTagListAPIView,
    FoodTagListAPIView,
    PlaceTagListAPIView,
)

from .pagination import *
