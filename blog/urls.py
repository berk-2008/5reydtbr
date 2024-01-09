
from django.urls import path
from .views import(
    intex,
    CreateBlog,
    DeleteBlog
)

urlpatterns = [

    path('',intex),
    path('create/', CreateBlog),
    path('delete/<int:id>' , DeleteBlog)
]





