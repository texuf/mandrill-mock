from mandrill import Mandrill, ROOT
import os, logging

class MandrillMock(Mandrill):
    def __init__(self, apikey=None, debug=True): #default debug to true
        if apikey is None:
            apikey = ''
        Mandrill.__init__(self, apikey, debug)
        
        if os.environ.get('ENVIRONMENT') == 'test':
            self.level = logging.DEBUG
        else:
            self.level = logging.INFO


    def call(self, url, params=None):
        '''skip the api call so tests don\'t fire emails'''
        
        self.log('NO MANDRILL API KEY, would have sent:\nPOST to %s%s.json: %s' % (ROOT, url, params))

        if 'message' in params and 'to' in params['message']:
            result = []
            for email in params['message']['to']:
                result.append({u'email': email['email'], u'_id': u'', u'status': u'mocked'})
            return result
        else:
            return {}


    def __repr__(self):
        return object.__repr__(self) 

