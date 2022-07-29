from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from book.forms import BookForm
from book.models import Books, RequestBook


class BookCreate(CreateView):
    template_name = 'user/main.html'
    model = Books
    form_class = BookForm
    success_url = '/book-list/'


    # def post(self, request, *args, **kwargs):
    #     # self.object = None
    #     import pdb; pdb.set_trace()
    #     return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return 'book-list' + '/' + str(self.request.user.id)
    #
    #     # return reverse('book_list', kwargs={"pk": self.request.user.id})


class BookUpdate(UpdateView):
    template_name = 'user/main.html'
    model = Books
    form_class = BookForm
    success_url = ""


class BookDelete(DeleteView):
    template_name = 'book/.html'
    model = Books


class BookDetail(DetailView):
    template_name = 'book/detail.html'
    model = Books
    success_url = ""


class BookList(ListView):
    template_name = 'profile (1).html'
    model = Books


# class RequestBooks(CreateView):
#     model = RequestBook
#     success_url = reverse_lazy('book_list')
#     fields = '__all__'
#     template_name = 'book/detail.html'
#
#     def post(self, request, *args, **kwargs):
#         import pdb
#         pdb.set_trace()
#         book = Books.objects.filter(user=self.request.user.pk).first()
#         RequestBook.objects.create(name=request.user, book_name=book)
#         return super(RequestBooks, self).post(request, *args, **kwargs)
    #     # return redirect("main.html")
    #     return render(request, 'profile (1).html', {'filter': book})
    #

def create_book_request(request):
    if request.method == 'GET':
        book = Books.objects.filter(user=request.user.pk).first()
        # import pdb
        # pdb.set_trace()
        RequestBook.objects.create(name=request.user, book_name=book)
        RequestBook.objects.update(status='assigned')
        # request_book.save()

        # RequestBook.objects.filter(pk=request.user.id).update(status='assigned')
        return redirect('book_list')


class RequestedBookListView(ListView):
    template_name = 'book/requstedbook.html'
    model = RequestBook

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RequestedBookListView, self).get_context_data(**kwargs)
        request_books = RequestBook.objects.filter(name=self.request.user)
        context.update({'request_books': request_books})

        # import pdb;
        # pdb.set_trace()
        books=Books.objects.filter(id=self.request.user.id)
        RequestBook.objects.filter(book_name=books).exclude(name=self.request.user.id)

        return context


class RequestedBookDeleteView(DeleteView):
    model = RequestBook
    template_name = 'delete.html'

    # def get_success_url(self):
    #     return 'requested_book_list' + '/' + str(self.request.user.id)


class notification(ListView):
    model = RequestBook
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = {}
        contex['data'] = RequestBook.objects.filter(name=self.request.user).first()
        # import pdb;
        # pdb.set_trace()
        RequestBook.objects.filter(name=self.request.user)
            # .exclude(book_name=self.request.user.book)
        return contex


    # def get_queryset(self, **kwargs):
    #     import pdb;
    #     pdb.set_trace()
    #     return RequestBook.objects.filter(id=self.request.user.id).first()
