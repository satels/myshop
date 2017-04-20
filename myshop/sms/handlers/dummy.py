from contracts import contract
from sms.helpers import post_json, ExternalError
from sms.base import BaseSMSHandler, SMSHandlerError


class SMSHandler(BaseSMSHandler):

    handler_name = 'dummy'

    @contract
    def send_message(self, phone, message):
        '''
        :type phone: str
        :type message: str
        :rtype: dict
        '''
        conf = self.get_conf()

        return {'status': 'ok', 'data': {'phone': phone, 'conf': conf}}
