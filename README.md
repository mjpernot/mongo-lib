# Python project that contains common libraries and classes for Mongo database.
# Classification (U)

# Description:
  This library module consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Mongo database/replica set.


###  This README file is broken down into the following sections:
 * Prerequisites
   - Secure Environment
 * Configuration
 * Installation
   - Pip Installation
 * Testing
   - Unit
   - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python3-devel
    - gcc

  * Secure Environment:  If operating in a Secure environment, this package will require at least a minimum of pymongo==3.8.0 or better.  It will also require a manual change to the auth.py module in the pymongo package.  See below for changes to auth.py.
    - Locate the auth.py file python installed packages on the system in the pymongo package directory.
    - Edit the file and locate the \_password_digest function.
    - In the \_password_digest function there is an line that should match: "md5hash = hashlib.md5()".  Change it to "md5hash = hashlib.md5(usedforsecurity=False)".
    - Lastly, it will require the configuration file entry auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.


# Configuration
Any program that wants to use this module to connect to mongo, recommend using the mongo.py file as a baseline configuration file for the mongo connection configuration.


# Installation:

### Pip Installation:

##### Create requirements file in another program's project to install mongo-lib as a library module.

  * Create requirements-mongo-lib.txt and requirements-mongo-python-lib.txt.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/mongo-lib.git@N.N.N#egg=mysql-lib' > requirements-mongo-lib.txt
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git@N.N.N#egg=python-lib' > requirements-mongo-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file and the following lines to install the library modules:

```
python -m pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-mongo-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):

##### Add the general mongo-Lib requirements to (requirements3.txt) to the other program's requirements3.txt file.

Redhat 8 (Running Python 3.9/3.12):

##### Add the general mongo-Lib requirements to (requirements39.txt) to the other program's requirements39.txt file.


# Testing

### Git Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-lib.git
```

Install/upgrade system modules.

NOTE: Install as the user that will use the package.

Redhat 8 (Running Python 3.6):

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.9/3.12):

```
python -m pip install --user -r requirements39.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install supporting classes and libraries

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
test/unit/mongodb_class/unit_test_run.sh
test/unit/mongodb_lib/unit_test_run.sh
```

### Code coverage:
```
test/unit/mongodb_class/code_coverage.sh
test/unit/mongodb_lib/code_coverage.sh
```

# Integration Testing:

NOTE:  Part of the Integration testing will require access to a Mongo database server which is part of a replica set.  If this is not the case, then do not run the Mongo Replica part of the testing.

### Installation:

Install the project using the procedures in the Git Installation section.

### Configuration:

Create Mongo configuration files.
  Make the appropriate change to the environment.
  Note 1:  There will be three configuration files created for testing.  One for a standalone Mongo database and two will be created that require the Mongo databases to be part of a replica set.  One of these will be the master_mongo.py and the other one will be the slave_mongo.py.
  NOTE 2:  Even if testing only the replication side, the testing files will still require the mongo.py to be setup.
  * Change these entries in the Mongo setup:
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - port = 27017
    - conf_file = None
    - auth = True
    - auth_db = "admin"
    - auth_mech = "SCRAM-SHA-1"

  * Connecting to a Mongo replica set.
    Note:  These will only be in the master_mongo.py and slave_mongo.py files.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

  * Notes for auth_mech configuration entry:
    - NOTE 1:  SCRAM-SHA-256 only works for Mongodb 4.0 and better.
    - NOTE 2:  Secure environment requires SCRAM-SHA-1 or SCRAM-SHA-256.

  * If Mongo is set to use TLS or SSL connections, then one or more of the following entries will need to be completed to connect using TLS or SSL protocols.
    - Note 1:  Read the configuration file to determine which entries will need to be set.
    - Note 2:  Use the individual test files to test using SSL and/or TLS connections - see below.

    - SSL:
        -> auth_type = None
        -> ssl_client_ca = None
        -> ssl_client_key = None
        -> ssl_client_cert = None
        -> ssl_client_phrase = None
    - TLS:
        -> auth_type = None
        -> tls_ca_certs = None
        -> tls_certkey = None
        -> tls_certkey_phrase = None

```
cp mongo.py test/integration/config/mongo.py
cp mongo.py test/integration/config/master_mongo.py
cp mongo.py test/integration/config/slave_mongo.py
chmod 600 test/integration/config/mongo.py test/integration/config/master_mongo.py test/integration/config/slave_mongo.py
vim test/integration/config/mongo.py test/integration/config/master_mongo.py test/integration/config/slave_mongo.py
```

### Testing mongo_class.py - Mongo Stand Alone

```
test/integration/mongo_class/integration_test_run.sh
test/integration/mongo_class/code_coverage.sh
```

### Testing mongo_lib.py:

```
test/integration/mongo_libs/integration_test_run.sh
test/integration/mongo_libs/code_coverage.sh
```

### Testing mongo_lib.py with SSL and/or TLS connections:

```
test/integration/mongo_libs/create_instance_ssl.py
test/integration/mongo_libs/create_instance_tls.py
test/integration/mongo_libs/crt_base_cmd_ssl.py
test/integration/mongo_libs/crt_base_cmd_tls.py
test/integration/mongo_libs/crt_coll_inst_ssl.py
test/integration/mongo_libs/crt_coll_inst_tls.py
```

### Testing mongo_class.py - Mongo Replica Set

```
test/integration/mongo_class/replica_integration_test_run.sh
test/integration/mongo_class/replica_code_coverage.sh
```

### Testing mongo_class.py - Mongo Replica Set with SSL and/or TLS connections:

```
test/integration/mongo_class/slaverep_init_ssl.py
test/integration/mongo_class/slaverep_init_tls.py
```

