from django.conf import settings
from django.utils.html import urllib
from duchemin.helpers.solrpaginate import SolrPaginator, SolrGroupedPaginator
import solr

import pdb


CADENCE_FIELDS = ['f', 'k', 'm', 'cadence_role_cantz', 'cadence_role_tenz']

INTPATT_FIELDS = ['intpatt_p6_up', 'intpatt_p6_lo', 'intpatt_p3_up', 'intpatt_p3_lo',
                    'intpatt_53_up', 'intpatt_53_lo', 'intpatt_other']

PRESTYP_FIELDS = ['prestype_nim_up1', 'prestype_nim_lo1', 'prestype_nim_up2', 'prestype_nim_lo2',
                    'prestype_free_dux', 'prestype_free_comes', 'prestype_imduet_dux1', 'prestype_imduet_comes1',
                    'prestype_imduet_dux2', 'prestype_imduet_comes2', 'prestype_entry_p_dux1', 'prestype_entry_p_comes1',
                    'prestype_entry_p_dux2', 'prestype_entry_p_comes2', 'prestype_entry_t_dux1', 'prestype_entry_t_comes1',
                    'prestype_entry_t_dux2', 'prestype_entry_t_comes2', 'prestype_entry_s_dux1', 'prestype_entry_s_comes1',
                    'prestype_entry_s_dux2', 'prestype_entry_s_comes2']


def translate_voice_filter_to_solr(request):
    qdict = request.GET
    resdict = {}
    if 'prestype_perentry_s_voice_c1_un_oct' in qdict.keys():
        com1 = qdict.getlist('prestype_entry_s_comes1')
        com2 = qdict.getlist('prestype_entry_s_comes2')
        resdict['voice_role_un_oct'] = "({0} OR {1})".format(com1, com2)

    if 'prestype_perentry_s_voice_c1_fifth' in qdict.keys():
        pass

    if 'prestype_perentry_s_voice_c1_above' in qdict.keys():
        pass

    if 'prestype_perentry_s_voice_c1_below' in qdict.keys():
        pass

    if 'prestype_perentry_s_voice_d2_un_oct' in qdict.keys():
        pass
    if 'prestype_perentry_s_voice_d2_fifth' in qdict.keys():
        pass
    if 'prestype_perentry_s_voice_d2_above' in qdict.keys():
        pass
    if 'prestype_perentry_s_voice_d2_below' in qdict.keys():
        pass

    if 'prestype_perentry_s_opts_stretto' in qdict.keys():
        pass
    if 'prestype_perentry_s_opts_invertible' in qdict.keys():
        pass


class DCSolrSearch(object):
    def __init__(self, request):
        self.server = solr.Solr(settings.SOLR_SERVER)
        self.request = request
        self.parsed_request = {}
        self.prepared_query = u""
        self.solr_params = {}
        self._parse_request()
        self._prep_q()

    def search(self, **kwargs):
        self.solr_params.update(kwargs)
        res = self._do_query()
        return SolrPaginator(res)

    def facets(self, facet_fields=settings.SOLR_FACET_FIELDS, **kwargs):
        facet_params = {
            'facet': 'true',
            'facet_field': facet_fields,
        }
        self.solr_params.update(facet_params)
        self.solr_params.update(kwargs)

        res = self._do_query()
        return res

    def group_search(self, group_fields, **kwargs):
        group_params = {
            'group': 'true',
            'group_ngroups': 'true',
            'group_field': group_fields
        }
        self.solr_params.update(group_params)
        self.solr_params.update(kwargs)

        res = self._do_query()
        return SolrGroupedPaginator(res)

    def _do_query(self):
        return self.server.select(self.prepared_query, **self.solr_params)

    def _parse_request(self):
        qdict = self.request.GET
        for k, v in qdict.lists():
            if k not in settings.SEARCH_PARAM_MAP.keys():
                continue
            self.parsed_request[settings.SEARCH_PARAM_MAP[k]] = v
        # pdb.set_trace()

    def _prep_q(self):
        if self.parsed_request:
            arr = []
            for k, v in self.parsed_request.iteritems():
                arr.append(u"{0}:({1})".format(k, " OR ".join(["\"{0}\"".format(s) for s in v])))
            self.prepared_query = u" AND ".join(arr)
        else:
            self.prepared_query = u"*:*"
