from mandrill import Mandrill, ROOT


class MandrillMock(Mandrill):
    def __init__(self, apikey=None, debug=True): #default debug to true
        if apikey is None:
            apikey = ''
        Mandrill.__init__(self, apikey, debug)


    def call(self, url, params=None):
        '''skipp the api call!!! we don't want to send emails from the intern's computer right? '''
        result = []

        self.log('NO MANDRILL API KEY, would have sent:\nPOST to %s%s.json: %s' % (ROOT, url, params))

        if 'message' in params and 'to' in params['message']:
            for email in params['message']['to']:
                result.append({u'email': email['email'], u'_id': u'', u'status': u'mocked'})
        return result


    def __repr__(self):
        return object.__repr__(self) 

