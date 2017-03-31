import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
# from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

from usami.forms import NounForm, VerbForm, AdjectiveForm, AdverbForm, MiscForm
from usami.models import Noun, Verb, Adjective, Adverb, Misc

# TODO:
# -- Handle invalid input(s)

# Single-page application model:
#   This should be the only view that actually renders HTML content.
#   All other "views" either provide data for display or perform database operations.
def home(request):
    return _render_home(request)

######## RETRIEVE DATA ########################################################

# NOUNS

def get_noun_rows_jp(request):
    rows = []
    nouns = _get_all_nouns()
    for noun in nouns:
        row = {
            'vocab': _get_ruby(noun, "・"),
            'english': noun.english,
            'category': noun.category,
            'buttons': """
            <a class="btn btn-primary" data-toggle="modal" data-target="#noun-form-{0}">Edit</a>
            <a class="btn btn-danger" onclick="deleteNoun({0})">Delete</a>
            <a class="btn btn-success" onclick="archiveNoun({0})">Archive</a>
            """.format(noun.id)
        }
        rows.append(row)
    return HttpResponse(json.dumps(rows))

def get_noun_modals_jp(request):
    html = ""
    nouns = _get_all_nouns()
    for noun in nouns:
        html += """
        <div class="modal fade" id="noun-form-{3}" tabindex="-1" role="dialog" aria-labelledby="noun-form-label-{3}">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="noun-form-label-{3}">Edit {0}</h4>
              </div>
              <div class="modal-body">
                <div class="form-group">
                  <label for="noun-edit-vocab-{3}">Vocab:</label>
                  <input class="form-control" id="noun-edit-vocab-{3}" maxlength="16" name="vocab" type="text" required="" value="{4}">
                </div>
                <div class="form-group">
                  <label for="noun-edit-phonetic-{3}">Phonetic:</label>
                  <input class="form-control" id="noun-edit-phonetic-{3}" maxlength="32" name="phonetic" type="text" required="" value="{5}">
                </div>
                <div class="form-group">
                  <label for="noun-edit-english-{3}">English:</label>
                  <input class="form-control" id="noun-edit-english-{3}" maxlength="32" name="english" type="text" required="" value="{1}">
                </div>
                <div class="form-group">
                  <label for="noun-edit-category-{3}">Category:</label>
                  <input class="form-control" id="noun-edit-category-{3}" maxlength="32" name="category" type="text" required="" value="{2}">
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                 <button type="submit" class="btn btn-primary">Save changes</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        """.format(_get_ruby(noun, "・"), noun.english, noun.category, noun.id, noun.vocab, noun.phonetic)
    return HttpResponse(html)

# VERBS

def get_verb_rows_jp(request):
    rows = []
    verbs = _get_all_verbs()
    for verb in verbs:
        row = {
            'vocab': _get_ruby(verb, "・"),
            'english': verb.english,
            'category': verb.category,
            'transitivity': verb.transitivity,
            'jp_type': verb.jp_type,
            'buttons': """
            <a class="btn btn-primary" data-toggle="modal" data-target="#verb-form-{0}">Edit</a>
            <a class="btn btn-danger" onclick="deleteVerb({0})">Delete</a>
            <a class="btn btn-success" onclick="archiveVerb({0})">Archive</a>
            """.format(verb.id)
        }
        rows.append(row)
    return HttpResponse(json.dumps(rows))

def get_verb_modals_jp(request):
    html = ""
    verbs = _get_all_verbs()
    for verb in verbs:
        html += """
        <div class="modal fade" id="verb-form-{3}" tabindex="-1" role="dialog" aria-labelledby="verb-form-label-{3}">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="verb-form-label-{3}">Edit {0}</h4>
              </div>
              <div class="modal-body">
                <div class="form-group">
                  <label for="verb-edit-vocab-{3}">Vocab:</label>
                  <input class="form-control" id="verb-edit-vocab-{3}" maxlength="16" type="text" value="{4}">
                </div>
                <div class="form-group">
                  <label for="verb-edit-phonetic-{3}">Phonetic:</label>
                  <input class="form-control" id="verb-edit-phonetic-{3}" maxlength="32" type="text" value="{5}">
                </div>
                <div class="form-group">
                  <label for="verb-edit-english-{3}">English:</label>
                  <input class="form-control" id="verb-edit-english-{3}" maxlength="32" type="text" value="{1}">
                </div>
                <div class="form-group">
                  <label for="verb-edit-category-{3}">Category:</label>
                  <input class="form-control" id="verb-edit-category-{3}" maxlength="32" type="text" value="{2}">
                </div>
                <div class="form-group">
                  <label for="verb-edit-transitivity-{3}">Transitivity:</label>
                  <select class="form-control" id="verb-edit-transitivity-{3}" value="{6}">
                    <option value="t">t</option>
                    <option value="i">i</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="verb-edit-jp-type-{3}">Type:</label>
                  <select class="form-control" id="verb-edit-jp-type-{3}" value="{7}">
                    <option value="u">u</option>
                    <option value="r">ru</option>
                    <option value="e">ex</option>
                  </select>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                  <button type="submit" class="btn btn-primary">Save changes</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        """.format(_get_ruby(verb, "・"), verb.english, verb.category, verb.id, verb.vocab, verb.phonetic, verb.transitivity, verb.jp_type)
    return HttpResponse(html)

