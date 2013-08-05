mandrill-mock
=============


A python lib to wrap the mandrill api in dev and test environments

Implementation::
    
    import os

    #get your api key from the environment
    _MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')

    if _MANDRILL_API_KEY is not None:
        from mandrill import Mandrill
        mandrill_client = Mandrill(_MANDRILL_API_KEY)
    else:
        from mandrill_mock import MandrillMock
        mandrill_client = MandrillMock()

    #call like normal
    response = mandrill_client.messages.send(message=
                                  {
                                    'text': 'some message',
                                    'subject': 'some subject',
                                    'from_email': 'from@test.com',
                                    'from_name': 'from name',
                                    'to': [{'email':to_email}]
                                  }
                                )

To use in your python project::

    pip install -e git://github.com/texuf/mandrill-mock.git#egg=mandrill-mock

To download, setup and perfom tests, run the following commands on Mac / Linux::

    get clone <repo>
    cd <reponame>
    virtualenv venv --distribute
    source venv/bin/activate
    pip install nose
    python setup.py install
    nosetests
