from django.shortcuts import render
from django.core.paginator import EmptyPage, InvalidPage
from duchemin.helpers.solrsearch import DCSolrSearch


def result_callback(request, restype):
    if restype == 'work':
        return _fetch_work_results(request)
    elif restype == 'element':
        return _fetch_element_results(request)


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
