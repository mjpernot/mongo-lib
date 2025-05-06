# Classification (U)

"""Program:  crt_coll_inst.py

    Description:  Integration testing of crt_coll_inst in mongo_libs.py.

    Note:  This is only for testing on TLS connections.

    Usage:
        test/integration/mongo_libs/crt_coll_inst_tls.py

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
        test_set_tls_ca_certs
        test_auth_type_tls

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

    def test_set_tls_ca_certs(self):

        """Function:  test_set_tls_ca_certs

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.tls_ca_certs, self.cfg.tls_ca_certs)

    def test_auth_type_tls(self):

        """Function:  test_auth_type_tls

        Description:  Test with auth_type set to TLS.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(mongo.auth_type, self.cfg.auth_type)


if __name__ == "__main__":
    unittest.main()
