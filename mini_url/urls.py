__author__ = 'PHUONG'

from django.conf.urls import patterns, url

urlpatterns = patterns('mini_url.views',
                       url(r'^$', 'liste', name='url_liste'),
                       url(r'^nouveau$', 'nouveau', name='url_nouveau'),
                       url(r'^(?P<code>\w{6})/$', 'redirection', name='url_redirection'),
                       )