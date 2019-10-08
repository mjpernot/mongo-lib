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

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class DBValidate(object):

    """Class:  DBValidate

    Description:  Class stub holder for DB class.

    Methods:
        validate_collection -> Stub for DB.db.validate_collection method.

    """

    def validate_collection(self, tbl_name, full):

        """Function:  validate_collection

        Description:  Stub for DB.db.validate_collection method.

        Arguments:
            (input) tbl_name -> Table name.
            (input) full -> True|False - Do full scan.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
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

    def test_default(self):

        """Function:  test_default

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.passwd,
                               self.host, self.port)
        mongo.db = DBValidate()

        self.assertTrue(mongo.validate_tbl("tbl", True))


if __name__ == "__main__":
    unittest.main()
