from django.conf import settings
from duchemin.helpers.solrpaginate import SolrPaginator, SolrGroupedPaginator
import solr


class DCSolrSearch(object):
    """
        active_query = {
            'q': {
                'q': ['amour']/['*:*'],
                'cadence': ['foo:bar', '(foo:A or foo:B)'],
                'intpatt': ['(foo:A OR foo:B)'],
                'prestype': ['(prestype:"NIM" AND x:A AND y:b)', '(prestype:"ID" AND x:A AND y:b)']
                ...
                }
            'group': ...,
            'fq': ...
        }

        " OR ".join(active_query['q']['prestype'])
        " OR ".join([active_query['q']['cadence'], active_query['q']['intpatt']])

    """
    def __init__(self, **kwargs):
        self.server = solr.Solr(settings.SOLR_SERVER)
        self.group_q = False
        self._initialize()

    def search(self, request, fetch_num=False, **kwargs):
        # returns a paginator object for the search results.
        self.qdict = request.GET
        self._initialize()
        self._map_query(request)
        # print self.active_query
        # treat group & filter
        extra_params = {}
        if 'group' in kwargs.keys():
            self.group_q = True
            extra_params['group'] = 'true'
            extra_params['group_ngroups'] = 'true'
            extra_params['group_field'] = ",".join(kwargs['group']).strip(",")
        if 'filter' in kwargs.keys():
            extra_params['fq'] = ",".join(kwargs['filter']).strip(",")

        results = self.server.select(self.qstring, **extra_params)

        if self.group_q:
            return SolrGroupedPaginator(results)
        else:
            return SolrPaginator(results)

    def num_results(self, request, **kwargs):
        return self.search(request, fetch_num=True, **kwargs)

    def _initialize(self):
        self.active_query = {}
        self.active_query['q'] = {}
        self.group = False
        self.filter = False

    def _map_query(self, request):
        # if self.qdict.get('q') != "":
        #     self.active_query['q']['q'] = u"{0}".format(self.qdict.get('q'))
        # else:
        #     self.active_query['q']['q'] = u"*:*"
        self._q_book()
        self._q_composer()
        self._q_cadence()
        self._q_intpatt()
        self._q_prestype()
        self._construct_querystring()

    def _construct_querystring(self):
        self.qstring = ""
        if self.qdict.get('q') != "":
            self.qstring = u"{0}".format(self.qdict.get('q'))
        else:
            self.qstring = u"*:*"

        for grp, q in self.active_query['q'].iteritems():
            if not q:
                continue
            self.qstring = u"{0} AND {1}".format(self.qstring, " AND ".join(q))

    def _q_composer(self):
        group = 'composer'
        self.active_query['q'][group] = []
        fields = ['p']
        self._prep_q(fields, group)

    def _q_book(self):
        group = 'book'
        self.active_query['q'][group] = []
        qfield = self.qdict.getlist('b')
        if qfield:
            q = " OR ".join(["{0}:{1}".format('book_id', q) for q in qfield])
            self.active_query['q'][group].append(q)
            # self._prep_q(fields, group)

    def _q_cadence(self):
        group = 'cadence'
        self.active_query['q'][group] = []
        # self.active_query['q'][group].append("is_cadence:true")
        fields = ['f', 'k', 'm', 'cadence_role_cantz', 'cadence_role_tenz']
        self._prep_q(fields, group)

    def _q_intpatt(self):
        group = 'intpatt'
        self.active_query['q'][group] = []
        fields = ['intpatt_p6_up', 'intpatt_p6_lo', 'intpatt_p3_up', 'intpatt_p3_lo',
                    'intpatt_53_up', 'intpatt_53_lo', 'intpatt_other']
        self._prep_q(fields, group)

    def _q_prestype(self):
        group = 'prestype'
        self.active_query['q'][group] = []
        fields = ['prestype_nim_up1', 'prestype_nim_lo1', 'prestype_nim_up2', 'prestype_nim_lo2',
                    'prestype_free_dux', 'prestype_free_comes', 'prestype_imduet_dux1', 'prestype_imduet_comes1',
                    'prestype_imduet_dux2', 'prestype_imduet_comes2', 'prestype_entry_p_dux1', 'prestype_entry_p_comes1',
                    'prestype_entry_p_dux2', 'prestype_entry_p_comes2', 'prestype_entry_t_dux1', 'prestype_entry_t_comes1',
                    'prestype_entry_t_dux2', 'prestype_entry_t_comes2', 'prestype_entry_s_dux1', 'prestype_entry_s_comes1',
                    'prestype_entry_s_dux2', 'prestype_entry_s_comes2']

        prestype = {}
        for field in fields:
            qfield = self.qdict.get(field)
            if not qfield:
                continue
            if 'None' in qfield:
                continue
            solr_field = settings.SEARCH_PARAM_MAP[field]

            if "_nim_" in field:
                # non imitative
                if 'nim' not in prestype.keys():
                    prestype['nim'] = []
                    prestype['nim'].append(u'other_pres_type:\"NIM\"')
                prestype['nim'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

            if "_free_" in field:
                if 'free' not in prestype.keys():
                    prestype['free'] = []
                    prestype['nim'].append(u'other_pres_type:\"FI\"')
                prestype['free'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

            if "_imduet_" in field:
                # imitative duet
                if 'imduet' not in prestype.keys():
                    prestype['imduet'] = []
                    prestype['imduet'].append(u'other_pres_type:\"ID\"')
                prestype['imduet'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

            if "_entry_p_" in field:
                # periodic entry
                if 'entry_p' not in prestype.keys():
                    prestype['entry_p'] = []
                    prestype['entry_p'].append(u'other_pres_type:\"PEn\"')
                prestype['entry_p'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

            if "_entry_t_" in field:
                # tonal entry
                if 'entry_t' not in prestype.keys():
                    prestype['entry_t'] = []
                    prestype['entry_t'].append(u'other_pres_type:\"PEn Tonal\"')
                prestype['entry_t'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

            if "_entry_s_" in field:
                # stacked entry
                if 'entry_s' not in prestype.keys():
                    prestype['entry_s'] = []
                    prestype['entry_s'].append(u'other_pres_type:\"PEn Stacked\"')
                prestype['entry_s'].append(u"{0}:\"{1}\"".format(solr_field, qfield))

        for pt, pt_query in prestype.iteritems():
            full_q = u" AND ".join(pt_query)
            full_q = u"{0}".format(full_q)
            self.active_query['q'][group].append(full_q)

        # self._prep_q(fields, group)

    def _prep_q(self, fields, group):
        for field in fields:
            qfield = self.qdict.getlist(field)
            if not qfield:
                continue
            if 'None' in qfield:
                continue
            solr_field = settings.SEARCH_PARAM_MAP[field]
            if len(qfield) > 1:
                res = u" AND ".join(["{0}:\"{1}\"".format(solr_field, f) for f in qfield])
                res = u"{0}".format(res)
            else:
                res = u"{0}:\"{1}\"".format(solr_field, qfield[0])
            self.active_query['q'][group].append(res)
