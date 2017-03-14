from django import forms

from usami.models import Noun, Verb, Adjective, Adverb, Misc

POS_FIELDS = ('vocab', 'phonetic', 'english', 'category')

class NounForm(forms.ModelForm):
    class Meta:
        model = Noun
        fields = POS_FIELDS

class VerbForm(forms.ModelForm):
    class Meta:
        model = Verb
        fields = POS_FIELDS + ('transitivity', 'jp_type', )

class AdjectiveForm(forms.ModelForm):
    class Meta:
        model = Adjective
        fields = POS_FIELDS + ('jp_type', )

class AdverbForm(forms.ModelForm):
    class Meta:
        model = Adverb
        fields = POS_FIELDS

class MiscForm(forms.ModelForm):
    class Meta:
        model = Misc
        fields = POS_FIELDS


