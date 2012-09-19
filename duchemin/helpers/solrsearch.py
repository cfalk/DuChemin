from django.conf import settings
import solr


class DCSolrSearch(object):
    def __init__(self, **kwargs):
        self.server = solr.Solr(settings.SOLR_SERVER)
        self.param_map = settings.SEARCH_PARAM_MAP
        self.active_query = {}
        self.qstring = None
        self.group = False
        self.filter = False

    def search(self, request, **kwargs):
        if 'group' in kwargs.keys():
            # group = [groupfields]
            self.group = ",".join(kwargs['group']).strip(",")
        if 'filter' in kwargs.keys():
            # filter = [filterfields]
            self.filter = ",".join(kwargs['filter']).strip(",")

        self.map_query(request)
        results = self.server.select(self.qstring, **self.active_query)
        return results

    def __map_func(param):
        pass

    def map_query(self, request):
        """ Takes a search form request object and maps it to a Solr query """
        # self.qstring = request.GET.get('q', '')
        # if not self.qstring:
        #     self.qstring = "*:*"
        qdict = request.GET
        if 'q' in qdict.keys():
            self.qstring = qdict['q']
        else:
            self.qstring = "*:*"

        if self.group:
            self.active_query['group'] = "true"
            self.active_query['group_main'] = "true"
            self.active_query['group_field'] = self.group

        if self.filter:
            self.active_query['fq'] = self.filter

        for key, item in qdict.items():
            if item == "None":
                continue
            print key.strip(), ": ", item
