from django.db import models

NOUN = ('nou', "noun")
PRONOUN = ('pro', "pronoun")
ADJECTIVE = ('adj', "adjective")
VERB = ('ver', "verb")
ADVERB = ('adv', "adverb")
PARTICLE = ('par', "particle")
NAME = ('nam', "name")

VERB_U = ('u', "u")
VERB_RU = ('r', "ru")
VERB_EXCEPTION = ('e', "ex")
JP_VERB_TYPES = (VERB_U, VERB_RU, VERB_EXCEPTION)

ADJ_I = ('i', "i")
ADJ_NA = ('na', "na")
JP_ADJ_TYPES = (ADJ_I, ADJ_NA)

class PosBase(models.Model):
    vocab = models.CharField(max_length=16)
    phonetic = models.CharField(max_length=32, null=True)
    english = models.CharField(max_length=32, null=True)
    category = models.CharField(max_length=32, null=True)

    class Meta:
        abstract = True

class Noun(PosBase):
    def __str__(self):
        return "[noun] {} ({})".format(self.vocab, self.english)

class Verb(PosBase):
    jp_type = models.CharField(max_length=2, choices=JP_VERB_TYPES, default=JP_VERB_TYPES[0])

    def __str__(self):
        return "[verb] {} ({})".format(self.vocab, self.english)

class Adjective(PosBase):
    jp_type = models.CharField(max_length=2, choices=JP_ADJ_TYPES, default=JP_ADJ_TYPES[0])

    def __str__(self):
        return "[adjective] {} ({})".format(self.vocab, self.english)

class Adverb(PosBase):
    def __str__(self):
        return "[adverb] {} ({})".format(self.vocab, self.english)

class Misc(PosBase):
    def __str__(self):
        return "[misc] {} ({})".format(self.vocab, self.english)
