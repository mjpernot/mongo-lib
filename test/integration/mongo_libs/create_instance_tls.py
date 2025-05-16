# Classification (U)                            # pylint:disable=C0302

"""Program:  create_instance_tls.py

    Description:  Integration testing of create_instance in mongo_libs.py.

    Note:  This is only for testing on TLS connections.

    Usage:
        test/integration/mongo_libs/create_instance_tls.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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

    Note:  Some of the tests will fail depending whether SSL or TLS is being
        used.

    Methods:
        setUp
        test_set_tls8
        test_set_tls7
        test_set_tls6
        test_set_tls5
        test_set_tls4
        test_set_tls3
        test_set_tls2
        test_set_tls

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.auth_mech = "SCRAM-SHA-1"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.tls_ca_certs = self.cfg.tls_ca_certs

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls8(self, mock_load):

        """Function:  test_set_tls8

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.RepSetColl)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls7(self, mock_load):

        """Function:  test_set_tls7

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.RepSet)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls6(self, mock_load):

        """Function:  test_set_tls6

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.SlaveRep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls5(self, mock_load):

        """Function:  test_set_tls5

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.MasterRep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls4(self, mock_load):

        """Function:  test_set_tls4

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.Rep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls3(self, mock_load):

        """Function:  test_set_tls3

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.Coll)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls2(self, mock_load):

        """Function:  test_set_tls2

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.DB)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls(self, mock_load):

        """Function:  test_set_tls

        Description:  Test Server class with TLS attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            self.config_name, self.config_dir, mongo_class.Server)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)


if __name__ == "__main__":
    unittest.main()
