from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = []

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls))
    )

    urlpatterns += patterns('duchemin.views.main',
        url(r'^$', 'home', name='home'),
        url(r'^piece/(?P<piece_id>[0-9a-zA-Z]+)/add-observation/$', 'add_observation'),
        url(r'^piece/(?P<piece_id>[0-9a-zA-Z]+)', 'piece'),
        url(r'^pieces/$', 'pieces'),

        url(r'^book/(?P<book_id>[0-9]+)', 'book'),
        url(r'^books/$', 'books'),

        url(r'^profile/', 'profile'),

        url(r'^reconstructions/$', 'reconstructions'),
        url(r'^reconstruction/(?P<reconstruction_id>[0-9]+)', 'reconstruction'),

        url(r'^people/$', 'people'),
        url(r'^person/(?P<person_id>[a-zA-Z0-9]+)', 'person')
    )

    urlpatterns += patterns('duchemin.views.search',
        url(r'^search/$', 'search', name="search")
    )

    urlpatterns += patterns('duchemin.views.data',
        url(r'^data/analysis/(?P<anid>[0-9]+)', 'analysis'),
        url(r'^data/phrase/(?P<piece_id>[a-zA-Z0-9_]+)/(?P<phrase_id>[0-9]+)', 'phrase'),
    )

    urlpatterns += patterns('duchemin.views.callbacks',
        url(r'^search/results/(?P<restype>[0-9a-zA-Z]+)/$', 'result_callback'),
        url(r'^favourite/(?P<ftype>[a-zA-Z]+)/(?P<fid>[a-zA-Z0-9]+)/$', 'favourite_callback'),
        url(r'^discussion/$', 'discussion_callback'),
    )

    urlpatterns += patterns('',
        url(r'^login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/profile'}}),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    )

    urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^about/$', 'flatpage', {'url': '/about/'}, name="about")
    )

# urlpatterns = patterns('',
#     # Examples:
#     url(r'^$', 'duchemin.views.home', name='home'),
#     # url(r'^duchemin/', include('duchemin.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )
