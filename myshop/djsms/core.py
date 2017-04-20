from contracts import contract
from django.conf import settings
from sms.api import get_handler
from sms.handlers.base import SMSHandlerError
import logging


logger = logging.getLogger('djsms.send_message')


@contract
def send_message(phone, message, fail_silently=False):
    '''
    :type phone: str
    :type message: str
    :rtype: bool
    '''
    path = getattr(settings, 'SMS_HANDLER', 'sms.handlers.dummy.SMSHandler')

    handler = get_handler(path)
    handler_name = handler.handler_name

    conf_name = 'SMS_{}_CONF'.format(handler_name.upper())
    try:
        handler_conf = getattr(settings, conf_name)
    except AttributeError:
        raise AttributeError('Set {} in django settings'.format(conf_name))

    handler.update_conf(handler_conf)

    try:
        res = handler.send_message(phone, message)
    except SMSHandlerError as e:
        logger.error('{}:{}'.format(handler_name, repr(e)))
        if not fail_silently:
            raise e
        return False
    else:
        logger.info('{}:{}'.format(handler_name, repr(res['data'])))
        return True
