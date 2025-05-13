# Classification (U)

"""Program:  server_upd_server_attr.py

    Description:  Integration testing of Server.upd_server_attr in
        mongo_class.py.

    Usage:
        test/integration/mongo_class/server_upd_server_attr.py

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
        test_base_attr
        test_no_conf_file
        test_conf_file

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
        self.conf_file = "/path/conf_file"

    def test_base_attr(self):

        """Function:  test_base_attr

        Description:  Test base attributes.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.upd_server_attr()

        self.assertTrue(self.mongo.db_path and self.mongo.log_path)
        self.mongo.disconnect()

    def test_no_conf_file(self):

        """Function:  test_no_conf_file

        Description:  Test with no conf_file present.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.upd_server_attr()

        self.assertTrue(self.mongo.conf_file)
        self.mongo.disconnect()

    def test_conf_file(self):

        """Function:  test_conf_file

        Description:  Test with conf_file present.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.conf_file = self.conf_file
        self.mongo.upd_server_attr()

        self.assertEqual(self.mongo.conf_file, self.conf_file)
        self.mongo.disconnect()


if __name__ == "__main__":
    unittest.main()
