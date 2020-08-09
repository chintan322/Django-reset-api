from django.urls import path

from .views import (
    StatusAPIView, 
    # StatusCreateAPIView, 
    # StatusDetailAPIView, 
    # StatusUpdateAPIView, 
    # StatusDeleteAPIView
    )

urlpatterns = [

    path('', StatusAPIView.as_view()),
    # path('<int:pk>/', StatusDetailAPIView.as_view()),
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', StatusDeleteAPIView .as_view()),
]

# Start with
# /api/status/ ->List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update/ -> Update
# /api/status/12/delete/ -> Delete

# End with

# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# FINAL

# /api/status/ -> CRUD & LS