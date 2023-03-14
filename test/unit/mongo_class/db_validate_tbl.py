# Classification (U)

"""Program:  db_validate_tbl.py

    Description:  Unit testing of DB.validate_tbl in mongo_class.py.

    Usage:
        test/unit/mongo_class/db_validate_tbl.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
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
        __init__
        validate_collection

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
            (input) tbl_name
            (input) full

        """

        self.tbl_name = tbl_name
        self.full = full

        raise pymongo.errors.OperationFailure("ErrorMsg")


class DBValidate(object):

    """Class:  DBValidate

    Description:  Class stub holder for DB class.

    Methods:
        __init__
        validate_collection

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
            (input) tbl_name
            (input) full

        """

        self.tbl_name = tbl_name
        self.full = full

        return "MessageHere"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_raise_exception2
        test_raise_exception
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.db_auth = None

    def test_raise_exception2(self):

        """Function:  test_raise_exception

        Description:  Test the raise exception in pymongo==3.2.0.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.db_inst = DBValidate2()
        status, _ = mongo.validate_tbl("tbl", True)

        self.assertEqual((status), (False))

    @unittest.skip("Bug: Skipped since pymongo 3.2.0 is current production.")
    def test_raise_exception(self):

        """Function:  test_raise_exception

        Description:  Test the raise exception.

        Note:  This test will fail if pymongo is below 3.8.0.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.db_inst = DBValidate2()
        status, msg = mongo.validate_tbl("tbl", True)

        self.assertEqual((status, msg._message), (False, "ErrorMsg"))

    def test_default(self):

        """Function:  test_default

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.db_inst = DBValidate()

        self.assertEqual(mongo.validate_tbl("tbl", True),
                         (True, "MessageHere"))


if __name__ == "__main__":
    unittest.main()
