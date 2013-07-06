mandrill-mock
=============

A python lib to wrap the mandrill api in dev and test environments

Implementation
 
 
To use in your python project
 pip install -e git://github.com/texuf/mandrill-mock.git#egg=mandrill-mock

To download, setup and perfom tests, run the following commands on Mac / Linux::

 get clone <repo>
 cd <reponame>
 virtualenv venv --distribute
 source venv/bin/activate
 pip install nose
 python setup.py install
 nosetests
