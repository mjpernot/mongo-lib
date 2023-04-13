# Classification (U)

"""Program:  server_get_server_attr.py

    Description:  Integration testing of Server.get_server_attr in
        mongo_class.py.

    Usage:
        test/integration/mongo_class/server_get_server_attr.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import pymongo

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
        test_login_fail
        test_connect

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

    def test_login_fail(self):

        """Function:  test_login_fail

        Description:  Test with login failure.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg
        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.conn = pymongo.MongoClient(
            mongo.conn_list, username=mongo.user, authSource=mongo.auth_db,
            **mongo.config)

        self.assertEqual(mongo.get_srv_attr(), (False, errmsg))

    def test_connect(self):

        """Function:  test_connect

        Description:  Test with successful connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.conn = pymongo.MongoClient(
            mongo.conn_list, username=mongo.user, authSource=mongo.auth_db,
            **mongo.config)

        self.assertEqual(mongo.get_srv_attr(), (True, None))


if __name__ == "__main__":
    unittest.main()
