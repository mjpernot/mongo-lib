# Classification (U)

"""Program:  db_get_tbl_list.py

    Description:  Unit testing of DB.get_tbl_list in mongo_class.py.

    Usage:
        test/unit/mongo_class/db_get_tbl_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class DBValidate(object):

    """Class:  DBValidate

    Description:  Class stub holder for DB class.

    Methods:
        __init__
        collection_names
        list_collection_names

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.include_system_collections = None

    def collection_names(self, include_system_collections):

        """Function:  collection_names

        Description:  Stub for DB.db.collection_names method.

        Arguments:
            (input) include_system_collections -> True|False - Include system
                tables

        """

        self.include_system_collections = include_system_collections

        return True

    def list_collection_names(self, include_system_collections):

        """Function:  list_collection_names

        Description:  Stub for DB.db.list_collection_names method.

        Arguments:
            (input) include_system_collections -> True|False - Include system
                tables

        """

        self.include_system_collections = include_system_collections

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
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

    def test_default(self):

        """Function:  test_default

        Description:  Test get_tbl_list method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.db_inst = DBValidate()

        self.assertTrue(mongo.get_tbl_list(True))


if __name__ == "__main__":
    unittest.main()
