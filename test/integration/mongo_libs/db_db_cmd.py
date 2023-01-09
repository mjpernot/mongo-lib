# Classification (U)

"""Program:  db_db_cmd.py

    Description:  Integration testing of DB.db_cmd in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_db_cmd.py

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
        test_object2
        test_object
        test_base_cmd2
        test_base_cmd

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

    def test_object2(self):

        """Function:  test_object2

        Description:  Test with object passed to method.

        Arguments:

        """

        data = self.mongo.db_cmd("collstats", obj=self.tbl_name)

        self.assertEqual(data["ns"], self.database + "." + self.tbl_name)

    def test_object(self):

        """Function:  test_object

        Description:  Test with object passed to method.

        Arguments:

        """

        data = self.mongo.db_cmd("collstats", obj=self.tbl_name)

        self.assertTrue(isinstance(data, dict))

    def test_base_cmd2(self):

        """Function:  test_base_cmd2

        Description:  Test with base command.

        Arguments:

        """

        data = self.mongo.db_cmd("buildinfo")

        self.assertTrue(isinstance(data["storageEngines"], list))

    def test_base_cmd(self):

        """Function:  test_base_cmd

        Description:  Test with base command.

        Arguments:

        """

        data = self.mongo.db_cmd("buildinfo")

        self.assertTrue(isinstance(data, dict))


if __name__ == "__main__":
    unittest.main()
