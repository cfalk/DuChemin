from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.conf import settings
from django.core.paginator import EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from duchemin.helpers.solrsearch import DCSolrSearch

from duchemin.models.piece import DCPiece
from duchemin.models.analysis import DCAnalysis
from duchemin.models.reconstruction import DCReconstruction


class JsonResponse(HttpResponse):
    def __init__(self, content, mimetype='application/json', status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=simplejson.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type
        )


@login_required
def favourite_callback(request, ftype, fid):
    action = None
    if 'remove' in request.GET.keys():
        action = 'remove'
    else:
        action = 'add'

    user_profile = request.user.get_profile()

    success = False
    if ftype == 'piece':
        if action == 'remove':
            piece = DCPiece.objects.get(pk=fid)
            user_profile.favourited_piece.remove(piece)
            success = True
        else:
            # favourite a piece
            piece = DCPiece.objects.get(pk=fid)
            user_profile.favourited_piece.add(piece)
            success = True

    elif ftype == 'analysis':
        if action == 'remove':
            an = DCAnalysis.objects.get(pk=fid)
            user_profile.favourited_analysis.remove(an)
            success = True
        else:
            # favourite an analysis
            an = DCAnalysis.objects.get(pk=fid)
            user_profile.favourited_analysis.add(an)
            success = True

    elif ftype == 'reconstruction':
        if action == 'remove':
            recon = DCReconstruction.objects.get(pk=fid)
            user_profile.favourited_reconstruction.remove(recon)
            success = True
        else:
            recon = DCReconstruction.objects.get(pk=fid)
            user_profile.favourited_reconstruction.add(recon)
            success = True
    else:
        pass

    data = {
        'success': success
    }
    return JsonResponse(data)


def result_callback(request, restype):
    if restype == 'work':
        return _fetch_work_results(request)
    elif restype == 'element':
        return _fetch_element_results(request)
    elif restype == 'facet':
        return _fetch_facet_results(request)


def _fetch_work_results(request):
    s = DCSolrSearch(request)
    work_res = s.group_search(['title'], fq=['type:(duchemin_analysis OR duchemin_piece)'])

    if work_res.count == 0:
        return render(request, 'search/no_results.html')

    try:
        wpage = int(request.GET.get('wpage', '1'))
    except ValueError:
        wpage = 1

    try:
        work_results = work_res.page(wpage)
    except (EmptyPage, InvalidPage):
        work_results = work_res.page(work_res.num_pages)
    work_results.pager_id = 'works'

    data = {
        'work_results': work_results
    }
    return render(request, 'search/work_result_list.html', data)


def _fetch_element_results(request):
    s = DCSolrSearch(request)
    el_res = s.search(fq=['type:duchemin_analysis'])

    if el_res.count == 0:
        return render(request, 'search/no_results.html')

    try:
        epage = int(request.GET.get('epage', '1'))
    except ValueError:
        epage = 1

    try:
        element_results = el_res.page(epage)
    except (EmptyPage, InvalidPage):
        element_results = el_res.page(el_res.num_pages)
    element_results.pager_id = 'elements'

    data = {
        'element_results': element_results
    }
    return render(request, 'search/element_result_list.html', data)


def _fetch_facet_results(request):
    s = DCSolrSearch(request)
    facet_params = {
        'facet': 'true',
        'facet_field': settings.SOLR_FACET_FIELDS,
        'facet_mincount': 1,
    }
    facet_res = s.search(fq=['type:duchemin_analysis'], **facet_params)
    facets = facet_res.result.facet_counts['facet_fields']
    filtered_facets = dict([(k, v) for k, v in facets.iteritems() if k in settings.DISPLAY_FACETS])
    data = {
        'facet_results': filtered_facets.iteritems()
    }
    return render(request, 'search/facets.html', data)
