from django.conf.urls import patterns, include, url, static
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

        url(r'^piece/(?P<piece_id>[0-9a-zA-Z]+)', 'piece'),
        url(r'^pieces/$', 'pieces'),

        url(r'^book/(?P<book_id>[0-9]+)', 'book'),
        url(r'^books/$', 'books'),

        url(r'^profile/', 'profile')
    )

    urlpatterns += patterns('duchemin.views.search',
        url(r'^search/$', 'search', name="search"),
    )

    urlpatterns += patterns('duchemin.views.data',
        url(r'^data/analysis/(?P<anid>[0-9]+)', 'analysis')
    )

    urlpatterns += patterns('',
        url(r'^login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/profile'}}),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
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
