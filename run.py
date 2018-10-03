from boto.s3.connection import S3Connection
from boto.s3.key import Key
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib2
import time
import os
import urlparse

s3_id = os.environ['S3_ID']
s3_secret = os.environ['S3_SECRET']
s3_bucket = os.environ['S3_BUCKET']
download_url = os.environ['DOWNLOAD_URL']
polling_interval = int(os.environ['POLLING_INTERVAL'])

def downloadToS3():

	request = urllib2.Request(download_url)
	response = urllib2.urlopen(request)

	conn = S3Connection(s3_id, s3_secret)
	bucket = conn.create_bucket(s3_bucket)
	k = Key(bucket)

	basename = os.path.basename(urlparse.urlparse(download_url).path)
	timestr = time.strftime('%Y%m%d_%H%M%S_')
	k.name = timestr + basename
	k.set_contents_from_string(response.read(), {'Content-Type': response.info().gettype()})

downloadToS3()

scheduler = BlockingScheduler()
scheduler.add_job(downloadToS3, 'interval', seconds=polling_interval)
scheduler.start()