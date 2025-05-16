# Classification (U)                                    # pylint:disable=C0302

"""Program:  create_instance_ssl.py

    Description:  Integration testing of create_instance in mongo_libs.py.

    Note:  This is only for testing on SSL connections.

    Usage:
        test/integration/mongo_libs/create_instance_ssl.py

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

    Methods:
        setUp
        test_set_ssl8
        test_set_ssl7
        test_set_ssl6
        test_set_ssl5
        test_set_ssl4
        test_set_ssl3
        test_set_ssl2
        test_set_ssl
        test_none_ssl8
        test_none_ssl7
        test_none_ssl6
        test_none_ssl5
        test_none_ssl4
        test_none_ssl3
        test_none_ssl2
        test_none_ssl

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
        self.ssl_client_ca = self.cfg.ssl_client_ca

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl8(self, mock_load):

        """Function:  test_set_ssl8

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl7(self, mock_load):

        """Function:  test_set_ssl7

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl6(self, mock_load):

        """Function:  test_set_ssl6

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl5(self, mock_load):

        """Function:  test_set_ssl5

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl4(self, mock_load):

        """Function:  test_set_ssl4

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl3(self, mock_load):

        """Function:  test_set_ssl3

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl2(self, mock_load):

        """Function:  test_set_ssl2

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl(self, mock_load):

        """Function:  test_set_ssl

        Description:  Test Server class with SSL attribute set.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl8(self, mock_load):

        """Function:  test_none_ssl8

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl7(self, mock_load):

        """Function:  test_none_ssl7

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl6(self, mock_load):

        """Function:  test_none_ssl6

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl5(self, mock_load):

        """Function:  test_none_ssl5

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl4(self, mock_load):

        """Function:  test_none_ssl4

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl3(self, mock_load):

        """Function:  test_none_ssl3

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl2(self, mock_load):

        """Function:  test_none_ssl2

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl(self, mock_load):

        """Function:  test_none_ssl

        Description:  Test Server class with SSL attribute set to none.

        Arguments:

        """

        mock_load.return_value = self.cfg
        tmp = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = None
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        self.ssl_client_ca = tmp

        self.assertIsNone(mongo.ssl_client_ca)


if __name__ == "__main__":
    unittest.main()
