from contracts import contract
import importlib


@contract
def get_handler(path, conf=None):
    '''
    :type path: str
    :type conf: dict|None
    :rtype: SMSHandler
    '''

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
