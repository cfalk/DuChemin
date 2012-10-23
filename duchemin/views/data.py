from django.http import HttpResponse
from django.conf import settings

import httplib2
from duchemin.models.analysis import DCAnalysis


def analysis(request, anid):
    analysis = DCAnalysis.objects.get(id=anid)
    compnum = analysis.composition_number.piece_id
    location = "{0}_XML/{1}.xml".format(compnum[0:4], compnum)
    start_meas = analysis.start_measure
    end_meas = analysis.stop_measure

    req_url = "{0}/{1}/{2}/{3}".format(settings.VEXF_SERVER, location, start_meas, end_meas)

    h = httplib2.Http()
    resp, content = h.request(req_url, "GET")

    return HttpResponse(content)
