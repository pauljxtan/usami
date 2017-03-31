import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from usami.forms import NounForm, VerbForm, AdjectiveForm, AdverbForm, MiscForm
from usami.models import Noun, Verb, Adjective, Adverb, Misc
from usami.serialization import get_serializable_noun

def home(request):
    return _render_home(request)

def get_all_nouns_jp(request):
    nouns = _get_all_nouns_with_ruby("・")
    data = json.dumps([(get_serializable_noun(noun[0]), noun[1]) for noun in nouns])
    print(data)
    return HttpResponse(data)#, content_type="application/json")

def get_noun_tab_jp(request):
    html = ""
    nouns = _get_all_nouns_with_ruby("・")
    for noun in nouns:
        id = noun[0].id
        vocab = noun[0].vocab
        english = noun[0].english
        category = noun[0].category
        ruby = noun[1]

        html += """
        <tr class="vocab-row">
        <td class="vocab vocab-vocab">{}</td>
        <td class="vocab vocab-english">{}</td>
        <td class="vocab vocab-category">{}</td>
        <td class="vocab vocab-buttons">
        <a class="btn btn-primary" data-toggle="modal" data-target="#noun-form-{}">Edit</a>
        <a class="btn btn-danger" href="/noun/delete/{}/">Delete</a>
        <a class="btn btn-success" href="/noun/archive/{}/">Archive</a>
        </td>
        </tr>
        """.format(ruby, english, category, id, id, id)
# <div class="modal fade" id="noun-form-{{ noun.0.id }}" tabindex="-1" role="dialog"
# aria-labelledby="noun-form-label-{{ noun.0.id }}">
# <div class="modal-dialog" role="document">
# <div class="modal-content">
# <div class="modal-header">
# <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
# <h4 class="modal-title" id="noun-form-label-{{ noun.0.id }}">Edit {{ noun.1 | safe }}</h4>
# </div>
# <div class="modal-body">
# <form class="form-inline" action="{% url 'edit_noun' noun.0.id %}" method="post">
# {% csrf_token %}
# <div class="form-group">
# <label for="id_vocab">Vocab:</label>
# <input class="form-control" id="id_vocab" maxlength="16" name="vocab" type="text" required=""
# value="{{ noun.0.vocab }}">
# </div>
# <div class="form-group">
# <label for="id_phonetic">Phonetic:</label>
# <input class="form-control" id="id_phonetic" maxlength="32" name="phonetic" type="text" required=""
# value="{{ noun.0.phonetic }}">
# </div>
# <div class="form-group">
# <label for="id_english">English:</label>
# <input class="form-control" id="id_english" maxlength="32" name="english" type="text" required=""
# value="{{ noun.0.english }}">
# </div>
# <div class="form-group">
# <label for="id_category">Category:</label>
# <input class="form-control" id="id_category" maxlength="32" name="category" type="text" required=""
# value="{{ noun.0.category }}">
# </div>
# <div class="modal-footer">
# <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
# <button type="submit" class="btn btn-primary">Save changes</button>
# </div>
# </form>
# </div>
# </div>
# </div>
# </div>
#
# {% endfor %}

    return HttpResponse(html)


def add_noun_jp(request):      return _add_noun(request, 'jp')
def add_verb_jp(request):      return _add_verb(request, 'jp')
def add_adjective_jp(request): return _add_adjective(request, 'jp')
def add_adverb_jp(request):    return _add_adverb(request, 'jp')
def add_misc_jp(request):      return _add_misc(request, 'jp')

def edit_noun(request, noun_id):
    active_lang = None
    if request.method == 'POST':
        form = NounForm(request.POST)
        if form.is_valid():
            noun_edited = Noun.objects.filter(id=noun_id).first()
            noun_edited.vocab    = form.cleaned_data.get('vocab', "")
            noun_edited.phonetic = form.cleaned_data.get('phonetic', "")
            noun_edited.english  = form.cleaned_data.get('english', "")
            noun_edited.category = form.cleaned_data.get('category', "")
            noun_edited.save()
            active_lang = noun_edited.lang
            messages.add_message(request, messages.INFO, "Edited: {}".format(noun_edited))
    if active_lang:
        return _render_home(request, 'nouns', active_lang)
    return _render_home(request, 'nouns')

def edit_verb(request, verb_id):
    active_lang = None
    if request.method == 'POST':
        form = VerbForm(request.POST)
        if form.is_valid():
            verb_edited = Verb.objects.filter(id=verb_id).first()
            verb_edited.vocab        = form.cleaned_data.get('vocab', "")
            verb_edited.phonetic     = form.cleaned_data.get('phonetic', "")
            verb_edited.english      = form.cleaned_data.get('english', "")
            verb_edited.category     = form.cleaned_data.get('category', "")
            verb_edited.transitivity = form.cleaned_data.get('transitivity', "")
            verb_edited.jp_type      = form.cleaned_data.get('jp_type', "")
            verb_edited.save()
            active_lang = verb_edited.lang
            messages.add_message(request, messages.INFO, "Edited: {}".format(verb_edited))
    if active_lang:
        return _render_home(request, 'verbs', active_lang)
    return _render_home(request, 'verbs')

