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
        print self.active_query['q']
        results = self.server.select(**self.active_query)
        return results

    def __map_func(param):
        pass

    def map_query(self, request):
        """ Takes a search form request object and maps it to a Solr query

            CAD <-> INTPATT = AND
            INTPATT <-> TXTREAT = AND
            PRESTYPE <-> TXTREAT = AND
            CAD <-> TXTREAT = AND

        """
        # self.qstring = request.GET.get('q', '')
        # if not self.qstring:
        #     self.qstring = "*:*"
        qdict = request.GET
        if qdict.get('q') != "":
            self.active_query['q'] = u"{0}".format(qdict.get('q'))
        else:
            self.active_query['q'] = u"*:*"

        if self.group:
            self.active_query['group'] = "true"
            self.active_query['group_main'] = "true"
            self.active_query['group_field'] = self.group

        if self.filter:
            self.active_query['fq'] = self.filter

        # process cadences
        self.__q_cadence(qdict)
        # _intpatt = self.__q_intpatt(qdict)

        # for key, item in qdict.items():
        #     if item == "None":
        #         continue
        #     print key.strip(), ": ", item
    def __q_cadence(self, qdict):
        if 'f' in qdict.keys():
            solr_field = settings.SEARCH_PARAM_MAP['f']
            qstr = self._prep_q(solr_field, qdict.getlist('f'), "OR")
            self._add_q(qstr)

        if 'k' in qdict.keys():
            # cadence type
            solr_field = settings.SEARCH_PARAM_MAP['k']
            qstr = self._prep_q(solr_field, qdict.getlist('k'), "OR")
            self._add_q(qstr)

        if 'm' in qdict.keys():
            solr_field = settings.SEARCH_PARAM_MAP['m']
            qstr = self._prep_q(solr_field, qdict.getlist('m'), "OR")
            self._add_q(qstr)

        if 'None' not in qdict.get('cadence_role_cantz'):
            # cadence cantizans role
            solr_field = settings.SEARCH_PARAM_MAP['cadence_role_cantz']
            qstr = self._prep_q(solr_field, qdict.getlist('cadence_role_cantz'))
            self._add_q(qstr)

        if 'None' not in qdict.get('cadence_role_tenz'):
            # cadence tenorizans role
            solr_field = settings.SEARCH_PARAM_MAP['cadence_role_tenz']
            qstr = self._prep_q(solr_field, qdict.getlist('cadence_role_tenz'))
            self._add_q(qstr)

    def add_query(self, field, qdict, op="AND"):
        solr_field = settings.SEARCH_PARAM_MAP[field]
        self._add_q(self._prep_q(solr_field, qdict.getlist(field), op))

    def _prep_q(self, field, query, op="AND"):
        q = ""
        # print query
        if len(query) > 1:
            q = " {0} ".format(op).join(["{0}:\"{1}\"".format(field, q) for q in query])
            q = "({0})".format(q.strip())
        else:
            q = "{0}:\"{1}\"".format(field, query[0])
        return q

    def _add_q(self, query, op='AND'):
        self.active_query['q'] = "{0} {1} {2}".format(self.active_query['q'], op, query)
