from django.shortcuts import render

from usami.forms import NounForm, VerbForm, AdjectiveForm, AdverbForm, MiscForm
from usami.models import Noun, Verb, Adjective, Adverb, Misc

def home(request):
    return _render_home(request)

def add_noun_jp(request):      return _add_noun(request, 'jp')
def add_verb_jp(request):      return _add_verb(request, 'jp')
def add_adjective_jp(request): return _add_adjective(request, 'jp')
def add_adverb_jp(request):    return _add_adverb(request, 'jp')
def add_misc_jp(request):      return _add_misc(request, 'jp')

def edit_noun(request, noun_id):
    noun_edited = None
    if request.method == 'POST':
        form = NounForm(request.POST)
        if form.is_valid():
            Noun.objects.filter(id=noun_id).update(
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
            noun_edited = Noun.objects.filter(id=noun_id).first()
    return _render_home(request, noun_edited=noun_edited)

def edit_verb(request, verb_id):
    verb_edited = None
    if request.method == 'POST':
        form = VerbForm(request.POST)
        if form.is_valid():
            Verb.objects.filter(id=verb_id).update(
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', ""),
                transitivity=form.cleaned_data.get('transitivity', ""),
                jp_type=form.cleaned_data.get('jp_type', "")
            )
            verb_edited = Verb.objects.filter(id=verb_id).first()
    return _render_home(request, verb_edited=verb_edited)

def edit_adjective(request, adjective_id):
    adjective_edited = None
    if request.method == 'POST':
        form = AdjectiveForm(request.POST)
        if form.is_valid():
            Adjective.objects.filter(id=adjective_id).update(
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', ""),
                jp_type=form.cleaned_data.get('jp_type', "")
            )
            adjective_edited = Adjective.objects.filter(id=adjective_id).first()
    return _render_home(request, adjective_edited=adjective_edited)

def edit_adverb(request, adverb_id):
    adverb_edited = None
    if request.method == 'POST':
        form = AdverbForm(request.POST)
        if form.is_valid():
            Adverb.objects.filter(id=adverb_id).update(
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
            adverb_edited = Adverb.objects.filter(id=adverb_id).first()
    return _render_home(request, adverb_edited=adverb_edited)

def edit_misc(request, misc_id):
    misc_edited = None
    if request.method == 'POST':
        form = MiscForm(request.POST)
        if form.is_valid():
            Misc.objects.filter(id=misc_id).update(
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
            misc_edited = Misc.objects.filter(id=misc_id).first()
    return _render_home(request, misc_edited=misc_edited)

def delete_noun(request, noun_id):
    noun = Noun.objects.filter(id=noun_id)
    noun_deleted = noun.first()
    noun.delete()
    return _render_home(request, noun_deleted=noun_deleted)

def delete_verb(request, verb_id):
    verb = Verb.objects.filter(id=verb_id)
    verb_deleted = verb.first()
    verb.delete()
    return _render_home(request, verb_deleted=verb_deleted)

def delete_adjective(request, adjective_id):
    adjective = Adjective.objects.filter(id=adjective_id)
    adjective_deleted = adjective.first()
    adjective.delete()
    return _render_home(request, adjective_deleted=adjective_deleted)

def delete_adverb(request, adverb_id):
    adverb = Adverb.objects.filter(id=adverb_id)
    adverb_deleted = adverb.first()
    adverb.delete()
    return _render_home(request, adverb_deleted=adverb_deleted)

def delete_misc(request, misc_id):
    misc = Misc.objects.filter(id=misc_id)
    misc_deleted = misc.first()
    misc.delete()
    return _render_home(request, misc_deleted=misc_deleted)

def _render_home(request,
                 noun_added=None, verb_added=None, adjective_added=None, adverb_added=None, misc_added=None,
                 noun_edited=None, verb_edited=None, adjective_edited=None, adverb_edited=None, misc_edited=None,
                 noun_deleted=None, verb_deleted=None, adjective_deleted=None, adverb_deleted=None, misc_deleted=None):
    return render(
        request,
        'usami/home.html',
        {
            'nouns': _get_all_nouns_with_ruby("・"),
            'verbs': _get_all_verbs_with_ruby("・"),
            'adjectives': _get_all_adjectives_with_ruby("・"),
            'adverbs': _get_all_adverbs_with_ruby("・"),
            'miscs': _get_all_miscs_with_ruby("・"),

            # 'form_noun': NounForm(),
            # 'form_verb': VerbForm(),
            # 'form_adjective': AdjectiveForm(),
            # 'form_adverb': AdverbForm(),
            # 'form_misc': MiscForm(),

            'noun_added': noun_added,
            'verb_added': verb_added,
            'adjective_added': adjective_added,
            'adverb_added': adverb_added,
            'misc_added': misc_added,

            'noun_edited': noun_edited,
            'verb_edited': verb_edited,
            'adjective_edited': adjective_edited,
            'adverb_edited': adverb_edited,
            'misc_edited': misc_edited,

            'noun_deleted': noun_deleted,
            'verb_deleted': verb_deleted,
            'adjective_deleted': adjective_deleted,
            'adverb_deleted': adverb_deleted,
            'misc_deleted': misc_deleted,

            'total_nouns': len(_get_all_nouns()),
            'total_verbs': len(_get_all_verbs()),
            'total_adjectives': len(_get_all_adjectives()),
            'total_adverbs': len(_get_all_adverbs()),
            'total_miscs': len(_get_all_miscs()),
        }
    )

def _add_noun(request, lang):
    noun_added = None
    if request.method == 'POST':
        form = NounForm(request.POST)
        if form.is_valid():
            noun_added = Noun.objects.create(
                lang=lang,
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
        else:
            # TODO: Display message indicating invalid form
            pass
    return _render_home(request, noun_added=noun_added)

def _add_verb(request, lang):
    verb_added = None
    if request.method == 'POST':
        form = VerbForm(request.POST)
        if form.is_valid():
            verb_added = Verb.objects.create(
                lang=lang,
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', ""),
                transitivity=form.cleaned_data.get('transitivity', ""),
                jp_type=form.cleaned_data.get('jp_type', "")
            )
    return _render_home(request, verb_added=verb_added)

def _add_adjective(request, lang):
    adjective_added = None
    if request.method == 'POST':
        form = AdjectiveForm(request.POST)
        if form.is_valid():
            adjective_added = Adjective.objects.create(
                lang=lang,
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', ""),
                jp_type=form.cleaned_data['jp_type']
            )
    return _render_home(request, adjective_added=adjective_added)

def _add_adverb(request, lang):
    adverb_added = None
    if request.method == 'POST':
        form = AdverbForm(request.POST)
        if form.is_valid():
            adverb_added = Adverb.objects.create(
                lang=lang,
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
    return _render_home(request, adverb_added=adverb_added)

def _add_misc(request, lang):
    misc_added = None
    if request.method == 'POST':
        form = MiscForm(request.POST)
        if form.is_valid():
            misc_added = Misc.objects.create(
                lang=lang,
                vocab=form.cleaned_data.get('vocab', ""),
                phonetic=form.cleaned_data.get('phonetic', ""),
                english=form.cleaned_data.get('english', ""),
                category=form.cleaned_data.get('category', "")
            )
    return _render_home(request, misc_added=misc_added)

def _get_all_nouns(): return Noun.objects.all()
def _get_all_verbs(): return Verb.objects.all()
def _get_all_adjectives(): return Adjective.objects.all()
def _get_all_adverbs(): return Adverb.objects.all()
def _get_all_miscs(): return Misc.objects.all()

def _get_all_nouns_with_ruby(phonetic_split_str):
    nouns = _get_all_nouns()
    return _get_vocabs_with_ruby(nouns, phonetic_split_str)

def _get_all_verbs_with_ruby(phonetic_split_str):
    verbs = _get_all_verbs()
    return _get_vocabs_with_ruby(verbs, phonetic_split_str)

def _get_all_adjectives_with_ruby(phonetic_split_str):
    adjectives = _get_all_adjectives()
    return _get_vocabs_with_ruby(adjectives, phonetic_split_str)

def _get_all_adverbs_with_ruby(phonetic_split_str):
    adverbs = _get_all_adverbs()
    return _get_vocabs_with_ruby(adverbs, phonetic_split_str)

def _get_all_miscs_with_ruby(phonetic_split_str):
    miscs = _get_all_miscs()
    return _get_vocabs_with_ruby(miscs, phonetic_split_str)

def _get_vocabs_with_ruby(vocabs, phonetic_split_str):
    vocabs_with_ruby = []
    for vocab in vocabs:
        phonetic_split = vocab.phonetic.split(phonetic_split_str)
        vocab_ruby = ""
        if len(phonetic_split) == len(vocab.vocab):
            for i, v in enumerate(vocab.vocab):
                vocab_ruby += "<ruby>{}<rp>(</rp><rt>{}</rt><rp>)</rp></ruby>".format(v, phonetic_split [i])
        vocabs_with_ruby.append((vocab, vocab_ruby))
    return vocabs_with_ruby