def edit_adjective(request, adjective_id):
    active_lang = None
    if request.method == 'POST':
        form = AdjectiveForm(request.POST)
        if form.is_valid():
            adjective_edited = Adjective.objects.filter(id=adjective_id).first()
            adjective_edited.vocab    = form.cleaned_data.get('vocab', "")
            adjective_edited.phonetic = form.cleaned_data.get('phonetic', "")
            adjective_edited.english  = form.cleaned_data.get('english', "")
            adjective_edited.category = form.cleaned_data.get('category', "")
            adjective_edited.jp_type  = form.cleaned_data.get('jp_type', "")
            adjective_edited.save()
            active_lang = adjective_edited.lang
            messages.add_message(request, messages.INFO, "Edited: {}".format(adjective_edited))
    if active_lang:
        return _render_home(request, 'adjectives', active_lang)
    return _render_home(request, 'adjectives')

def edit_adverb(request, adverb_id):
    active_lang = None
    if request.method == 'POST':
        form = AdverbForm(request.POST)
        if form.is_valid():
            adverb_edited = Adverb.objects.filter(id=adverb_id).first()
            adverb_edited.vocab=form.cleaned_data.get('vocab', "")
            adverb_edited.phonetic=form.cleaned_data.get('phonetic', "")
            adverb_edited.english=form.cleaned_data.get('english', "")
            adverb_edited.category=form.cleaned_data.get('category', "")
            adverb_edited.save()
            active_lang = adverb_edited.lang
            messages.add_message(request, messages.INFO, "Edited: {}".format(adverb_edited))
    if active_lang:
        return _render_home(request, 'adverbs', active_lang)
    return _render_home(request, 'adverbs')

def edit_misc(request, misc_id):
    active_lang = None
    if request.method == 'POST':
        form = MiscForm(request.POST)
        if form.is_valid():
            misc_edited = Misc.objects.filter(id=misc_id).first()
            misc_edited.vocab=form.cleaned_data.get('vocab', "")
            misc_edited.phonetic=form.cleaned_data.get('phonetic', "")
            misc_edited.english=form.cleaned_data.get('english', "")
            misc_edited.category=form.cleaned_data.get('category', "")
            misc_edited.save()
            active_lang = misc_edited.lang
            messages.add_message(request, messages.INFO, "Edited: {}".format(misc_edited))
    if active_lang:
        return _render_home(request, 'miscs', active_lang)
    return _render_home(request, 'miscs')

def delete_noun(request, noun_id):
    noun = Noun.objects.filter(id=noun_id)
    noun_deleted = noun.first()
    noun.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(noun_deleted))
    return _render_home(request, 'nouns')

def delete_verb(request, verb_id):
    verb = Verb.objects.filter(id=verb_id)
    verb_deleted = verb.first()
    verb.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(verb_deleted))
    return _render_home(request, 'verbs')

def delete_adjective(request, adjective_id):
    adjective = Adjective.objects.filter(id=adjective_id)
    adjective_deleted = adjective.first()
    adjective.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(adjective_deleted))
    return _render_home(request, 'adjectives')

def delete_adverb(request, adverb_id):
    adverb = Adverb.objects.filter(id=adverb_id)
    adverb_deleted = adverb.first()
    adverb.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(adverb_deleted))
    return _render_home(request, 'adverbs')

def delete_misc(request, misc_id):
    misc = Misc.objects.filter(id=misc_id)
    misc_deleted = misc.first()
    misc.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(misc_deleted))
    return _render_home(request, 'miscs')

def archive_noun(request, noun_id):
    noun_archived = Noun.objects.filter(id=noun_id).first()
    noun_archived.archived = True
    noun_archived.save()
    messages.add_message(request, messages.INFO, "Archived: {}".format(noun_archived))
    return _render_home(request, 'nouns')

def unarchive_noun(request, noun_id):
    noun_unarchived = Noun.objects.filter(id=noun_id).first()
    noun_unarchived.archived = False
    messages.add_message(request, messages.INFO, "Unarchived: {}".format(noun_unarchived))
    return _render_home(request, 'nouns')

