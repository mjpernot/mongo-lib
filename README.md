# Python project that contains common libraries and classes for Mongo database.
# Classification (U)

# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Mongo database.  These programs are not standalone programs, but are available for python programs to utilize.


###  This README file is broken down into the following sections:
 * Prerequisites
 * Installation
   - Pip Installation
   - Git Installation
 * Testing
   - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * List of local packages that need to be installed within the program structure.
    - lib/arg_parser
    - lib/gen_libs
    - lib/cmds_gen


# Installation:
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

##### Create requirements file in another program's project to install mongo-lib as a library module.

Create requirements-mongo-lib.txt file:

```
vim {Other_Python_Project}/requirements-mongo-lib.txt
```

Add the following lines to the requirements-mongo-lib.txt file:

```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/mongo-lib.git#egg=mongo-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:

```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md
```

Add the following lines under the "Install supporting classes and libraries" section.

```
   pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Mongo-Lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:

```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:

```
psutil==5.4.3
pymongo==3.2.0
simplejson==2.0.9
```


### Git Installation:

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

