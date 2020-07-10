#!/usr/bin/python
# Classification (U)

"""Program:  DB_validate_tbl.py

    Description:  Unit testing of DB.validate_tbl in mongo_class.py.

    Usage:
        test/unit/mongo_class/DB_validate_tbl.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import pymongo

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class DBValidate2(object):

    """Class:  DBValidate2

    Description:  Class stub holder for DB class.

    Methods:
        __init__ -> Class initialization.
        validate_collection -> Stub for DB.db.validate_collection method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.tbl_name = None
        self.full = None

    def validate_collection(self, tbl_name, full):

        """Function:  validate_collection

        Description:  Stub for DB.db.validate_collection method.

        Arguments:
            (input) tbl_name -> Table name.
            (input) full -> True|False - Do full scan.

        """

        self.tbl_name = tbl_name
        self.full = full

        raise pymongo.errors.OperationFailure("ErrorMsg")


class DBValidate(object):

    """Class:  DBValidate

    Description:  Class stub holder for DB class.

    Methods:
        __init__ -> Class initialization.
        validate_collection -> Stub for DB.db.validate_collection method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.tbl_name = None
        self.full = None

    def validate_collection(self, tbl_name, full):

        """Function:  validate_collection

        Description:  Stub for DB.db.validate_collection method.

        Arguments:
            (input) tbl_name -> Table name.
            (input) full -> True|False - Do full scan.

        """

        self.tbl_name = tbl_name
        self.full = full

        return "MessageHere"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_raise_exception2 -> Test the raise exception in pymongo==3.2.0.
        test_raise_exception -> Test the raise exception.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.passwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.db = "test"
        self.db_auth = None

    def test_raise_exception2(self):

        """Function:  test_raise_exception

        Description:  Test the raise exception in pymongo==3.2.0.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.passwd,
                               self.host, self.port)
        mongo.db = DBValidate2()
        status, msg = mongo.validate_tbl("tbl", True)

        self.assertEqual((status), (False))

    @unittest.skip("Skipped due to pymongo is at 3.2.0 instead of 3.8.0")
    def test_raise_exception(self):

        """Function:  test_raise_exception

        Description:  Test the raise exception.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.passwd,
                               self.host, self.port)
        mongo.db = DBValidate2()
        status, msg = mongo.validate_tbl("tbl", True)

        self.assertEqual((status, msg._message), (False, "ErrorMsg"))

    def test_default(self):

        """Function:  test_default

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.passwd,
                               self.host, self.port)
        mongo.db = DBValidate()

        self.assertEqual(mongo.validate_tbl("tbl", True),
                         (True, "MessageHere"))


if __name__ == "__main__":
    unittest.main()
