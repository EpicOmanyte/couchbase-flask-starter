from couchbase.management.buckets import CreateBucketSettings

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
        
        # Try to get the bucket, create it if it doesn't exist
        try:
            bucket = cluster.bucket(app.config['COUCHBASE_DEFAULT_BUCKET'])
        except CouchbaseException as e:
            if isinstance(e, BucketNotFoundException):
                # Create the bucket
                bucket_manager = cluster.buckets()
                bucket_manager.create_bucket(CreateBucketSettings(
                    name=app.config['COUCHBASE_DEFAULT_BUCKET'],
                    bucket_type='couchbase',
                    ram_quota_mb=100
                ))
                bucket = cluster.bucket(app.config['COUCHBASE_DEFAULT_BUCKET'])
            else:
                raise

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