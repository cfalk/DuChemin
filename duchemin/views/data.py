from django.http import HttpResponse
from django.conf import settings

import httplib2
from duchemin.models.analysis import DCAnalysis
from duchemin.models.phrase import DCPhrase

# These methods are wrapped here to allow for cross-site
# calls without running in to the browser same-origin policies.
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

def phrase(request, piece_id, phrase_id):
    phrase = DCPhrase.objects.get(phrase_id=phrase_id)
    location = "{0}_XML/{1}.xml".format(piece_id[0:4], piece_id)
    start_meas = phrase.phrase_start
    end_meas = phrase.phrase_stop

    req_url = "{0}/{1}/{2}/{3}".format(settings.VEXF_SERVER, location, start_meas, end_meas)
    h = httplib2.Http()
    resp, content = h.request(req_url, "GET")
    return HttpResponse(content)