def get_totals(request):
    totals = {
        'total_nouns': len(_get_all_nouns()),
        'total_verbs': len(_get_all_verbs()),
        'total_adjectives': len(_get_all_adjectives()),
        'total_adverbs': len(_get_all_adverbs()),
        'total_miscs': len(_get_all_miscs()),

        'total_nouns_archived': len(_get_all_nouns(archived=True)),
        'total_verbs_archived': len(_get_all_verbs(archived=True)),
        'total_adjectives_archived': len(_get_all_adjectives(archived=True)),
        'total_adverbs_archived': len(_get_all_adverbs(archived=True)),
        'total_miscs_archived': len(_get_all_miscs(archived=True)),
    }
    return HttpResponse(json.dumps(totals))

######## GET VOCAB ############################################################

def _get_all_nouns(archived=False):      return Noun.objects.filter(archived=archived)
def _get_all_verbs(archived=False):      return Verb.objects.filter(archived=archived)
def _get_all_adjectives(archived=False): return Adjective.objects.filter(archived=archived)
def _get_all_adverbs(archived=False):    return Adverb.objects.filter(archived=archived)
def _get_all_miscs(archived=False):      return Misc.objects.filter(archived=archived)

######## ADD VOCAB ############################################################

@csrf_exempt
def add_noun_jp(request):
    return _add_noun(request, 'jp')

@csrf_exempt
def add_verb_jp(request):
    return _add_verb(request, 'jp')

@csrf_exempt
def add_adjective_jp(request):
    return _add_adjective(request, 'jp')

@csrf_exempt
def add_adverb_jp(request):
    return _add_adverb(request, 'jp')

@csrf_exempt
def add_misc_jp(request):
    return _add_misc(request, 'jp')

def _add_noun(request, lang):
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
            data = {'message': {'text': "Added: {}".format(noun_added), 'level': 'success'}}
        else:
            data = {'message': {'text': "Could not add noun", 'level': 'error'}}
    else:
        data = {'message': {'text': "Request was not POST", 'level': 'error'}}
    return HttpResponse(json.dumps(data))

def _add_verb(request, lang):
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
            data = {'message': {'text': "Added: {}".format(verb_added), 'level': 'success'}}
        else:
            data = {'message': {'text': "Could not add verb", 'level': 'error'}}
    else:
        data = {'message': {'text': "Request was not POST", 'level': 'error'}}
    return HttpResponse(json.dumps(data))

def _add_adjective(request, lang):
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
            data = {'message': {'text': "Added: {}".format(adjective_added), 'level': 'success'}}
        else:
            data = {'message': {'text': "Could not add adjective", 'level': 'error'}}
    else:
        data = {'message': {'text': "Request was not POST", 'level': 'error'}}
    return HttpResponse(json.dumps(data))

def _add_adverb(request, lang):
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
            data = {'message': {'text': "Added: {}".format(adverb_added), 'level': 'success'}}
        else:
            data = {'message': {'text': "Could not add adverb", 'level': 'error'}}
    else:
        data = {'message': {'text': "Request was not POST", 'level': 'error'}}
    return HttpResponse(json.dumps(data))

def _add_misc(request, lang):
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
            data = {'message': {'text': "Added: {}".format(misc_added), 'level': 'success'}}
        else:
            data = {'message': {'text': "Could not add misc", 'level': 'error'}}
    else:
        data = {'message': {'text': "Request was not POST", 'level': 'error'}}
    return HttpResponse(json.dumps(data))

######## EDIT VOCAB ###########################################################

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

######## DELETE VOCAB #########################################################

@csrf_exempt
def delete_noun(request, noun_id):
    noun = Noun.objects.filter(id=noun_id)
    noun_deleted = noun.first()
    noun.delete()
    data = {'message': {'text': "Deleted: {}".format(noun_deleted), 'level': 'warning'}}
    return HttpResponse(json.dumps(data))

