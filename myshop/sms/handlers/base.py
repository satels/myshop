from contracts import contract
from sms.conf import handler_confs


class SMSHandlerError(Exception):
    pass


class BaseSMSHandler(object):

    handler_name = None

    @contract
    def __init__(self, conf=None):
        '''
        :type conf: dict|None
        '''
        self.conf = conf

    @contract
    def update_conf(self, conf):
        '''
        :type conf: dict|None
        '''
        if self.conf is None:
            self.conf = conf
        else:
            self.conf.update(conf)

    @contract
    def get_conf(self):
        '''
        :rtype: dict
        '''
        if self.handler_name is None:
            raise NotImplementedError('Set handler name')
        if self.handler_name not in handler_confs:
            raise NotImplementedError(
                    'Set conf for {} handler (see sms.conf '
                    'module)'.format(self.handler_name))
        ret = handler_confs[self.handler_name]
        if self.conf is not None:
            ret = dict(ret, **self.conf)
        return ret

    def send_message(self, phone, message):
        raise NotImplementedError('Please, make the impliment with specific sms handler')
