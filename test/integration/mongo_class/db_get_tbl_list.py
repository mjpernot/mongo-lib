# Classification (U)

"""Program:  db_get_tbl_list.py

    Description:  Integration testing of DB.get_tbl_list in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_get_tbl_list.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_pass_false
        test_pass_true2
        test_pass_true
        test_default2
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.database = "admin"
        self.tbl_name = "system.users"
        self.mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        self.mongo.connect()
        self.mongo.chg_db(self.database)

    def test_pass_false(self):

        """Function:  test_pass_false

        Description:  Test pass False to include system tables.

        Arguments:

        """

        db_list = self.mongo.get_tbl_list(False)

        self.assertTrue(isinstance(db_list, list))

    def test_pass_true2(self):

        """Function:  test_pass_true2

        Description:  Test pass True to include system tables.

        Arguments:

        """

        db_list = self.mongo.get_tbl_list(True)

        self.assertTrue(self.tbl_name in db_list)

    def test_pass_true(self):

        """Function:  test_pass_true

        Description:  Test pass True to include system tables.

        Arguments:

        """

        db_list = self.mongo.get_tbl_list(True)

        self.assertTrue(isinstance(db_list, list))

    def test_default2(self):

        """Function:  test_default2

        Description:  Test get_tbl_list method with default arguments.

        Arguments:

        """

        db_list = self.mongo.get_tbl_list()

        self.assertTrue(self.tbl_name in db_list)

    def test_default(self):

        """Function:  test_default

        Description:  Test get_tbl_list method with default arguments.

        Arguments:

        """

        db_list = self.mongo.get_tbl_list()

        self.assertTrue(isinstance(db_list, list))


if __name__ == "__main__":
    unittest.main()
