from django.contrib import admin

from usami.models import Noun, Verb, Adjective, Adverb, Misc

POS_LIST_DISPLAY = ('vocab', 'phonetic', 'english', 'category')

class VocabAdmin(admin.ModelAdmin):
    list_display = ('type', 'kanji', 'furigana', 'english', 'category')

class NounAdmin(admin.ModelAdmin):
    list_display = POS_LIST_DISPLAY

class VerbAdmin(admin.ModelAdmin):
    list_display = POS_LIST_DISPLAY

class AdjectiveAdmin(admin.ModelAdmin):
    list_display = POS_LIST_DISPLAY

class AdverbAdmin(admin.ModelAdmin):
    list_display = POS_LIST_DISPLAY

class MiscAdmin(admin.ModelAdmin):
    list_display = POS_LIST_DISPLAY

admin.site.register(Noun, NounAdmin)
admin.site.register(Verb, VerbAdmin)
admin.site.register(Adjective, AdjectiveAdmin)
admin.site.register(Adverb, AdverbAdmin)
admin.site.register(Misc, MiscAdmin)
