import importlib


def get_handler(path, conf=None):
    """
    Doc
    """

    try:
        mod_name, klass_name = path.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
    except AttributeError as e:
        raise NotImplementedError(
                'Error importing sms handler module %s: "%s"' % (mod_name, e))

    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise NotImplementedError(
                'Module "%s" does not define a "%s" '
                'class' % (mod_name, klass_name))

    return klass(conf=conf)
