import logging
from flask import Flask
from app.config import Config
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from couchbase.exceptions import CouchbaseException

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    try:
        # Initialize Couchbase connection
        auth = PasswordAuthenticator(
            app.config['COUCHBASE_USERNAME'],
            app.config['COUCHBASE_PASSWORD']
        )
        cluster = Cluster(app.config['COUCHBASE_CONNECTION_STRING'], ClusterOptions(auth))
        bucket = cluster.bucket(app.config['COUCHBASE_DEFAULT_BUCKET'])
        app.couchbase_collection = bucket.scope(app.config['COUCHBASE_DEFAULT_SCOPE']).collection(app.config['COUCHBASE_DEFAULT_COLLECTION'])
        
        # Test the connection
        cluster.ping()
        logger.info("Successfully connected to Couchbase")
    except CouchbaseException as e:
        logger.error(f"Failed to connect to Couchbase: {str(e)}")
        raise

    from app import routes
    app.register_blueprint(routes.bp)

    return app