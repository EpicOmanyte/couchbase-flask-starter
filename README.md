# Couchbase Flask Starter Kit
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/couchbase-starter-kit/couchbase-flask-starter)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/couchbase-starter-kit/couchbase-flask-starter)
![Test Suite](https://github.com/couchbase-starter-kit/couchbase-flask-starter/actions/workflows/run-tests.yml/badge.svg)
![Couchbase Capella](https://img.shields.io/badge/Couchbase_Capella-Enabled-red)
[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)
![Static Badge](https://img.shields.io/badge/Code_of_Conduct-Contributor_Covenant-violet.svg)

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

## Getting Started

Follow these steps to get the starter kit up and running on yoru local machine. 

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Git 

### Clone the repository

```
git clone https://github.com/couchbase-starter-kit/couchbase-flask-starter.git
cd couchbase-flask-starter

### Install Dependencies

```
pip3 install -r "requirements.txt"
```

### Configure Couchbase Credentials 

Copy the `.env.sample` file in the root directory of the project and rename it to `.env`. Update the `.env` file with your Couchbase credentials as follows:

```
FLASK_APP=couchbase-flask-starter
COUCHBASE_CONNECTION_STRING="couchbase://localhost"
COUCHBASE_USERNAME="Administrator"
COUCHBASE_PASSWORD="password"
COUCHBASE_USE_CAPELLA=false
COUCHBASE_DEFAULT_BUCKET="default"
COUCHBASE_DEFAULT_SCOPE="_default"
COUCHBASE_DEFAULT_COLLECTION="_default"
```

You can obtain those credentials by first creating an account on Couchbase Capella at [https://cloud.couchbase.com/](https://cloud.couchbase.com/) and then creating a database. Inside the database, create a bucket. The name of the bucket is what you should use for the `COUCHBASE_DEFAULT_BUCKET` environment variable.

Once you have done so, you can navigate to the `Connect` tab in the database and copy the connection string URL. This is what you should use for the `COUCHBASE_CONNECTION_STRING` environment variable. You will also need to create a user with the appropriate permissions and use the username and password for the `COUCHBASE_USERNAME` and `COUCHBASE_PASSWORD` environment variables.

## Unit Tests

Unit tests are run using pytest.

## Running the test suite

To run the test suite, use the following command: 

```
pytest 
```

## Running the Application

To run the application, use the following command:

```
python run.py
```

## Development with Gitpod

This project is configured to work with Gitpod. Click the "Open in Gitpod" button above to start a new workspace.
