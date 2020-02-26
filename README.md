Django-python-interpreter
=========================
[![Build Status](https://travis-ci.org/xzmeng/django-python-interpreter.svg?branch=master)](https://travis-ci.org/xzmeng/django-python-interpreter)
[![Coverage Status](https://coveralls.io/repos/github/xzmeng/django-python-interpreter/badge.svg?branch=master)](https://coveralls.io/github/xzmeng/django-python-interpreter)

Django application for running python code in your project's environment from django admin.

Installation
------------

    pip install django-python-interpreter

settings.py:
```python
INSTALLED_APPS = (
    ...
    'webshell',
    ...
)
```

urls.py:
```python
urlpatterns = patterns('',
    ...
    (r'^admin/webshell/', include('webshell.urls')),
    ...
)
```
![django-webshell](screenshot.png)
