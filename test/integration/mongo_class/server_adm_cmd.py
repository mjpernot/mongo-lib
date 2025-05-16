# Classification (U)

"""Program:  server_adm_cmd.py

    Description:  Integration testing of Server.adm_cmd in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_adm_cmd.py

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
        test_arg2
        test_arg
        test_adm_cmd

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

    def test_arg1(self):

        """Function:  test_arg1

        Description:  Test with argument passed.

        Arguments:

        """

        data = self.mongo.adm_cmd("getLog", arg1="global")
        self.mongo.disconnect()

        self.assertIsInstance(data["log"], list)

    def test_arg(self):

        """Function:  test_arg

        Description:  Test with argument passed.

        Arguments:

        """

        data = self.mongo.adm_cmd("getLog", arg1="global")
        self.mongo.disconnect()

        self.assertGreaterEqual(data["totalLinesWritten"], 0)

    def test_adm_cmd(self):

        """Function:  test_adm_cmd

        Description:  Test adm_cmd method.

        Arguments:

        """

        data = self.mongo.adm_cmd("listDatabases")
        self.mongo.disconnect()
        db_list = [item["name"] for item in data["databases"]]

        self.assertIn("admin", db_list)


if __name__ == "__main__":
    unittest.main()
