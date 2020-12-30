Django Crypto Trading Bot
=========================

Auto crypto trading bot for various exchanges.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
.. image:: https://travis-ci.com/linuxluigi/django-crypto-trading-bot.svg?branch=master
     :target: https://travis-ci.com/linuxluigi/django-crypto-trading-bot
     :alt: Travis CI tests
.. image:: https://readthedocs.org/projects/django-crypto-trading-bot/badge/?version=latest
     :target: https://django-crypto-trading-bot.readthedocs.io/en/latest/?badge=latest
     :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/linuxluigi/django-crypto-trading-bot/badge.svg?branch=master
     :target: https://coveralls.io/github/linuxluigi/django-crypto-trading-bot?branch=master
     :alt: Coverage
.. image:: https://api.codacy.com/project/badge/Grade/c6bd668a8e61448b86a15fdb2648cd38?isInternal=true
     :target: https://www.codacy.com/manual/linuxluigi/django-crypto-trading-bot?utm_source=github.com&utm_medium=referral&utm_content=linuxluigi/django-crypto-trading-bot&utm_campaign=Badge_Grade_Dashboard
     :alt: Codacy quality
.. image:: https://static.deepsource.io/deepsource-badge-light.svg
     :target: https://deepsource.io/gh/linuxluigi/django-crypto-trading-bot/?ref=repository-badge
     :alt: DeepSource


:License: MIT
Rewrite in progress
=========================

The current state of the project is very experimental and there is a complete rewrite_ in progress. Soon it will be possible to create a trading strategy through a django app.

.. _rewrite: https://github.com/linuxluigi/django-crypto-trading-bot/tree/v0.2

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy django_crypto_trading_bot

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



