# Classification (U)

"""Program:  server_fetch_adr.py

    Description:  Integration testing of Server.fetch_adr in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_fetch_adr.py

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
        test_fetch_adr2
        test_fetch_adr

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
        self.results = (self.cfg.host, self.cfg.port)

    def test_fetch_adr2(self):

        """Function:  test_fetch_adr2

        Description:  Test fetch_adr method.

        Arguments:

        """

        self.assertTrue(isinstance(self.mongo.fetch_adr(), tuple))

    def test_fetch_adr(self):

        """Function:  test_fetch_adr

        Description:  Test fetch_adr method.

        Arguments:

        """

        self.assertEqual(self.mongo.fetch_adr(), self.results)


if __name__ == "__main__":
    unittest.main()
