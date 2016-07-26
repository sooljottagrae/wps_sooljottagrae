from .post import (
        PostListAPIView,
        PostCreateAPIView,
        PostDetailAPIView,
        PostUpdateAPIView,
        PostDeleteAPIView,
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

from .user import (
        UserCreateAPIView,
        UserLoginAPIView,
        UserListAPIView,
        UserDetailAPIView,

        MytagsListAPIView,
)
