from sms.helpers import post_json, ExternalError
from sms.base import BaseSMSHandler, SMSHandlerError


class SMSHandler(BaseSMSHandler):

    handler_name = 'dummy'

    def send_message(self, phone, message):
        '''
        Doc
        '''
        conf = self.get_conf()

        return {'status': 'ok', 'data': {'phone': phone, 'conf': conf}}
