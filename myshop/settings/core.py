import os


def get_env_param_str(param_name, default_param_str=None, raise_exception=True):
    param_str = os.environ.get(param_name) or default_param_str
    if param_str is None and raise_exception:
        raise Exception(u'Incorrect env param: {}'.format(param_name))
    return param_str
