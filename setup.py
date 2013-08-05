import os
import platform
from setuptools import setup



install_requires = ['mandrill']
if platform.python_version() < '2.7':
    install_requires.append('unittest2')

setup(
      name='mandrill-mock',
      version='0.1',
      url='https://github.com/texuf/mandrill-mock',
      classifiers = [
          'Programming Language :: Python :: 2.7',
          ],
      description='Fake mandrill stub for testing simple mandrill dependent code',
      license='BSD',
      author='Austin Ellis',
      author_email='austinellis@gmail.com',
      py_modules=['mandrill_mock'],
      install_requires=install_requires,
      scripts=[],
      namespace_packages=[]
      )
