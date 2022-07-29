from django.contrib import admin

# Register your models here.
from book.models import Books, BookCategory, RequestBook

admin.site.register(Books)
admin.site.register(BookCategory)
admin.site.register(RequestBook)

