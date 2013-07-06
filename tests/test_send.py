

from unittest import TestCase
from mandrill_mock import MandrillMock

class SendTest(TestCase):
    def test__null_key(self):
        api_key = None
        m = MandrillMock(api_key)
        self.assertTrue(m is not None)

    def test__send(self):
        m = MandrillMock()
        to_email = 'test@test.com'
        response = m.messages.send(message=
                                  {
                                    'text': 'some message',
                                    'subject': 'some subject',
                                    'from_email': 'from@test.com',
                                    'from_name': 'from name',
                                    'to': [{'email':to_email}]
                                  }
                                )
        self.assertTrue(len(response) > 0)
        self.assertTrue(response[0]['email'] == to_email)
        self.assertTrue(response[0]['status'] == 'mocked')


