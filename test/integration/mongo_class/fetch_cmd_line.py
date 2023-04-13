# Classification (U)

"""Program:  fetch_cmd_line.py

    Description:  Integration testing of fetch_cmd_line in mongo_class.py.

    Usage:
        test/integration/mongo_class/fetch_cmd_line.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_cmd_line2
        test_fetch_cmd_line

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

    def test_fetch_cmd_line2(self):

        """Function:  test_fetch_cmd_line2

        Description:  Test fetch_cmd_line method.

        Arguments:

        """

        data = mongo_class.fetch_cmd_line(self.mongo)

        self.assertTrue("mongod" in data["argv"])

    def test_fetch_cmd_line(self):

        """Function:  test_fetch_cmd_line

        Description:  Test fetch_cmd_line method.

        Arguments:

        """

        data = mongo_class.fetch_cmd_line(self.mongo)

        self.assertTrue(isinstance(data, dict))


if __name__ == "__main__":
    unittest.main()
