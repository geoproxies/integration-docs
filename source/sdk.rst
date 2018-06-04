The Geoproxies SDK for Python, JavaScript and TypeScript
========================================================

Making use of Geoproxies might be a new learning curve for some developer. For this reason, Geoproxies provides helper modules in various languages, that encapsulates its Proxy parameters, in a programmable and intuitive way for use in scrapping frameworks or any other project.


Python SDK tutorial
-------------------

* Requirements and installation *

The SDK requires atleast the python 2.7 version or beyond.

To install using pip::

   pip install geoproxies



Node.Js SDK Tutorial
--------------------

* Requirements and installation *

To install using npm::

  npm install geoproxies




Using Geoproxies SDK with Scrappy
---------------------------------



API references for Python and Node.Js
-------------------------------------

The API classes and methods are same on both the Python and Node.Js platform, with the exception of language norm code style.

.. automodule:: geoproxies
.. autoclass:: ProxySettings
   :members:


Using SDK
---------

* Simplest Request

A valid ProxySettings is created by initializing the ProxySettings Class with the customer token value.

	>>> from geoproxies import ProxySettings
	>>> proxysettings = ProxySettings('24f2f5b3-1867-42ac-994c-57140022fb46')

*This is all it takes to make a request with Geoproxies*


* Tracking a Request

The *tracking_id* is how every request is expected to be identified. The request data can be collected after a completed request via the Geoproxies API.

	>>> proxysettings.set_tracking_id('any id works')

*or* even better generate a new tracking id for every request with the method

	>>> proxysettings.new_tracking_id()

.. note:: It is required to provide this value when request information or wiretap data is to be retrieved afterwards.

* Sessions and Session Groups

Using session allows for the use/re-use of the same IP address. **Think of a session as associated with an IP address**.

.. note:: The inclusion of the *country* or *session_group* option makes up for a different IP. A logical way to think of this will be, A session is made up of the provided session_id and country and session_group.

Session Group as the name suggest, is to allow for the grouping of sessions.
This is particularly useful when using the same set of session over different requirements. Here the different requirement would represent a different *session_group* name.

.. note:: The *fail_on_duplicate_ip* in conjunction with *session_group* instructs the Proxy to fail when Geoproxies is unable to dispatch a unique IP address in the batch of IP(s) associated with the Session Group.

* Making a Wiretap Request

    >>> proxysettings.set_wiretap(True)

Provides the feature of recording the data transferred up and down for various reasons, most notably for debugging.

* Using the output

	>>> print(str(proxysettings))
	>>> http://24f2f5b3-1867-42ac-994c-57140022fb46:wiretap=True@proxy.geoproxies.com:1080
