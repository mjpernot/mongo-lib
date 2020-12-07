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
    - git
    - python-pip

  * List of local packages that need to be installed within the program structure.
    - lib/arg_parser
    - lib/gen_libs
    - lib/cmds_gen

  * FIPS Environment
    If operating in a FIPS 104-2 environment, this package will require at least a minimum of pymongo==3.8.0 or better.  It will also require a manual change to the auth.py module in the pymongo package.  See below for changes to auth.py.
    - Locate the auth.py file python installed packages on the system in the pymongo package directory.
    - Edit the file and locate the \_password_digest function.
    - In the \_password_digest function there is an line that should match: "md5hash = hashlib.md5()".  Change it to "md5hash = hashlib.md5(usedforsecurity=False)".


# Installation:

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

##### Create requirements file in another program's project to install mongo-lib as a library module.

Create requirements-mongo-lib.txt and requirements-python-lib.txt files:

```
cd {Python_Project}
cp requirements-mongo-lib.txt > {Other_Python_Project}/requirements-mongo-lib.txt
cp requirements-python-lib.txt > {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

```
   pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
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
  * Replace **{Python_Project}** with the baseline path of the python program.

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
  * Replace **{Python_Project}** with the baseline path of the python program.

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

NOTE:  Integration testing will require access to a Mongo database server which is part of a replica set.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-lib.git
```

Install/upgrade system modules.

```
cd mongo-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Configuration:

Create Mongo configuration files.  Two configuration files will be created, one with master as main connection and one with slave as main connection.  Make the appropriate change to the environment.
  * Change these entries in the Mongo setup:
    - user = "USER"
    - japd = "PWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"
    - port = 27017
    - conf_file = None
    - auth = True

  * Connecting to a Mongo replica set.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
cd test/integration/config
cp mongo.py.TEMPLATE mongo.py
cp mongo.py.TEMPLATE slave_mongo.py
chmod 600 mongo.py slave_mongo.py
vim mongo.py slave_mongo.py
```

### Testing mongo_class.py

```
cd {Python_Project}/mongo-lib
test/integration/mongo_class/integration_test_run.sh
test/integration/mongo_class/code_coverage.sh
```

### Testing mongo--lib.py:

```
cd {Python_Project}/mongo-lib
test/integration/mongo_libs/integration_test_run.sh
test/integration/mongo_libs/code_coverage.sh
```

