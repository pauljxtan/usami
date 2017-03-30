from json import JSONEncoder

class NounEncoder(JSONEncoder):
    def __init__(self):
        JSONEncoder.__init__(self)

    # lang
    # vocab
    # phonetic
    # english
    # category
    # archived
