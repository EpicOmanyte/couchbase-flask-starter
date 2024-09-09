# Couchbase Flask Starter Kit
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/couchbase-starter-kit/couchbase-flask-starter)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/couchbase-starter-kit/couchbase-flask-starter)

## Configuration

| Variable Name                      | Description                                                 |      Default value       |
|:-----------------------------------|:------------------------------------------------------------|:------------------------:|
| FLASK_APP                          | The name of your application                                | couchbase-flask-starter  |
| COUCHBASE_CONNECTION_STRING        | A couchbase connection string                               |            -             |
| COUCHBASE_USERNAME                 | Username for authentication with Couchbase                  |            -             |
| COUCHBASE_PASSWORD                 | Password for authentication with Couchbase                  |            -             |
| COUCHBASE_USE_CAPELLA              | Use to change the connection profile                        |          false           |
| COUCHBASE_DEFAULT_BUCKET           | The name of the Couchbase Bucket, parent of the scope       |         default          |
| COUCHBASE_DEFAULT_SCOPE            | The name of the Couchbase scope, parent of the collection   |         _default         |
| COUCHBASE_DEFAULT_COLLECTION       | The name of the Couchbase collection to store the Documents |         _default         |

## Unit Tests

Unit tests are run using pytest.

## Running the Application

To run the application, use the following command:

```
python run.py
```

## Development with Gitpod

This project is configured to work with Gitpod. Click the "Open in Gitpod" button above to start a new workspace.
