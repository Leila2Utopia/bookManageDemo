from django.shortcuts import render,HttpResponse,redirect
from app02 import models

# Create your views here.
def login(request):
    err_msg = ''
    if request.method == 'POST':
        name = request.POST.get("name12")
        pwd = request.POST.get("pwd12")
        if name == 'lary' and pwd == '123456':
            return redirect('/book_list/')
        else:
            err_msg = 'name or pwd wrong!'
    return render(request, 'login.html', {"error": err_msg})

def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {"books": books})

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        models.Book.objects.create(title=book_name)
        return redirect('/book_list/')
    return render(request,'add_book.html')

def edit_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        new_book_title = request.POST.get('book_name')
        book_obj = models.Book.objects.get(id=book_id)
        book_obj.title = new_book_title
        book_obj.save()
        return redirect('/book_list/')
    edit_id = request.GET.get('id')
    book = models.Book.objects.get(id=edit_id)
    return render(request, 'edit_book.html', {"book": book})

def delete_book(request):
    delete_id = request.GET.get('id')
    models.Book.objects.get(id=delete_id).delete()
    return redirect('/book_list/')