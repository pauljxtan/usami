from django.conf.urls import url
from django.contrib import admin

import usami.views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', usami.views.home, name='home'),

    # Retrieve data

    url(r'^jp/nouns/rows/', usami.views.get_noun_rows_jp),
    url(r'^jp/nouns/modals/', usami.views.get_noun_modals_jp),
    url(r'^jp/verbs/rows/', usami.views.get_verb_rows_jp),
    url(r'^jp/verbs/modals/', usami.views.get_verb_modals_jp),
    url(r'^jp/adjectives/rows/', usami.views.get_adjective_rows_jp),
    url(r'^jp/adjectives/modals/', usami.views.get_adjective_modals_jp),
    url(r'^jp/adverbs/rows/', usami.views.get_adverb_rows_jp),
    url(r'^jp/adverbs/modals/', usami.views.get_adverb_modals_jp),
    url(r'^jp/miscs/rows/', usami.views.get_misc_rows_jp),
    url(r'^jp/miscs/modals/', usami.views.get_misc_modals_jp),
    url(r'^totals/', usami.views.get_totals),

    # Add vocab

    url(r'^jp/noun/add/', usami.views.add_noun_jp, name='add_noun_jp'),
    url(r'^jp/verb/add/', usami.views.add_verb_jp, name='add_verb_jp'),
    url(r'^jp/adjective/add/', usami.views.add_adjective_jp, name='add_adjective_jp'),
    url(r'^jp/adverb/add/', usami.views.add_adverb_jp, name='add_adverb_jp'),
    url(r'^jp/misc/add/', usami.views.add_misc_jp, name='add_misc_jp'),

    # Edit vocab

    url(r'^noun/edit/(?P<noun_id>[0-9]+)/', usami.views.edit_noun, name='edit_noun'),
    url(r'^verb/edit/(?P<verb_id>[0-9]+)/', usami.views.edit_verb, name='edit_verb'),
    url(r'^adjective/edit/(?P<adjective_id>[0-9]+)/', usami.views.edit_adjective, name='edit_adjective'),
    url(r'^adverb/edit/(?P<adverb_id>[0-9]+)/', usami.views.edit_adverb, name='edit_adverb'),
    url(r'^misc/edit/(?P<misc_id>[0-9]+)/', usami.views.edit_misc, name='edit_misc'),

    # Delete vocab

    url(r'^noun/delete/(?P<noun_id>[0-9]+)/', usami.views.delete_noun, name='delete_noun'),
    url(r'^verb/delete/(?P<verb_id>[0-9]+)/', usami.views.delete_verb, name='delete_verb'),
    url(r'^adjective/delete/(?P<adjective_id>[0-9]+)/', usami.views.delete_adjective, name='delete_adjective'),
    url(r'^adverb/delete/(?P<adverb_id>[0-9]+)/', usami.views.delete_adverb, name='delete_adverb'),
    url(r'^misc/delete/(?P<misc_id>[0-9]+)/', usami.views.delete_misc, name='delete_misc'),

    # Archive vocab

    url(r'^noun/archive/(?P<noun_id>[0-9]+)/', usami.views.archive_noun, name='archive_noun'),
    url(r'^verb/archive/(?P<verb_id>[0-9]+)/', usami.views.archive_verb, name='archive_verb'),
    url(r'^adjective/archive/(?P<adjective_id>[0-9]+)/', usami.views.archive_adjective, name='archive_adjective'),
    url(r'^adverb/archive/(?P<adverb_id>[0-9]+)/', usami.views.archive_adverb, name='archive_adverb'),
    url(r'^misc/archive/(?P<misc_id>[0-9]+)/', usami.views.archive_misc, name='archive_misc'),

    url(r'^noun/unarchive/(?P<noun_id>[0-9]+)/', usami.views.unarchive_noun, name='unarchive_noun'),
    url(r'^verb/unarchive/(?P<verb_id>[0-9]+)/', usami.views.unarchive_verb, name='unarchive_verb'),
    url(r'^adjective/unarchive/(?P<adjective_id>[0-9]+)/', usami.views.unarchive_adjective, name='unarchive_adjective'),
    url(r'^adverb/unarchive/(?P<adverb_id>[0-9]+)/', usami.views.unarchive_adverb, name='unarchive_adverb'),
    url(r'^misc/unarchive/(?P<misc_id>[0-9]+)/', usami.views.unarchive_misc, name='unarchive_misc'),
]
