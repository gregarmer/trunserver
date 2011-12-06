Twisted / Django runserver replacement
======================================

.. contents::

Overview
--------

This package is a simple replacement for the built-in Django runserver command
that uses the far more polished and multiple process capable Twisted Web
server. It currently handles the same autoreload-after-save provided by the
built-in Django runserver command.


Install
-------

The installation is relatively simple::

   pip install trunserver

   or

   easy_install trunserver

Once installed, simply add "trunserv" to your INSTALLED_APPS and use
"trunserver" wherever you would normally use "runserver". You can pass
"--noreload" to trunserver as a parameter to stop the autoreload behavior.
