from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    (r'^blog/', include('base.blog.urls'), "main"),
    # Examples:
    # url(r'^$', 'web_dja.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
)


