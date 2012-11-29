from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from duchemin.models.piece import DCPiece
from duchemin.models.phrase import DCPhrase
from duchemin.models.analysis import DCAnalysis
from duchemin.models.book import DCBook
from duchemin.models.person import DCPerson
from duchemin.models.reconstruction import DCReconstruction
from duchemin.models.content_block import DCContentBlock


def home(request):
    front_page_blocks = DCContentBlock.objects.filter(published=True, content_type="block").order_by('position')
    front_page_blocks = front_page_blocks[0:3]
    news_blocks = DCContentBlock.objects.filter(published=True, content_type="news").order_by('position')
    data = {
        'user': request.user,
        'front_page_blocks': front_page_blocks,
        'news_blocks': news_blocks
    }
    return render(request, 'main/home.html', data)


def book(request, book_id):
    try:
        book = DCBook.objects.get(book_id=book_id)
        pieces = DCPiece.objects.filter(book_id=book_id).order_by('book_position')
    except DCBook.DoesNotExist:
        raise Http404
    return render(request, 'main/book.html', {'book': book, 'pieces': pieces})


def books(request):
    books = DCBook.objects.all().order_by('id')
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
    pieces = DCPiece.objects.all().order_by('book_id__id', 'book_position')
    paginator = Paginator(pieces, 25)

    is_logged_in = False
    if request.user.is_authenticated():
        is_logged_in = True
        profile = request.user.profile
        favourite_pieces = profile.favourited_piece.all()
        for piece in pieces:
            if piece in favourite_pieces:
                piece.is_favourite = True
            else:
                piece.is_favourite = False

    page = request.GET.get('page')
    try:
        all_pieces = paginator.page(page)
    except PageNotAnInteger:
        all_pieces = paginator.page(1)
    except EmptyPage:
        all_pieces = paginator.page(paginator.num_pages)

    return render(request, 'main/pieces.html', { 'pieces': all_pieces, 'is_logged_in': is_logged_in })


def piece(request, piece_id):
    try:
        piece = DCPiece.objects.get(piece_id=piece_id)
    except DCPiece.DoesNotExist:
        raise Http404

    is_favourite = False
    is_logged_in = False
    if request.user.is_authenticated():
        is_logged_in = True
        profile = request.user.profile
        if profile.favourited_piece.filter(id=piece.id):
            is_favourite = True

    phrases = DCPhrase.objects.filter(piece_id=piece_id).order_by('phrase_num')
    analyses = DCAnalysis.objects.filter(composition_number=piece_id).order_by('phrase_number__phrase_num', 'start_measure')
    reconstructions = DCReconstruction.objects.filter(piece=piece_id).order_by('piece')

    data = {
        'piece': piece,
        'phrases': phrases,
        'analyses': analyses,
        'reconstructions': reconstructions,
        'is_favourite': is_favourite,
        'is_logged_in': is_logged_in
    }
    return render(request, 'main/piece.html', data)


def reconstructions(request):
    reconstructions = DCReconstruction.objects.all().order_by('piece__title', 'reconstructor__surname')
    paginator = Paginator(reconstructions, 25)
    page = request.GET.get('page')
    try:
        all_r = paginator.page(page)
    except PageNotAnInteger:
        all_r = paginator.page(1)
    except EmptyPage:
        all_r = paginator.page(paginator.num_pages)

    return render(request, 'main/reconstructions.html', {'reconstructions': all_r})

def reconstruction(request, recon_id):
    try:
        recon = DCReconstruction.objects.get(pk=recon_id)
    except DCReconstructions.DoesNotExist:
        raise Http404

    data = {
        'reconstruction': recon
    }
    return render(request, 'main/reconstruction.html', data)


def people(request):
    people = DCPerson.objects.all().order_by('surname')
    paginator = Paginator(people, 20)
    page = request.GET.get('page')
    try:
        all_people = paginator.page(page)
    except PageNotAnInteger:
        all_people = paginator.page(1)
    except EmptyPage:
        all_people = paginator.page(paginator.num_pages)

    return render(request, 'main/people.html', {'people': all_people})


def person(request, person_id):
    try:
        person = DCPerson.objects.get(person_id=person_id)
    except DCPerson.DoesNotExist:
        raise Http404

    pieces = DCPiece.objects.filter(composer_id=person.person_id)
    analyses = DCAnalysis.objects.filter(analyst=person.person_id)

    data = {
        'person': person,
        'pieces': pieces,
        'analyses': analyses
    }
    return render(request, 'main/person.html', data)


@login_required(login_url="/login/")
def profile(request):
    profile = request.user.profile

    analyses = None
    reconstructions = None
    if profile.person:
        analyses = DCAnalysis.objects.filter(analyst_id=profile.person.person_id).order_by('composition_number__title')
        reconstructions = DCReconstruction.objects.filter(reconstructor=profile.person.person_id).order_by('piece__title')

    data = {
        'user': request.user,
        'profile': profile,
        'favourited_pieces': profile.favourited_piece.iterator(),
        'favourited_analyses': profile.favourited_analysis.iterator(),
        'favourited_reconstructions': profile.favourited_reconstruction.iterator(),
        'my_analyses': analyses,
        'my_reconstructions': reconstructions
    }
    return render(request, 'main/profile.html', data)

def login(request):
    return render(request, 'main/login.html')
