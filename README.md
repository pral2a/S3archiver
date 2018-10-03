S3UrlArchiver
=============

**Just a test. Not production ready!**

Fetch a URL and stores the content on an S3 bucket periodically

Example `.env`

```
S3_ID= #AWS ID
S3_SECRET= #AWS Secret
S3_BUCKET= #AWS Bucket
DOWNLOAD_URL= #URL to fetch
POLLING_INTERVAL= #Polling interval in seconds
```

Build like:

`docker build -t mys3archiver .`

Run like:

`docker run --env-file .env mys3archiver`