
from mandrill import Mandrill


class MandrillMock(Mandrill):
    def __init__(self, apikey=None, debug=False):
        if apikey is None:
            apikey = ''
        Mandrill.__init__(self, apikey, debug)


    def call(self, url, params=None):
        '''skipp the api call!!! we don't want to send emails from the intern's computer right? '''
        result = []
        if 'message' in params and 'to' in params['message']:
            for email in params['message']['to']:
                result.append({u'email': email['email'], u'_id': u'', u'status': u'mocked'})
        return result




