# Classification (U)                                    # pylint:disable=C0302

"""Program:  create_instance.py

    Description:  Integration testing of create_instance in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/create_instance.py

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
        test_auth_mech8
        test_auth_mech7
        test_auth_mech6
        test_auth_mech5
        test_auth_mech4
        test_auth_mech3
        test_auth_mech2
        test_auth_mech
        test_auth_db_repsetcoll2
        test_auth_db_repsetcoll
        test_auth_db_repset2
        test_auth_db_repset
        test_auth_db_coll2
        test_auth_db_coll
        test_auth_db_db2
        test_auth_db_db
        test_auth_db_slaverep2
        test_auth_db_slaverep
        test_auth_db_masterrep2
        test_auth_db_masterrep
        test_auth_db_rep2
        test_auth_db_rep
        test_auth_db_server2
        test_auth_db_server
        test_create_repsetcoll2
        test_create_repsetcoll
        test_create_repset2
        test_create_repset
        test_create_coll2
        test_create_coll
        test_create_db2
        test_create_db
        test_create_slaverep2
        test_create_slaverep
        test_create_masterrep2
        test_create_masterrep
        test_create_rep2
        test_create_rep
        test_create_server2
        test_create_server

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

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech8(self, mock_load):

        """Function:  test_auth_mech8

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech7(self, mock_load):

        """Function:  test_auth_mech7

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech6(self, mock_load):

        """Function:  test_auth_mech6

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech5(self, mock_load):

        """Function:  test_auth_mech5

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech4(self, mock_load):

        """Function:  test_auth_mech4

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech3(self, mock_load):

        """Function:  test_auth_mech3

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech2(self, mock_load):

        """Function:  test_auth_mech2

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_mech(self, mock_load):

        """Function:  test_auth_mech

        Description:  Test Server class with auth_mech attribute.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_repsetcoll2(self, mock_load):

        """Function:  test_auth_db_repsetcoll2

        Description:  Test RepSetColl class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertIsInstance(mongo, mongo_class.RepSetColl)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_repsetcoll(self, mock_load):

        """Function:  test_auth_db_repsetcoll

        Description:  Test RepSetColl class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_repset2(self, mock_load):

        """Function:  test_auth_db_repset2

        Description:  Test RepSet class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertIsInstance(mongo, mongo_class.RepSet)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_repset(self, mock_load):

        """Function:  test_auth_db_repset

        Description:  Test RepSet class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_coll2(self, mock_load):

        """Function:  test_auth_db_coll2

        Description:  Test Coll class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertIsInstance(mongo, mongo_class.Coll)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_coll(self, mock_load):

        """Function:  test_auth_db_coll

        Description:  Test Coll class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_db2(self, mock_load):

        """Function:  test_auth_db_db2

        Description:  Test DB class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertIsInstance(mongo, mongo_class.DB)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_db(self, mock_load):

        """Function:  test_auth_db_db

        Description:  Test DB class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_slaverep2(self, mock_load):

        """Function:  test_auth_db_slaverep2

        Description:  Test SlaveRep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertIsInstance(mongo, mongo_class.SlaveRep)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_slaverep(self, mock_load):

        """Function:  test_auth_db_slaverep

        Description:  Test SlaveRep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_masterrep2(self, mock_load):

        """Function:  test_auth_db_masterrep2

        Description:  Test MasterRep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertIsInstance(mongo, mongo_class.MasterRep)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_masterrep(self, mock_load):

        """Function:  test_auth_db_masterrep

        Description:  Test MasterRep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_rep2(self, mock_load):

        """Function:  test_auth_db_rep2

        Description:  Test Rep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertIsInstance(mongo, mongo_class.Rep)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_rep(self, mock_load):

        """Function:  test_auth_db_rep

        Description:  Test Rep class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_server2(self, mock_load):

        """Function:  test_auth_db_server2

        Description:  Test Server class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertIsInstance(mongo, mongo_class.Server)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_db_server(self, mock_load):

        """Function:  test_auth_db_server

        Description:  Test Server class with auth_db attribute.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             "test"))

    def test_create_repsetcoll2(self):

        """Function:  test_create_repsetcoll2

        Description:  Test creating RepSetColl class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertIsInstance(mongo, mongo_class.RepSetColl)

    def test_create_repsetcoll(self):

        """Function:  test_create_repsetcoll

        Description:  Test creating RepSetColl class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_repset2(self):

        """Function:  test_create_repset2

        Description:  Test creating RepSet class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertIsInstance(mongo, mongo_class.RepSet)

    def test_create_repset(self):

        """Function:  test_create_repset

        Description:  Test creating RepSet class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_coll2(self):

        """Function:  test_create_coll2

        Description:  Test creating Coll class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertIsInstance(mongo, mongo_class.Coll)

    def test_create_coll(self):

        """Function:  test_create_coll

        Description:  Test creating Coll class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_db2(self):

        """Function:  test_create_db2

        Description:  Test creating DB class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertIsInstance(mongo, mongo_class.DB)

    def test_create_db(self):

        """Function:  test_create_db

        Description:  Test creating DB class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_slaverep2(self):

        """Function:  test_create_slaverep2

        Description:  Test creating SlaveRep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertIsInstance(mongo, mongo_class.SlaveRep)

    def test_create_slaverep(self):

        """Function:  test_create_slaverep

        Description:  Test creating SlaveRep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_masterrep2(self):

        """Function:  test_create_masterrep2

        Description:  Test creating MasterRep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertIsInstance(mongo, mongo_class.MasterRep)

    def test_create_masterrep(self):

        """Function:  test_create_masterrep

        Description:  Test creating MasterRep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_rep2(self):

        """Function:  test_create_rep2

        Description:  Test creating Rep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertIsInstance(mongo, mongo_class.Rep)

    def test_create_rep(self):

        """Function:  test_create_rep

        Description:  Test creating Rep class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_create_server2(self):

        """Function:  test_create_server2

        Description:  Test creating Server class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertIsInstance(mongo, mongo_class.Server)

    def test_create_server(self):

        """Function:  test_create_server

        Description:  Test creating Server class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))


if __name__ == "__main__":
    unittest.main()
