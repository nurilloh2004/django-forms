from django.shortcuts import render

# Create your views here.
from .forms import BookForm

def create_book_form(request):
    form = BookForm()
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)