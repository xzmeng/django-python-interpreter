#!/usr/bin/env python

from setuptools import setup, find_packages
from webshell import __version__

DESCRIPTION = "Django application for running python code in your project's environment from django admin."

setup(
    name='django-python-interpreter',
    version=__version__,
    description=DESCRIPTION,
    author='Meng Xiangzhuo',
    author_email='15195891330@163.com',
    url='https://github.com/xzmeng/django-python-interpreter',
    download_url='https://github.com/xzmeng/django-python-interpreter/tarball/master',
    license='MIT',
    packages=find_packages(),
    package_data={'webshell': [
        'templates/webshell/*',
        'static/css/*',
        'static/js/*',
    ]},
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
