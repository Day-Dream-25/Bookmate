from urllib.request import Request

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from book.views import BookList, BookDetail, BookDelete, BookUpdate, BookCreate, notification, create_book_request, RequestedBookListView, RequestedBookDeleteView
# , RequestBook
from user.views import *

urlpatterns = [
    path('book-list/', BookList.as_view(), name="book_list"),
    path('book-detail/<int:pk>', BookDetail.as_view(), name="book_detail"),
    path('book-delete/', BookDelete .as_view(), name='book_delete'),
    path('book-update/', BookUpdate.as_view(), name="book_update"),
    path('book-create/', BookCreate.as_view(), name="book_create"),

    path('request/', create_book_request, name="request_book"),

    path('requestedbook/<int:pk>', RequestedBookListView.as_view(), name="requested_book_list"),
    path('requestedbookdelete/<int:pk>', RequestedBookDeleteView.as_view(), name="requested_book_delete"),
    path('notification/<int:pk>', notification.as_view(), name="notification"),

]