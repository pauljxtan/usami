from django.db import models

# Add more languages here...
JAPANESE = ('jp', "Japanese")
CHINESE = ('zh', "Chinese")
FRENCH = ('fr', "French")
LANGS = sorted((JAPANESE, CHINESE, FRENCH), key=lambda x: x[0])

# Maybe use "ichidan/godan" here
JP_VERB_U = ('u', "u")
JP_VERB_RU = ('r', "ru")
JP_VERB_EXCEPTION = ('e', "ex")
JP_VERB_TYPES = (JP_VERB_U, JP_VERB_RU, JP_VERB_EXCEPTION)

JP_ADJ_I = ('i', "i")
JP_ADJ_NA = ('na', "na")
JP_ADJ_TYPES = (JP_ADJ_I, JP_ADJ_NA)

VERB_TRANSITIVE = ('t', "transitive")
VERB_INTRANSITIVE = ('i', "intransitive")
VERB_TRANSITIVITY = (VERB_TRANSITIVE, VERB_INTRANSITIVE)

class PosBase(models.Model):
    lang = models.CharField(max_length=2, choices=LANGS, default=JAPANESE)
    vocab = models.CharField(max_length=32)
    phonetic = models.CharField(max_length=32, null=True)
    english = models.CharField(max_length=32, null=True)
    category = models.CharField(max_length=32, null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "[{}-{}] {} ({})".format(self.__class__.__name__, self.lang, self.vocab, self.english)

    class Meta:
        abstract = True

class Noun(PosBase):
    pass

class Verb(PosBase):
    jp_type = models.CharField(max_length=2, choices=JP_VERB_TYPES, default=JP_VERB_TYPES[0])
    transitivity = models.CharField(max_length=1, choices=VERB_TRANSITIVITY, default=VERB_TRANSITIVITY[0])

class Adjective(PosBase):
    jp_type = models.CharField(max_length=2, choices=JP_ADJ_TYPES, default=JP_ADJ_TYPES[0])

class Adverb(PosBase):
    pass

class Misc(PosBase):
    pass
