Archive
=======

I think our interface needs the concept of "archive", which is an intermediary between the conventional CDN "origin" and the hosting arrangement.

.. graphviz::

   digraph d {
      archive [shape=rectangle];
      local_file [shape=rectangle];
      post_local;
      post_local -> local_file;
      post_local -> archive;
      http_origin [label=rectangle];
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