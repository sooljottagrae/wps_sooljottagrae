from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    "*",
]


STATICFILES_STORAGE = 'sooljottagrae.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# FILES_STORAGE = 'sooljottagrae.storage.S3PipelineCachedStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = 'dtskqisbdre76.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://dtskqisbdre76.cloudfront.net/"
