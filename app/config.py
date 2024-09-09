import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_APP = os.environ.get('FLASK_APP', 'couchbase-flask-starter')
    COUCHBASE_CONNECTION_STRING = os.environ.get('COUCHBASE_CONNECTION_STRING', 'couchbase://localhost')
    COUCHBASE_USERNAME = os.environ.get('COUCHBASE_USERNAME', 'Administrator')
    COUCHBASE_PASSWORD = os.environ.get('COUCHBASE_PASSWORD', 'password')
    COUCHBASE_USE_CAPELLA = os.environ.get('COUCHBASE_USE_CAPELLA', 'false').lower() == 'true'
    COUCHBASE_DEFAULT_BUCKET = os.environ.get('COUCHBASE_DEFAULT_BUCKET', 'default')
    COUCHBASE_DEFAULT_SCOPE = os.environ.get('COUCHBASE_DEFAULT_SCOPE', '_default')
    COUCHBASE_DEFAULT_COLLECTION = os.environ.get('COUCHBASE_DEFAULT_COLLECTION', '_default')