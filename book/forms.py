from django.forms import ModelForm

from book.models import *


class BookForm(ModelForm):

    class Meta:

        model = Books
        fields = '__all__'
