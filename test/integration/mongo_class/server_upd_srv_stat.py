# Classification (U)

"""Program:  server_upd_srv_stat.py

    Description:  Integration testing of Server.upd_srv_stat in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_upd_srv_stat.py

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
        test_decision_attr
        test_derived_attr
        test_base_attr

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

    def test_decision_attr(self):

        """Function:  test_decision_attr

        Description:  Test decision based attributes.

        Arguments:

        """

        self.mongo.upd_srv_stat()

        self.assertTrue(self.mongo.max_mem > 0 or self.mongo.prct_mem > 0)

    def test_derived_attr(self):

        """Function:  test_derived_attr

        Description:  Test derived attributes.

        Arguments:

        """

        self.mongo.upd_srv_stat()

        self.assertTrue(self.mongo.max_conn > 0 and self.mongo.days_up >= 0)

    def test_base_attr(self):

        """Function:  test_base_attr

        Description:  Test base attributes.

        Arguments:

        """

        self.mongo.upd_srv_stat()

        self.assertTrue(self.mongo.uptime > 0 and self.mongo.cur_conn > 0)


if __name__ == "__main__":
    unittest.main()
