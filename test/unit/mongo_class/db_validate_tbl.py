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
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class DBValidate2():                            # pylint:disable=R0903

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


class DBValidate():                             # pylint:disable=R0903

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

        self.assertFalse(status, False)

    def test_raise_exception(self):

        """Function:  test_raise_exception

        Description:  Test the raise exception.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.db_inst = DBValidate2()
        status, msg = mongo.validate_tbl("tbl", True)

        self.assertEqual((
            status, msg._message), (False, "ErrorMsg"))  # pylint:disable=W0212

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
