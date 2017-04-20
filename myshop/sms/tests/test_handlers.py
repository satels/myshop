from sms.api import get_handler
from sms.helpers import ExternalError
from sms.handlers.base import BaseSMSHandler, SMSHandlerError
from unittest.mock import patch
import unittest


class MainTest(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.patch_external()
        self.phone = '+79687298907'
        self.message = 'Hello, World!'

    def patch_external(self):
        post_json_patcher = patch('sms.handlers.smscru.post_json')
        self.m_post_json = post_json_patcher.start()
        self.m_post_json.return_value = {'status': 'ok'}

    def tearDown(self):
        patch.stopall()

    def test_dummy(self):
        conf = {'foo': 'bar'}
        handler = get_handler('sms.handlers.dummy.SMSHandler', conf=conf)
        ret = handler.send_message(self.phone, self.message)
        self.assertEquals(ret, {'status': 'ok', 'data': {'phone': self.phone, 'conf': conf}})

    def test_base(self):
        handler = BaseSMSHandler()
        with self.assertRaises(NotImplementedError) as cm:
            handler.send_message(self.phone, self.message)
        self.assertEquals(str(cm.exception), 'Please, make the impliment with specific sms handler')

    def test_smscru(self):
        handler = get_handler('sms.handlers.smscru.SMSHandler')

        with self.assertRaises(SMSHandlerError) as cm:
            handler.send_message(self.phone, self.message)
        self.assertEquals(str(cm.exception), 'Specify username and password')

        handler = get_handler('sms.handlers.smscru.SMSHandler', conf={'username': 'foo', 'password': 'bar'})
        ret = handler.send_message(self.phone, self.message)
        self.assertEquals(ret, {'data': {'status': 'ok'}, 'status': 'ok'})

    def test_update_conf(self):
        handler = get_handler('sms.handlers.dummy.SMSHandler')
        self.assertTrue(handler.conf is None)
        handler.update_conf({'test': 'dummy'})
        self.assertEquals(handler.conf, {'test': 'dummy'})
        handler.update_conf({'foo': 'bar'})
        self.assertEquals(handler.conf, {'test': 'dummy', 'foo': 'bar'})

    @patch('sms.handlers.dummy.SMSHandler.handler_name', None)
    def test_handler_name_empty(self):

        handler = get_handler('sms.handlers.dummy.SMSHandler')
        handler.update_conf({'test': 'dummy'})

        with self.assertRaises(NotImplementedError) as cm:
            handler.send_message(self.phone, self.message)
        self.assertEquals(str(cm.exception), 'Set handler name')

    def test_get_conf(self):
        handler = get_handler('sms.handlers.dummy.SMSHandler', conf={'initial': 'foobar'})
        handler.handler_name = 'dummy'
        handler.update_conf({'test': 'dummy'})

        self.assertEquals(handler.get_conf(), {'test': 'dummy', 'initial': 'foobar'})

    def test_get_handler(self):
        with self.assertRaises(NotImplementedError) as cm:
            get_handler('sms.handlers.dnotfound.SMSHandler')
        self.assertEquals(str(cm.exception), 'Error importing sms handler module sms.handlers.dnotfound: "No module named \'sms.handlers.dnotfound\'"')

        with self.assertRaises(NotImplementedError) as cm:
            get_handler('sms.handlers.dummy.DNotFoundHandler')
        self.assertEquals(str(cm.exception), 'Module "sms.handlers.dummy" does not define a "DNotFoundHandler" class')
