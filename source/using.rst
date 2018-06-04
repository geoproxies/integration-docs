Examples of Proxy Requests
==========================
The snippets in this section uses the basic authentication to connect to Geoproxies.

Curl
----
**curl** provides the capability to specify a proxy to connect through with the *-x* flag

.. code:: bash

 curl -x "http://24f2f5b3-1867-42ac-994c-57140022fb46:session=XYZ|wiretap@proxy.geoproxies.com:1080"\
 "http://httpbin.org/ip"

Python
------

* Using the *requests* library

.. code:: python

 import requests

 AUTHENTICATION_TOKEN = '24f2f5b3-1867-42ac-994c-57140022fb46'
 PROXY_ARGUMENTS = 'session=XYZ|wiretap'

 geoproxies_url = 'http://%s:%s@proxy.geoproxies.com:1080' % (AUTHENTICATION_TOKEN, PROXY_ARGUMENTS)

 r = requests.get('http://httpbin.org/ip', proxies=geoproxies_url)

 print(r.text)


Node
----

* Using the *request* module

.. code:: javascript

  var AUTHENTICATION_TOKEN = '24f2f5b3-1867-42ac-994c-57140022fb46';
  var PROXY_ARGUMENTS = 'session=XYZ|wiretap';

  var proxy = `http://${AUTHENTICATION_TOKEN}:{PROXY_ARGUMENTS}@proxy.geoproxies.com:1080/`;

  require('request')({
      url: 'http://httpbin.org/ip',
      method: 'GET',
      proxy: proxy,
  }, function(err,httpResponse,body) {
      console.info(err, body);
  });



PHP
---

* Using the inbuilt curl extension

.. code:: php

  $AUTHENTICATION_TOKEN = '24f2f5b3-1867-42ac-994c-57140022fb46';
  $PROXY_ARGUMENTS = 'session=XYZ|wiretap';

  $ch = curl_init("http://httpbin.org/ip");

  $options = [
    CURLOPT_PROXY => "http://proxy.geoproxies.com:1080",
    CURLOPT_PROXYUSERPWD => "{$AUTHENTICATION_TOKEN}:{$PROXY_ARGUMENTS}"
  ];

  curl_setopt_array($ch, $options);
  $curl_result = curl_exec($ch);
  curl_close($ch);

  print($curl_result);


Firefox
-------

Firefox allows you to modify its proxy settings. You can find it via the menu Preferences ‣ Advanced ‣ Network ‣ Connection ‣ Settings. Choose Manual proxy configuration, and then fill in the HTTP Proxy textfield to proxy.geoproxies.com and its Port to 1080.

.. image:: _static/firefox_settings.png
