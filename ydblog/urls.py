from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ydblog.views.home', name='home'),
    # url(r'^ydblog/', include('ydblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'account.views.test'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^register/$', 'account.views.register'),
    url(r'^post','post.views.PostView'),
    url(r'^reg/$','account.views.register',name='test'),
    url(r'^regpost/$','post.views.PostView',name='test'),
    url(r'^index/$','post.views.index'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)
