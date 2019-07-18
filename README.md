# Python project that contains common libraries and classes for Mongo database.
# Classification (U)

# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Mongo database.  These programs are not standalone programs, but are available for python programs to utilize.


###  This README file is broken down into the following sections:
 * Prerequisites
 * Installation
 * Program Descriptions
 * Testing
   - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * List of local packages that need to be installed within the program structure.
    - lib/arg_parser
    - lib/gen_libs
    - lib/cmds_gen


# Installation:
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirement files for the supporting library in another program's project.

```
cd {Python_Project}
cat requirements-mongo-lib.txt >> {Other_Python_Project}/requirements-mongo-lib.txt
cat requirements-python-lib.txt >> {Other_Python_Project}/requirements-python-lib.txt
```

Place the following commands into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the system module requirements to the another program's requirements.txt file and remove any duplicates.

``
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general Mongo libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-lib.git
```

Install supporting classes and libraries

```
cd mongo-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Program Descriptions:
### Program: mongodb_class.py
##### Description: Class definitions and methods for connecting to Mongodb database system.
##### Classes:
  * Server => Class which is a representation of a Mongo database server.
  * DB => Class which is a representation of a database instance in a Mongo database server.
  * Coll => Class which is a representation of a collection instance in a Mongo database server.
  * Rep => Class which is a representation of a Mongo database server in replication.
  * MasterRep => Class which is a representation of a Master Replication Mongo database server.
  * SlaveRep => Class which is a representation of a Slave Replication Mongo database server.
  * RepSet => Class which is a representation of a Mongo Replica set.
  * RepSetColl => Class which is a representation of a collection instance in a Mongo database server.

### Program: mongodb_libs.py
##### Description: Library of function calls for a Mongodb database system.

# Testing

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongodb_class.py and mongodb_libs.py programs.

### Installation:

Install general Mongo libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-lib.git
```

Install supporting classes and libraries

```
cd mongo-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

# Unit test runs for mongodb_class.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-lib
test/unit/mongo_class/MasterRep_init.py
test/unit/mongo_class/RepSetColl_coll_cnt.py
test/unit/mongo_class/RepSetColl_coll_del_many.py
test/unit/mongo_class/RepSetColl_connect.py
test/unit/mongo_class/RepSetColl_init.py
test/unit/mongo_class/RepSetColl_ins_doc.py
test/unit/mongo_class/RepSet_connect.py
test/unit/mongo_class/RepSet_init.py
test/unit/mongo_class/Rep_fetch_nodes.py
test/unit/mongo_class/Rep_init.py
test/unit/mongo_class/Server_connect.py
test/unit/mongo_class/Server_disconnect.py
test/unit/mongo_class/Server_fetch_adr.py
test/unit/mongo_class/Server_init.py
test/unit/mongo_class/Server_is_locked.py
test/unit/mongo_class/Server_is_primary.py
test/unit/mongo_class/Server_upd_server_attr.py
test/unit/mongo_class/Server_upd_srv_stat.py
test/unit/mongo_class/SlaveRep_init.py
```

### All unit testing for mongodb_class.py:
```
test/unit/mongodb_class/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/mongodb_class/code_coverage.sh
```

# Unit test runs for mongodb_libs.py:

### Unit:  
```
test/unit/mongodb_lib/
```

### All unit testing for mongodb_ib.py:
```
test/unit/mongodb_lib/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/mongodb_lib/code_coverage.sh
```

