def get_serializable_noun(noun):
    return {
        'lang': noun.lang,
        'vocab': noun.vocab,
        'phonetic': noun.phonetic,
        'english': noun.english,
        'category': noun.category,
        'archived': noun.archived,
    }
