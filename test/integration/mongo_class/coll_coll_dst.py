# Classification (U)

"""Program:  coll_coll_dst.py

    Description:  Integration testing of Coll.coll_dst in mongo_class.py.

    Usage:
        test/integration/mongo_class/coll_coll_dst.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class                              # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_query2
        test_query
        test_empty_query
        test_no_query

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
        self.coll = "system.users"
        self.mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

    def test_query2(self):

        """Function:  test_query2

        Description:  Test with query command.

        Arguments:

        """

        self.mongo.connect()
        data = self.mongo.coll_dst("db")
        self.mongo.disconnect()

        self.assertTrue(data)

    def test_query(self):

        """Function:  test_query

        Description:  Test with query command.

        Arguments:

        """

        self.mongo.connect()
        data = self.mongo.coll_dst("db")
        self.mongo.disconnect()

        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
