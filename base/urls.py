from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('blog.views',
    (r'^blog/', include('blog.urls'), "main"),
)

