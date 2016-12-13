# HiPFiSH API Documentation

This is aspirational, the API doesn't exist yet. When it does, it might have three parts: `profile`, `archive` and `hosting`.

## Profile

The profile part of the API (`/profile/*`) is for managing your account. Specifically, the things you can do from the web site that you might also want to do from the CLI (or some other integration).

All the other interfaces requre authentication (via tokens). The /profile/ part might have some token management features, such as:
 * Test validity of authentication token
 * Access account information for valid token

The various other services will produce logs. Using the authentication token, the user should be able to query something like an ES endpoint for their own logs. From an API perspective, this is hopefully just a case of saying "here is your read-only endpoint, knock yourself out"

In the MVP we will create new tokens using the web UI. It's entirely possible that we might also want to 

## /archive/

Once you can access the API because you have a valid token, you need files in the archive before you can publish them in IPFS.

One way to get a file in the archive is to post it directly there:
````
POST /archive/file/ {file, archive_config, hosting_config}
```
This will returns IPFS address of uploaded file, with some other metadata (such as size of file and archive configuration).

There is a maximum file size that can be uploaded this way. I don't know what it is yet, probably some MB. Hopefully it;s large enough to post a photo or video from a phone, so 10Mb, but may need to be smaller than that. There might also be some limits which are related to time (size+bandwidth).
Maximal file size is configurable in Nginx for classic deployment and 6MB (including request metadata) for Lambda. But these restrictions are generally avoidable (for example, by AWS S3 POST upload).

The `file` parameter is mandatory. With no file posted, it doesn't make sense.

The `archive_config` parameter is optional. If not supplied, defaults are used. I don't know what the archive_config parameters are yet but they include `store until` (file will be disposed after that date). They may also `privacy_lock`; if true makes file unpublishable (i.e. pure private archive), default to False. I have a few ideas about requirements to support various access control policies but they are not resolved yet.

The `hosting_config` is optional with default of none. If not none (and if archive_config.privacy_lock is false), this chains an API call to the right part of `/hosting/*` so that once archived, the file is immediately published (per hosting_config).

Another way to get a file in the archive is to pull it into the archive from IPFS:
```
POST /archive/ipfs/ {IPFS-ADDRESS, hosting_config, archive_config}
```
This has the limitation that the file has to be available from IPFS (already published somewhere). It has the advantage that a arbitrarially large files may be archived this way. The limits on the size of the file that can be downloaded are configured in the user profile, and are linked to the financial costs of downloading and storing very large files.

`hosting_metadata` is same as for `POST /archive/file/`.

When this method is called, it causes a background process to retrieved from IPFS network and saved to the archive. The method returns an address (`/archive/download_status/IPFS-ADDRESS`) where the status of the download can be queried.

i.e.
```
GET /archive/download_status/IPFS-ADDRESS
```
This returns one of two things.

If the download is still in progress, it returns status of download (if still in progress). This includes time spent since download started, ammount downloaded so far, and maybe some groovy array of IPFS stuff the hosts the data it streaming from.

If the download has completed, the method returns a simple structure containing the IPFS address and file metadata (size of file, time download started, time it finished, maybe other stuff too). We eventually keep this download_status for as long as the file is in the archive (or do we? we could delete the IPFS-ADDRESS file after a month)

When the download is complete, the response returned by `/archive/download_status/IPFS-ADDRESS` includes the IPFS address and the file metadata. When a file is archived (i.e. after a sucessful call of `POST /archive/ipfs {IPFS-ADDRESS}`, we can also fetch the file metadata like this:
```
GET /archive/ipfs/IPFS-ADDRESS/
```
This returns the full file metadata, including hosting configuration (disposal date, backup redundancy, etc). So the only data we would need to keep to service download_status/IPFS-ADDRESS requests is the mapping between IPFS-ADDRESS and ipfs_address. We could chain the request to `GET /archive/ipfs/IPFS-ADDRESS/` to fetch the rest of it.

If we want to change the archival config for a file, we simply PUT new config to the archive, like this:
```
PUT /archive/ipfs/IPFS-ADDRESS {new hosting metadata}
```
Obviously, some changes are not valid (you can't PUT a different file size, for example). There should be sane error messages if you try. But you should be able to PUT a different disposal date on the record. If the new disposal date is in the past, you might as well call this instead:
```
DELETE /archive/ipfs/IPFS-ADDRESS
```

Now, with all this stuff you can do to records, you should be able to find records to do them to. For this, you need the search API.
```
GET /archive/ipfs/foo=”bar”&baz=”123”
```
I don't know what `foo` and `baz` are, search parameters. It's the same as the UI search interface (basically, read-only access to an elastic search index of your file metadata).

The search returns a list of IPFS addresses meeting the criteria. If you want to know more about each address, `GET` it yourself.

## /hosting/
This is basically TODO.

We can use it to Publish archived files… Note introduction of `hosting_config` in `POST /archive/file/` above. Yeah, that stuff.

There might also be access to something like graphana? (carbon/statsd interface), so you can get realtime data about access to your hosted stuff.

