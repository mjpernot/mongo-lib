# Classification (U)

"""Program:  server_fetch_svr_info.py

    Description:  Integration testing of Server.fetch_svr_info in
        mongo_class.py.

    Usage:
        test/integration/mongo_class/server_fetch_svr_info.py

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
        test_fetch_svr_info4
        test_fetch_svr_info3
        test_fetch_svr_info2
        test_fetch_svr_info

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
        self.mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        self.mongo.connect()

    def test_fetch_svr_info4(self):

        """Function:  test_fetch_svr_info4

        Description:  Test fetch_svr_info method.

        Arguments:

        """

        data = self.mongo.fetch_svr_info()
        self.mongo.disconnect()
        build_data = data["buildEnvironment"]

        self.assertTrue(build_data["target_arch"])

    def test_fetch_svr_info3(self):

        """Function:  test_fetch_svr_info3

        Description:  Test fetch_svr_info method.

        Arguments:

        """

        data = self.mongo.fetch_svr_info()
        self.mongo.disconnect()

        self.assertIsInstance(data["buildEnvironment"], dict)

    def test_fetch_svr_info2(self):

        """Function:  test_fetch_svr_info2

        Description:  Test fetch_svr_info method.

        Arguments:

        """

        data = self.mongo.fetch_svr_info()
        self.mongo.disconnect()

        self.assertIsInstance(data["storageEngines"], list)

    def test_fetch_svr_info(self):

        """Function:  test_fetch_svr_info

        Description:  Test fetch_svr_info method.

        Arguments:

        """

        self.assertIsInstance(self.mongo.fetch_svr_info(), dict)
        self.mongo.disconnect()


if __name__ == "__main__":
    unittest.main()
