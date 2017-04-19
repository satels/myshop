from sms.helpers import post_json, ExternalError
from sms.base import BaseSMSHandler, SMSHandlerError


class SMSHandler(BaseSMSHandler):

    handler_name = 'smscru'

    def send_message(self, phone, message):
        '''
        Doc
        '''
        conf = self.get_conf()

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
