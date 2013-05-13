from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swancreekpress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('main.urls')),
    url(r'^Books/', include('books.urls')),
    url(r'^Author/', include('author.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url' : '/static/img/favicon.ico'}),
)
