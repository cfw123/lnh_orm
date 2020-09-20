from django.shortcuts import render, HttpResponse, redirect, reverse
from app01.models import Book
# Create your views here.

import datetime

from app01.models import Book


def addbook(request):
    # book=Book(title="python1",price=123,pub_date="2015-09-12",publish="pcec01")
    # book.save()
    if request.method == 'GET':
        return render(request, "addbook.html")
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")

        book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish=publish)

        return redirect(reverse('book:index'))


def books(request):
    book_list = Book.objects.filter()
    context = {
        'bookList': book_list,
    }
    return render(request, "books.html", context)


def delbook(request, delete_book_id):
    Book.objects.filter(nid=delete_book_id).delete()
    return redirect(reverse('book:index'))


def editbook(request,edit_book_id):
    """
    编辑功能：
       #Book.objects.filter(nid=edit_book_id).update(price=111)
       #Book.objects.filter(price=111).update(publish="南京出版社")

    :param request:
    :param edit_book_id:
    :return:
    """
    if request.method=="GET":
        edit_book = Book.objects.filter(nid=edit_book_id)[0]
        return render(request, "editbook.html", {"edit_book": edit_book})

    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        Book.objects.filter(nid=edit_book_id).update(title=title,
                                                     price=price,
                                                     pub_date=pub_date,
                                                     publish=publish)



        return redirect(reverse("book:index"))
