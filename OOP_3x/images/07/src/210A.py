class Options:
    default_options = {
    'port': 22,
    'host':'localhost',
    'usrname': 'Homer',
    'password': 'theSimpsons',
    'debug': True,
    }

    def __init__(self, **karwgs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]
