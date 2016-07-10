from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "해당 내용의 작성자만 가능합니다."
    my_safe_method = ['GET','PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

"""
referred cfr lecture blog api with django rest framework.

Its commit - https://github.com/codingforentrepreneurs/Blog-API-with-Django-Rest-Framework/commit/76eb764398628691a2be59bc87a541995913e2d7
"""
