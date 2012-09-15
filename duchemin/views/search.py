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
        'book_titles': book_title,
        'cadence_alters': cadence_alter,
        'cadence_final_tones': cadence_final_tone,
        'cadence_kinds': cadence_kind,
        'composers': composer,
        'contributors': contributor,
        'is_cadences': is_cadence,
        'repeat_kinds': repeat_kind,
        'text_treatments': text_treatment
    }

    return render(request, 'search/search.html', data)


def query(request):
    s = solr.Solr(settings.SOLR_SERVER)

    qstring = request.GET.get('q', '*:*')
    books = request.GET.getlist('b', '')
    composers = request.GET.getlist('p', '')
    contributors = request.GET.getlist('r', '')
    final_tone = request.GET.getlist('f', '')
    cadence_kind = request.GET.getlist('k', '')
    cadence_alter = request.GET.getlist('m', '')
    text_tone = request.GET.getlist('t', '')
    repeat_kinds = request.GET.getlist('lf', '')

    filter_queries = []
    if books:
        filter_queries.append(u"book_title:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in books])))
    if composers:
        filter_queries.append(u"composer:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in composers])))
    if contributors:
        filter_queries.append(u"contributor:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in contributors])))
    if final_tone:
        filter_queries.append(u"cadence_final_tone:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in final_tone])))
    if cadence_kind:
        filter_queries.append(u"cadence_kind:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in cadence_kind])))
    if cadence_alter:
        filter_queries.append(u"cadence_alter:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in cadence_alter])))
    if text_tone:
        filter_queries.append(u"text_treatment:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in text_tone])))
    if repeat_kinds:
        filter_queries.append(u"repeat_kind:({0})".format(u" OR ".join([u"\"{0}\"".format(x) for x in repeat_kinds])))

    ret = s.select(qstring, fq=filter_queries)

    res = [SolrResponseObject(**s) for s in ret]

    data = {
        'query': qstring,
        'results': res
    }

    return render(request, 'search/results.html', data)


class SolrResponseObject(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)
