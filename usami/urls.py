from django.conf.urls import url
from django.contrib import admin

import usami.views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', usami.views.home, name='home'),
    url(r'^noun/add/', usami.views.add_noun, name='add_noun'),
    url(r'^verb/add/', usami.views.add_verb, name='add_verb'),
    url(r'^adjective/add/', usami.views.add_adjective, name='add_adjective'),
    url(r'^adverb/add/', usami.views.add_adverb, name='add_adverb'),
    url(r'^misc/add/', usami.views.add_misc, name='add_misc'),
    url(r'^noun/delete/(?P<noun_id>[0-9]+)/', usami.views.delete_noun, name='delete_noun'),
    url(r'^verb/delete/(?P<verb_id>[0-9]+)/', usami.views.delete_verb, name='delete_verb'),
    url(r'^adjective/delete/(?P<adjective_id>[0-9]+)/', usami.views.delete_adjective, name='delete_adjective'),
    url(r'^adverb/delete/(?P<adverb_id>[0-9]+)/', usami.views.delete_adverb, name='delete_adverb'),
    url(r'^misc/delete/(?P<misc_id>[0-9]+)/', usami.views.delete_misc, name='delete_misc'),
]