@csrf_exempt
def delete_verb(request, verb_id):
    verb = Verb.objects.filter(id=verb_id)
    verb_deleted = verb.first()
    verb.delete()
    data = {'message': {'text': "Deleted: {}".format(verb_deleted), 'level': 'warning'}}
    return HttpResponse(json.dumps(data))

@csrf_exempt
def delete_adjective(request, adjective_id):
    adjective = Adjective.objects.filter(id=adjective_id)
    adjective_deleted = adjective.first()
    adjective.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(adjective_deleted))
    return _render_home(request, 'adjectives')

@csrf_exempt
def delete_adverb(request, adverb_id):
    adverb = Adverb.objects.filter(id=adverb_id)
    adverb_deleted = adverb.first()
    adverb.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(adverb_deleted))
    return _render_home(request, 'adverbs')

@csrf_exempt
def delete_misc(request, misc_id):
    misc = Misc.objects.filter(id=misc_id)
    misc_deleted = misc.first()
    misc.delete()
    messages.add_message(request, messages.WARNING, "Deleted: {}".format(misc_deleted))
    return _render_home(request, 'miscs')

######## ARCHIVE VOCAB ########################################################

@csrf_exempt
def archive_noun(request, noun_id):
    noun_archived = Noun.objects.filter(id=noun_id).first()
    noun_archived.archived = True
    noun_archived.save()
    data = {
        'message': {
            'text': "Archived: {}".format(noun_archived),
            'level': 'info',
        }
    }
    return HttpResponse(json.dumps(data))

@csrf_exempt
def unarchive_noun(request, noun_id):
    noun_unarchived = Noun.objects.filter(id=noun_id).first()
    noun_unarchived.archived = False
    messages.add_message(request, messages.INFO, "Unarchived: {}".format(noun_unarchived))
    return _render_home(request, 'nouns')

@csrf_exempt
def archive_verb(request, verb_id):
    verb_archived = Verb.objects.filter(id=verb_id).first()
    verb_archived.archived = True
    verb_archived.save()
    data = {'message': {'text': "Archived: {}".format(verb_archived), 'level': 'info'}}
    return HttpResponse(json.dumps(data))

@csrf_exempt
def unarchive_verb(request, verb_id):
    verb_unarchived = Verb.objects.filter(id=verb_id).first()
    verb_unarchived.archived = False
    messages.add_message(request, messages.INFO, "Unarchived: {}".format(verb_unarchived))
    return _render_home(request, 'nouns')

######## STATISTICS ###########################################################

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

######## HELPER FUNCTIONS #####################################################

def _get_ruby(vocab, phonetic_split_str):
    phonetic_split = vocab.phonetic.split(phonetic_split_str)
    ruby = ""
    if len(phonetic_split) == len(vocab.vocab):
        for i, v in enumerate(vocab.vocab):
            ruby += "<ruby>{}<rp>(</rp><rt>{}</rt><rp>)</rp></ruby>".format(v, phonetic_split [i])
    return ruby

# TODO: Deprecate
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

# TODO: Deprecate
def _get_all_nouns_with_ruby(phonetic_split_str, archived=False):
    nouns = _get_all_nouns(archived)
    return _get_vocabs_with_ruby(nouns, phonetic_split_str)

# TODO: Deprecate
def _get_all_verbs_with_ruby(phonetic_split_str, archived=False):
    verbs = _get_all_verbs(archived)
    return _get_vocabs_with_ruby(verbs, phonetic_split_str)

# TODO: Deprecate
def _get_all_adjectives_with_ruby(phonetic_split_str, archived=False):
    adjectives = _get_all_adjectives(archived)
    return _get_vocabs_with_ruby(adjectives, phonetic_split_str)

# TODO: Deprecate
def _get_all_adverbs_with_ruby(phonetic_split_str, archived=False):
    adverbs = _get_all_adverbs(archived)
    return _get_vocabs_with_ruby(adverbs, phonetic_split_str)

# TODO: Deprecate
def _get_all_miscs_with_ruby(phonetic_split_str, archived=False):
    miscs = _get_all_miscs(archived)
    return _get_vocabs_with_ruby(miscs, phonetic_split_str)

# TODO: Deprecate
def _get_vocabs_with_ruby(vocabs, phonetic_split_str, archived=False):
    vocabs_with_ruby = []
    for vocab in vocabs:
        vocabs_with_ruby.append((vocab, _get_ruby(vocab, phonetic_split_str)))
    return vocabs_with_ruby
