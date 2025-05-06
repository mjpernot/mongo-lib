# Classification (U)

"""Program:  crt_coll_inst_ssl.py

    Description:  Integration testing of crt_coll_inst in mongo_libs.py.

    Note:  This is only for testing on SSL connections.

    Usage:
        test/integration/mongo_libs/crt_coll_inst_ssl.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_libs                           # pylint:disable=E0401,C0413
import mongo_class                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_auth_type_ssl
        test_auth_type_none
        test_coll_set_ssl
        test_rep_set_ssl
        test_coll_none_ssl
        test_rep_none_ssl

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
        self.dbn = "admin"
        self.coll = "system.users"

    def test_auth_type_ssl(self):

        """Function:  test_auth_type_ssl

        Description:  Test with auth_type set to SSL.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.auth_type, self.cfg.auth_type)

    def test_auth_type_none(self):

        """Function:  test_auth_type_none

        Description:  Test with auth_type set to None.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.auth_type, "SSL")

    def test_coll_set_ssl(self):

        """Function:  test_coll_set_ssl

        Description:  Test mongo_class.Coll class with SSL set.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.ssl_client_ca, self.cfg.ssl_client_ca)

    def test_rep_set_ssl(self):

        """Function:  test_rep_set_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set.

        Arguments:

        """

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.ssl_client_ca, self.cfg.ssl_client_ca)

    def test_coll_none_ssl(self):

        """Function:  test_coll_none_ssl

        Description:  Test mongo_class.Coll class with SSL set to none.

        Arguments:

        """

        self.cfg.repset_hosts = None
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)
        self.cfg.ssl_client_ca = tmp

        self.assertFalse(mongo.ssl_client_ca)

    def test_rep_none_ssl(self):

        """Function:  test_rep_none_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set to none.

        Arguments:

        """

        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)
        self.cfg.ssl_client_ca = tmp

        self.assertFalse(mongo.ssl_client_ca)


if __name__ == "__main__":
    unittest.main()
