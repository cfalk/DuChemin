from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from django.conf import settings

import solr

def search(request):
    s = solr.Solr(settings.SOLR_SERVER)
    ret = s.select("*:*", facet="true", facet_field=['contributor', 'composer', 'is_cadence', 'cadence_final_tone', 'cadence_alter', 'cadence_kind', 'text_treatment', 'repeat_kind', 'book_title'], rows="0")

    facets = ret.facet_counts['facet_fields']
    cadence_alter = sorted(facets['cadence_alter'])
    book_title = sorted(facets['book_title'])
    cadence_final_tone = sorted(facets['cadence_final_tone'])
    cadence_kind = sorted(facets['cadence_kind'])
    composer = sorted(facets['composer'])
    contributor = sorted(facets['contributor'])
    is_cadence = sorted(facets['is_cadence'])
    repeat_kind = sorted(facets['repeat_kind'])
    text_treatment = sorted(facets['text_treatment'])

    data = {
        'book_title': book_title,
        'cadence_alter': cadence_alter,
        'cadence_final_tone': cadence_final_tone,
        'cadence_kind': cadence_kind,
        'composer': composer,
        'contributor': contributor,
        'is_cadence': is_cadence,
        'repeat_kind': repeat_kind,
        'text_treatment': text_treatment
    }

    return render(request, 'search/search.html', data)


def query(request):
    print request
    return render(request, 'search/results.html')