def _render_home(request, active_pos=None, active_lang='jp'):
    return render(
        request,
        'usami/home.html',
        {
            'nouns': _get_all_nouns_with_ruby("・"),
            'verbs': _get_all_verbs_with_ruby("・"),
            'adjectives': _get_all_adjectives_with_ruby("・"),
            'adverbs': _get_all_adverbs_with_ruby("・"),
            'miscs': _get_all_miscs_with_ruby("・"),

            'nouns_archived': _get_all_nouns_with_ruby("・", archived=True),
            'verbs_archived': _get_all_verbs_with_ruby("・", archived=True),
            'adjectives_archived': _get_all_adjectives_with_ruby("・", archived=True),
            'adverbs_archived': _get_all_adverbs_with_ruby("・", archived=True),
            'miscs_archived': _get_all_miscs_with_ruby("・", archived=True),

            'active_pos': active_pos,
            'active_lang': active_lang,

            'total_nouns': len(_get_all_nouns()),
            'total_verbs': len(_get_all_verbs()),
            'total_adjectives': len(_get_all_adjectives()),
            'total_adverbs': len(_get_all_adverbs()),
            'total_miscs': len(_get_all_miscs()),

            'noun_stats': _get_noun_stats(),
            'verb_stats': _get_verb_stats(),
            'adjective_stats': _get_adjective_stats(),
            'adverb_stats': _get_adverb_stats(),
            'misc_stats': _get_misc_stats(),
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
            messages.add_message(request, messages.SUCCESS, "Added: {}".format(noun_added))
        else:
            # TODO: Display message indicating invalid form
            pass
    return _render_home(request, 'nouns', lang)

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
            messages.add_message(request, messages.SUCCESS, "Added: {}".format(verb_added))
    return _render_home(request, 'verbs', lang)

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
            messages.add_message(request, messages.SUCCESS, "Added: {}".format(adjective_added))
    return _render_home(request, 'adjectives', lang)

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
            messages.add_message(request, messages.SUCCESS, "Added: {}".format(adverb_added))
    return _render_home(request, 'adverbs', lang)

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
            messages.add_message(request, messages.SUCCESS, "Added: {}".format(misc_added))
    return _render_home(request, 'miscs', lang)

def _get_all_nouns(archived=False):      return Noun.objects.filter(archived=archived)
def _get_all_verbs(archived=False):      return Verb.objects.filter(archived=archived)
def _get_all_adjectives(archived=False): return Adjective.objects.filter(archived=archived)
def _get_all_adverbs(archived=False):    return Adverb.objects.filter(archived=archived)
def _get_all_miscs(archived=False):      return Misc.objects.filter(archived=archived)

def _get_all_nouns_with_ruby(phonetic_split_str, archived=False):
    nouns = _get_all_nouns(archived)
    return _get_vocabs_with_ruby(nouns, phonetic_split_str)

def _get_all_verbs_with_ruby(phonetic_split_str, archived=False):
    verbs = _get_all_verbs(archived)
    return _get_vocabs_with_ruby(verbs, phonetic_split_str)

def _get_all_adjectives_with_ruby(phonetic_split_str, archived=False):
    adjectives = _get_all_adjectives(archived)
    return _get_vocabs_with_ruby(adjectives, phonetic_split_str)

def _get_all_adverbs_with_ruby(phonetic_split_str, archived=False):
    adverbs = _get_all_adverbs(archived)
    return _get_vocabs_with_ruby(adverbs, phonetic_split_str)

def _get_all_miscs_with_ruby(phonetic_split_str, archived=False):
    miscs = _get_all_miscs(archived)
    return _get_vocabs_with_ruby(miscs, phonetic_split_str)

def _get_vocabs_with_ruby(vocabs, phonetic_split_str, archived=False):
    vocabs_with_ruby = []
    for vocab in vocabs:
        phonetic_split = vocab.phonetic.split(phonetic_split_str)
        vocab_ruby = ""
        if len(phonetic_split) == len(vocab.vocab):
            for i, v in enumerate(vocab.vocab):
                vocab_ruby += "<ruby>{}<rp>(</rp><rt>{}</rt><rp>)</rp></ruby>".format(v, phonetic_split [i])
        vocabs_with_ruby.append((vocab, vocab_ruby))
    return vocabs_with_ruby

def _get_noun_stats():
    nouns = _get_all_nouns()
    return _get_vocab_stats(nouns)

def _get_verb_stats():
    verbs = _get_all_verbs()
    return _get_vocab_stats(verbs)

def _get_adjective_stats():
    adjectives = _get_all_adjectives()
    return _get_vocab_stats(adjectives)

def _get_adverb_stats():
    adverbs = _get_all_adverbs()
    return _get_vocab_stats(adverbs)

def _get_misc_stats():
    miscs = _get_all_miscs()
    return _get_vocab_stats(miscs)

def _get_vocab_stats(vocabs):
    stats = {}
    stats['category_counts'] = _get_category_counts(vocabs)
    return stats

def _get_category_counts(vocabs, ordered_by_count=True):
    categories_all = [vocab.category for vocab in vocabs]
    categories_unique = sorted(set(categories_all))
    category_counts = []
    for category in categories_unique:
        category_counts.append((category, categories_all.count(category)))

    if ordered_by_count:
        category_counts = sorted(category_counts, key=lambda x: -x[1])

    return category_counts
