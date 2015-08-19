__author__ = 'PHUONG'

#tao url cho app blog

from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
                       url(r'^accueil$', 'home'),
                       # xem 1 article precis: vi du: article/42
                       url(r'^article/(?P<id_article>\d+)$', 'view_article'),

                       )

