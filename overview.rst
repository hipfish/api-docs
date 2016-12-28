Overview
========

HiPFiSH is essentially two things:
 * A high reliability archive
 * A multi-protocol Content Delivery Network (CDN)

The archive is versatile, reliable and cost effective. It's composed of multiple 3rd party storage and backup services, achieving a higher level of redundancy than is possible with any single provider. The hipfish **Archive API** hides the complexity of dealing with multiple platforms behind a unified interface and security model.

Using the hipfish **Publishing API**, users can publish archived files via a conventional, best of breed HTTP/HTTPS CDN. The unique thing about hipfish is that it also provides Inter Planetary File System (IPFS) publishing, via the worlds largest IPFS CDN. This combines all the benefits of a traditional HTTP/HTTPS CDN with the benefits of IPFS (performance, efficiency, resiliance), ensuring the best possible experience for IPFS users.


Archive
-------
Users can load files into the archive using a variety of methods;
 * directly HTTP POST the file into an API
 * provide the URL of a file (a worker will fetch it)
 * provide an IPFS address (a worker will fetch it)

The archive is replicated across multiple networks and providers, ensuring high availability even if some providers go offline (or out of business).

Users have the option of ensuring archives not published (using a "privacy lock" feature). This is an excellent way to manage off-site backups, or retire


HTTP Publishing
---------------

Users can publish their files via a conventional HTTP/HTTPS CDN. This works in the usual way; files are replicated to regional centers and from there to edge servers, to minimise latency. A conventional CDN provides the best possible performance and availability for HTTP/HTTPS traffic.

This is as simple as toggling a single bit on the individual file (or archive) using the **Publishing API**. If the file (or archive) is "privacy locked", it is not possible to publish it via conventional HTTP/HTTPS CDN.

HiPFiSH is opinionated about file names. All files are published as https://cdn.hipfish.io/ipfs/<hash>/, where <hash> is the unique identifier for a specific version of the file. The <hash> is generated when the file is first saved to the archive. It is actually equal to the IPFS address of the file, if it were to be published via IPFS (the existance of the hash does not indicate that the file is or is not published via IPFS, it is a unique hash of the file contents).


IPFS Publishing
---------------

Users can publish an individual archived file (or entire archive) via the hipfish IPFS CDN, by simply toggling a single bit on the file (or archive) using the **Publishing API**.  If the file (or archive) is "privacy locked", it is not possible to publish it via the IPFS CDN.

The HiPFiSH IPFS CDN is similar to a conventional HTTP/HTTPS CDN, in that files are replicated to edge servers in multiple regions. But IPFS is not a client/server protocol like HTTP/HTTPS, it is a peer to peer protocol. This means the edge servers are actually a globally distributed network freeloader-friendly peers.

In theory, IPFS does not need this. In theory, once your files have been downloaded by a number of fair-playing consumers that go on to serve those files to their neighbours, your own IPFS server can go offline and the data will remain available due to a grid of fair-playing peers. There are certainly circumstances where this works out, but in reality there are also circumstances where some users, particularaly early users of your data, do not enjoy the benefits of a healthy grid of peers serving your data.

The HiPFiSH CDN is a kind of booster or accellerator for the IPFS grid. By publishing your data to our distributed network of peers, you can be sure the worst case scenario is that only our peers are hosting your data. That's a very high minimum standard, it's roughly equivalent to the best possible case for HTTP/HTTPS! Any peering on top of the HiPFiSH CDN is an improvement, especially for remote networks or networks with a sudden rush of interest in your data (for example a science conference). So you have the best of both worlds; At the very least, your data will always be served with a CDN level of performance. If a user has fair-playing peers in their network neighourborhood, their performance will be even better.


Web Interface
-------------

The hipfish.io website allows users to sign up, manage their account and API access tokens. These API access tokens can be used via the API or CLI tool.

The web site also allows users to perform many of the management features available via the CLI tool and API from their workstation, tablet or phone.


Command Line Tool
-----------------

There is a CLI tool (hipfish console) that uses the API, so it also needs an access token. Apart from manageing API access tokens, everything is possible via the CLI.

The CLI tool is called `hipfish`, and it is organised around sub-commands such as `archive` and `publish`. `hipfish --help` will list and describe the various subcommands.

hipfish subcommands also support the `--help` option, such as `hipfish archive --help`, which describe how to use the subcommands.


Application Programming Interface
---------------------------------

The API uses a HATEOS design. This means the design incorporates natural HTTP verbs (GET, POST, PUT, PATCH, DELETE) with resources that can be identified by their URL.

The CLI tool uses the REST API. Therefor, everything that is possible via the CLI is also possible via the API.


More Information
----------------

This documentation covers:
 * getting started: Try this out to get a feel for we web UI
 * applications: Example user-stories, who might find hipfish useful
 * console tool: Understand the features and concepts behind them
 * API: Online resources and verbs for accessing them programatically

The documentation itself:
 * is published at https://hipfish.readthedocs.io/
 * is managed at https://github.com/hipfish/hipfish-docs/

If there are issues with the documents or there is something you would like help with, please feel free to raise a ticket at http://github.com/hipfish/hipfish-docs/issues

The http://hipfish.io/ website is obviously a key resource, and the email helpdesk at support@hipfish.io is also available.
