Application Programming Interface
=================================

TODO:
 * document the API using HATEOS pattern (organise by resource subheading, then resource/verb sub-subheading)
 * cleanup this gumph

+---------------+----------------------------------------------------------------------------------------------+
| Path          | Description                                                                                  |
+===============+==============================================================================================+
| /archive/     | Unlike a traditional HTTP(S) CDN, an IPFS CDN can not assume the file is available as a URL. |
|               | Resources must somehow be placed in the hipfish archive before they can be reliably hosted.  |
|               | This archive is actually quite useful on it's own (it's durable, and can be kept private for |
|               | record keeping use-cases). This is a low-level API.                                          |
+---------------+----------------------------------------------------------------------------------------------+
| /hosting/     | Once a file is in the archive, it can be reliably published on IPFS using the hosting API.   |
|               | This low-level API provides fine-grained controll over hosting.                              |
+---------------+----------------------------------------------------------------------------------------------+
| /collections/ | A high-level API that allows users to archive and host collections of files as a group. This |
|               | API is quite similar to traditional CDN APIs, and is designed for maximum convenience. It's  |
|               | probably the one you want :)                                                                 |
+---------------+----------------------------------------------------------------------------------------------+


Low level `archive` api:
 * POST file to archive, returns archive job GUID
 * POST URL to spider that does `HTTP GET` into archive, returns archive job GUID 
 * POST IPFS address to spider that does `IPFS GET` into archive, returns archive job GUID
 * GET archive job GUID, returns status of archive job
 * `GET /archive/ipfs-hash/config` returns status/config of archive (if possible)
 * `PUT /archive/upfs-hash/config` updates config of archive

Low level "hosting" api:
 * POST ipfs address to hosting collection, if status of address is "archived" then idempotently adds file to hosting collection


Authentication
--------------

Access to the HiPFiSH API is controlled via API tokens. These can be managed via the Web UI.

TODO:
 * insert screen shots and HOWTO for API token management and account management
 * feature specification for API token management and account management
 * would we ever use the API to manage API tokens (how to bootstrap it - would require account creation, credit card etc, the whole thing?)


Archive
-------

One difference between HiPFiSH and a traditional (HTTP/HTTPS) Content Delivery Network is the concept Archive. With a traditional CDN, resources are proxied from an *origin* (or *upstream*). With IPFS, the origin resource may or may not exist, or may or may not be available.

With HiPFiSH, resources are first loaded into the archive, and then they can be served via IPFS.

.. graphviz::

   digraph d {
      archive [shape=rectangle];
      local_file [shape=rectangle];
      post_local;
      post_local -> local_file;
      post_local -> archive;
      http_origin [shape=rectangle];
      post_http;
      post_http -> http_origin;
      post_http -> archive;
      ipfs_origin [shape=rectangle];
      post_ipfs;
      post_ipfs -> ipfs_origin;
      post_ipfs -> archive;
   }

We should have multiple methods to get a file into the archive:
 * POST the file directly
 * POST a URL, which will be subject to a HTTP(S) GET request to pull the file into the archive.
 * POST an IPFS address, which will be subject to a an IPFS GET request to pull the file into the archive.

The first method (POST file) would work with a single file. The other two methods (POST URL/IPFS address) could reasonably work with a (potentially very large) collection of addresses. Conceivably, these collection of addresses could be of mixed type (URLs and IPFS addresses).

All these methods could take some time (non-blocking I/O), so they should immediately return a URL that can be used to check the status status address. For submitted collections of addresses, should it be:
 * a single URL (returning a collection of statuses); or
 * a collection of URLs, (each returning a single status)

The HTTP(S) and IPFS addresses may or may not succeed, due to file availability. So the 


Hosting
-------

TODO:
 * document hosting requirements
 * design hosting API


Search
------

TODO:
 * document search requirements


Statistics
----------

TODO:
 * document statistics requirements
 * design statistics API
 * note similarity and difference to search API (comment elements/paramaters please)


Billing
-------

TODO:
 * document billing requirements
 * design billing API
