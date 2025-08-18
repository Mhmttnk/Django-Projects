from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . models import Book_Management

def home(request):
    return render(request, 'books/home.html')

def add_book(request):
    if request.method == 'POST':
        book_name=request.POST.get('book_name')
        author=request.POST.get('author')
        page=request.POST.get('page')
        type=request.POST.get('type')
        publication_date=request.POST.get('publication_date')

        if book_name and author and page and type and publication_date:      
            Book_Management.objects.create(
                book_name = book_name,
                author = author,
                page = page,
                type = type,
                publication_date = publication_date)
            messages.success(request, 'Kitap Başarıyla Eklendi')
            return redirect('add_book')
    
    books=Book_Management.objects.all()
    return render(request, 'books/add_book.html',{'books':books})

def delete_book(request):
    books=Book_Management.objects.all()
    
    if request.method == 'POST':
        book_id=request.POST.get('book_id')
        try:
            book_to_delete=Book_Management.objects.get(id=book_id)
            book_to_delete.delete()
            messages.success(request, 'Kitap Başarıyla Silindi')
            return redirect('delete_book')
        except Book_Management.DoesNotExist:
            messages.error(request, 'Hata: Bu ID İle Eşleşen Bir Kitap Bulunamadı.')
    
    return render(request, 'books/delete_book.html', {'books': books})

def list_book(request):
        books=Book_Management.objects.all()
        return render(request, 'books/list_book.html', {'books':books}) 
 
def edit_book(request, id):
    books=get_object_or_404(Book_Management, id=id)

    if request.method == 'POST':
        books.book_name=request.POST.get('book_name')
        books.author=request.POST.get('author')
        books.page=request.POST.get('page')
        books.type=request.POST.get('type')
        books.publication_date=request.POST.get('publication_date')
        books.save()
        return redirect('list_book')
    
    return render(request, 'books/edit_book.html', {'books':books})