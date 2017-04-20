from sms.helpers import ExternalError
from sms.handlers.base import SMSHandlerError
from django.test import TestCase
from djsms.core import send_message
from unittest.mock import patch



class MainTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.patch_external()
        self.phone = '+79687298907'
        self.message = 'Hello, World!'

    def patch_external(self):
        post_json_patcher = patch('sms.handlers.smscru.post_json')
        self.m_post_json = post_json_patcher.start()

    def tearDown(self):
        patch.stopall()

    @patch('djsms.core.settings.SMS_HANDLER', 'sms.handlers.smscru.SMSHandler')
    def test_smscru(self):

        self.m_post_json.return_value = {}

        with self.assertRaises(SMSHandlerError) as cm:
            send_message(self.phone, self.message, fail_silently=False)
        self.assertEquals(str(cm.exception), 'No valid data')

        ret = send_message(self.phone, self.message, fail_silently=True)
        self.assertFalse(ret)

        self.m_post_json.return_value = {'status': 'error'}

        with self.assertRaises(SMSHandlerError) as cm:
            send_message(self.phone, self.message, fail_silently=False)
        self.assertEquals(str(cm.exception), 'Bad status for send: {\'status\': \'error\'}')

        self.m_post_json.return_value = {'status': 'ok'}
        ret = send_message(self.phone, self.message, fail_silently=False)
        self.assertTrue(ret)
        ret = send_message(self.phone, self.message, fail_silently=True)
        self.assertTrue(ret)

        self.m_post_json.side_effect = ExternalError('Timeout Error (504)')
        with self.assertRaises(SMSHandlerError) as cm:
            send_message(self.phone, self.message, fail_silently=False)
        self.assertEquals(str(cm.exception), 'Timeout Error (504)')

    @patch('djsms.core.settings')
    def test_settings(self, settings_mock):
        settings_mock.SMS_HANDLER = 'sms.handlers.smscru.SMSHandler'
        settings_mock.SMS_SMSCRU_CONF = {}
        del settings_mock.SMS_SMSCRU_CONF
        with self.assertRaises(AttributeError) as cm:
            send_message(self.phone, self.message, fail_silently=False)
        self.assertEquals(str(cm.exception), 'Set SMS_SMSCRU_CONF in django settings')
