from contracts import contract
from sms.helpers import post_json, ExternalError
from sms.handlers.base import BaseSMSHandler, SMSHandlerError


class SMSHandler(BaseSMSHandler):

    handler_name = 'smscru'

    @contract
    def send_message(self, phone, message):
        '''
        :type phone: str
        :type message: str
        :rtype: dict
        '''
        conf = self.get_conf()

        if 'username' not in conf or 'password' not in conf:
            raise SMSHandlerError('Specify username and password')

        try:
            res_data = post_json(conf['url'], {
                'login': conf['username'],
                'password': conf['password'],
                'message': message,
                'phone': phone,
            })
        except ExternalError as e:
            raise SMSHandlerError(e)

        if 'status' not in res_data:
            raise SMSHandlerError('No valid data')

        if res_data['status'] != 'ok':
            raise SMSHandlerError('Bad status for send: {}'.format(repr(res_data)))

        return {'status': 'ok', 'data': res_data}
