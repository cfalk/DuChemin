from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from duchemin.models.piece import DCPiece
from duchemin.models.phrase import DCPhrase
from duchemin.models.analysis import DCAnalysis
from duchemin.models.book import DCBook


def home(request):
    data = {
        'user': request.user
    }
    print dir(request.user)
    return render(request, 'main/home.html', data)


def book(request, book_id):
    try:
        book = DCBook.objects.get(book_id=book_id)
        pieces = DCPiece.objects.filter(book_id=book_id)
    except DCBook.DoesNotExist:
        raise Http404
    return render(request, 'main/book.html', {'book': book, 'pieces': pieces})


def books(request):
    books = DCBook.objects.all()
    paginator = Paginator(books, 25)

    page = request.GET.get('page')
    try:
        all_books = paginator.page(page)
    except PageNotAnInteger:
        all_books = paginator.page(1)
    except EmptyPage:
        all_books = paginator.page(paginator.num_pages)

    return render(request, 'main/books.html', {'books': all_books})


def pieces(request):
    pieces = DCPiece.objects.all()
    paginator = Paginator(pieces, 25)

    page = request.GET.get('page')
    try:
        all_pieces = paginator.page(page)
    except PageNotAnInteger:
        all_pieces = paginator.page(1)
    except EmptyPage:
        all_pieces = paginator.page(paginator.num_pages)

    return render(request, 'main/pieces.html', {'pieces': all_pieces})


def piece(request, piece_id):
    try:
        piece = DCPiece.objects.get(piece_id=piece_id)
    except DCPiece.DoesNotExist:
        raise Http404

    phrases = DCPhrase.objects.filter(piece_id=piece_id).order_by('phrase_num')
    analyses = DCAnalysis.objects.filter(composition_number=piece_id).order_by('start_measure')

    data = {
        'is_piece': True,
        'piece': piece,
        'phrases': phrases,
        'analyses': analyses
    }
    return render(request, 'main/piece.html', data)


@login_required(login_url="/login/")
def profile(request):
    profile = request.user.get_profile()
    data = {
        'user': request.user,
        'profile': profile,
        'favourited': profile.favourited.iterator()
    }
    return render(request, 'main/profile.html', data)


def login(request):
    return render(request, 'main/login.html')
