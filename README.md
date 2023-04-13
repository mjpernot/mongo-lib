# Python project that contains common libraries and classes for Mongo database.
# Classification (U)

# Description:
  This library module consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Mongo database/replica set.


###  This README file is broken down into the following sections:
 * Prerequisites
   - FIPS Environment
 * Installation
   - Pip Installation
 * Testing
   - Unit
   - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-devel (python3-devel if installing for Python 3)

  * FIPS Environment:  If operating in a FIPS 104-2 environment, this package will require at least a minimum of pymongo==3.8.0 or better.  It will also require a manual change to the auth.py module in the pymongo package.  See below for changes to auth.py.
    - Locate the auth.py file python installed packages on the system in the pymongo package directory.
    - Edit the file and locate the \_password_digest function.
    - In the \_password_digest function there is an line that should match: "md5hash = hashlib.md5()".  Change it to "md5hash = hashlib.md5(usedforsecurity=False)".
    - Lastly, it will require the configuration file entry auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.


# Installation:

### Pip Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program and any reference to **{Other_Python_Project}** with the baseline path of another python program.

##### Create requirements file in another program's project to install mongo-lib as a library module.

Create requirements-mongo-lib.txt and requirements-mongo-python-lib.txt files:

```
cd {Python_Project}
cp requirements-mongo-lib.txt {Other_Python_Project}/requirements-mongo-lib.txt
cp requirements-python-lib.txt {Other_Python_Project}/requirements-mongo-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

```
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Mongo-Lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
psutil==5.4.3
pymongo==3.8.0
simplejson==2.0.9
```


# Testing

# Unit Testing:

### Installation:

Install general Mongo libraries and classes using git.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-lib.git
```

Install/upgrade system modules.

```
cd mongo-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Testing:

```
cd {Python_Project}/mongo-lib
test/unit/mongodb_class/unit_test_run.sh
test/unit/mongodb_lib/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/mongo-lib
test/unit/mongodb_class/code_coverage.sh
test/unit/mongodb_lib/code_coverage.sh
```

# Integration Testing:

NOTE:  Part of the Integration testing will require access to a Mongo database server which is part of a replica set.  If this is not the case, then do not run the Mongo Replica part of the testing.

### Installation:

Install the project using the procedures in the Installation section under Unit Testing.

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
    - NOTE 2:  FIPS 140-2 environment requires SCRAM-SHA-1 or SCRAM-SHA-256.
    - NOTE 3:  MONGODB-CR is not supported in Mongodb 4.0 and better.

  * If Mongo is set to use SSL connections, then one or more of the following entries will need to be completed to connect using SSL protocols.  Note:  Read the configuration file (mongo.py.TEMPLATE) to determine which entries will need to be set.
    - ssl_client_ca = None
    - ssl_client_key = None
    - ssl_client_cert = None
    - ssl_client_phrase = None

```
cd test/integration/config
cp mongo.py.TEMPLATE mongo.py
cp mongo.py.TEMPLATE master_mongo.py
cp mongo.py.TEMPLATE slave_mongo.py
chmod 600 mongo.py master_mongo.py slave_mongo.py
vim mongo.py master_mongo.py slave_mongo.py
```

### Testing mongo_class.py - Mongo Stand Alone

```
cd {Python_Project}/mongo-lib
test/integration/mongo_class/integration_test_run.sh
test/integration/mongo_class/code_coverage.sh
```

### Testing mongo_lib.py:

```
cd {Python_Project}/mongo-lib
test/integration/mongo_libs/integration_test_run.sh
test/integration/mongo_libs/code_coverage.sh
```

### Testing mongo_class.py - Mongo Replica Set

```
cd {Python_Project}/mongo-lib
test/integration/mongo_class/replica_integration_test_run.sh
test/integration/mongo_class/replica_code_coverage.sh
```

