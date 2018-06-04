.. _proxyoptions:

Proxy Parameter Reference
=========================


Parameter syntax
----------------

Geoproxies allows the combination of its parameters in any order.

Each option/argument must be separated with the pipe (``|``) character.
For example using the country and project parameter will look like this: ``country=fi|project=analytics423``.

The parameter names are case-insensitive.

IP address selection
--------------------


* **pool**: string

The pool parameter is use to select the preferred choice of IP pool. Defaults to ``pool=static``. It accepts just one of two values consisting; static or residential

* **country**: iso alpha-2 country code

Pass the country option to specify an IP from any one region of the world. Only the standard iso alpha-2 country code is recognized.

For example fr - France, nl - Neitherlands etc


* **preferIP**: IPV4 Address

This parameter is used to pass the preferred IPV4 address to serve a request with. Should the IP passed be unavailable, another IP address will be used.

.. note:: You can query for the IP used to serve a request with a call to getRequestData API. See :ref:`apis` for more information on using this API.



Sessions
--------

* **session**: string

This parameter allows the persistent use of any single IP address on Geoproxies. Similar to the preferIP option, but in a much extensive way. See the sessionGroupId and failOnDuplicateIp parameters for advanced combinations.


* **sessionGroupId**: string

The sessionGroupId allows for a unique way to categorize a batch of request, and most importantly to hint Geoproxies on serving distinct IP addresses when possible.

.. note:: This option requires the *session* parameter to be provided.

          In addition, see the failOnDuplicateIp option to enforce a failure in the case where Geoproxies is unable serve with a new IP address based on all the arguments specified.


* **failOnDuplicateIp**: mixed

The parameter to optionally fail when unique IP is not dispatched in the use of session and grouping.

.. note:: This requires the sessionGroupId and session parameters to be provided.

Ban management
--------------


* **targetId**: string

This is intended to be used to represent a body of requests to a destination. Synonymous to a domain.


Debugging
---------

* **wiretap**: void

A toggle parameter to capture the request and response between the proxy and the target destination.

.. note:: The use of this option, also requires the trackingId parameter to be provided.

* **trackingId**: string

User provided value to represent a request. It is generally suggested to used this parameter, when you need to extract information about the request at a later time via API calls.

Traffic control
---------------

* **blockAds**: void

The blockAds option enables the filtering away of hosts and domains that are known to be analytics, adverts, attach website among others. Please see the link  https://github.com/notracking/hosts-blocklists/ for a list of blocked urls.


Accounting
----------

* **project**: string

The project option is used for data grouping. Commonly used for grouping traffic usage statistically.
