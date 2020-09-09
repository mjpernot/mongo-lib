#!/usr/bin/python
# Classification (U)

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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs
import mongo_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_auth_db_repsetcoll2 -> Test RepSetColl class w/ auth_db attribute.
        test_auth_db_repsetcoll -> Test RepSetColl class w/ auth_db attribute.
        test_auth_db_repset2 -> Test RepSet class with auth_db attribute.
        test_auth_db_repset -> Test RepSet class with auth_db attribute.
        test_auth_db_coll2 -> Test Coll class with auth_db attribute.
        test_auth_db_coll -> Test Coll class with auth_db attribute.
        test_auth_db_db2 -> Test DB class with auth_db attribute.
        test_auth_db_db -> Test DB class with auth_db attribute.
        test_auth_db_slaverep2 -> Test SlaveRep class with auth_db attribute.
        test_auth_db_slaverep -> Test SlaveRep class with auth_db attribute.
        test_auth_db_masterrep2 -> Test MasterRep class with auth_db attribute.
        test_auth_db_masterrep -> Test MasterRep class with auth_db attribute.
        test_auth_db_rep2 -> Test Rep class with auth_db attribute.
        test_auth_db_rep -> Test Rep class with auth_db attribute.
        test_auth_db_server2 -> Test Server class with auth_db attribute.
        test_auth_db_server -> Test Server class with auth_db attribute.
        test_use_uri_repsetcoll2 -> Test RepSetColl class w/ use_uri attribute.
        test_use_uri_repsetcoll -> Test RepSetColl class w/ use_uri attribute.
        test_use_uri_repset2 -> Test RepSet class with use_uri attribute.
        test_use_uri_repset -> Test RepSet class with use_uri attribute.
        test_use_uri_coll2 -> Test Coll class with use_uri attribute.
        test_use_uri_coll -> Test Coll class with use_uri attribute.
        test_use_uri_db2 -> Test DB class with use_uri attribute.
        test_use_uri_db -> Test DB class with use_uri attribute.
        test_use_uri_slaverep2 -> Test SlaveRep class with use_uri attribute.
        test_use_uri_slaverep -> Test SlaveRep class with use_uri attribute.
        test_use_uri_masterrep2 -> Test MasterRep class with use_uri attribute.
        test_use_uri_masterrep -> Test MasterRep class with use_uri attribute.
        test_use_uri_rep2 -> Test Rep class with use_uri attribute.
        test_use_uri_rep -> Test Rep class with use_uri attribute.
        test_use_uri_server2 -> Test Server class with use_uri attribute.
        test_use_uri_server -> Test Server class with use_uri attribute.
        test_use_arg_repsetcoll2 -> Test RepSetColl class w/ use_arg attribute.
        test_use_arg_repsetcoll -> Test RepSetColl class w/ use_arg attribute.
        test_use_arg_repset2 -> Test RepSet class with use_arg attribute.
        test_use_arg_repset -> Test RepSet class with use_arg attribute.
        test_use_arg_coll2 -> Test Coll class with use_arg attribute.
        test_use_arg_coll -> Test Coll class with use_arg attribute.
        test_use_arg_db2 -> Test DB class with use_arg attribute.
        test_use_arg_db -> Test DB class with use_arg attribute.
        test_use_arg_slaverep2 -> Test SlaveRep class with use_arg attribute.
        test_use_arg_slaverep -> Test SlaveRep class with use_arg attribute.
        test_use_arg_masterrep2 -> Test MasterRep class with use_arg attribute.
        test_use_arg_masterrep -> Test MasterRep class with use_arg attribute.
        test_use_arg_rep2 -> Test Rep class with use_arg attribute.
        test_use_arg_rep -> Test Rep class with use_arg attribute.
        test_use_arg_server2 -> Test Server class with use_arg attribute.
        test_use_arg_server -> Test Server class with use_arg attribute.
        test_create_repsetcoll2 -> Test creating RepSetColl class instance.
        test_create_repsetcoll -> Test creating RepSetColl class instance.
        test_create_repset2 -> Test creating RepSet class instance.
        test_create_repset -> Test creating RepSet class instance.
        test_create_coll2 -> Test creating Coll class instance.
        test_create_coll -> Test creating Coll class instance.
        test_create_db2 -> Test creating DB class instance.
        test_create_db -> Test creating DB class instance.
        test_create_slaverep2 -> Test creating SlaveRep class instance.
        test_create_slaverep -> Test creating SlaveRep class instance.
        test_create_masterrep2 -> Test creating MasterRep class instance.
        test_create_masterrep -> Test creating MasterRep class instance.
        test_create_rep2 -> Test creating Rep class instance.
        test_create_rep -> Test creating Rep class instance.
        test_create_server2 -> Test creating Server class instance.
        test_create_server -> Test creating Server class instance.

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

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

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

        self.assertTrue(isinstance(mongo, mongo_class.RepSet))

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

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

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

        self.assertTrue(isinstance(mongo, mongo_class.DB))

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

        self.assertTrue(isinstance(mongo, mongo_class.SlaveRep))

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

        self.assertTrue(isinstance(mongo, mongo_class.MasterRep))

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

        self.assertTrue(isinstance(mongo, mongo_class.Rep))

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

        self.assertTrue(isinstance(mongo, mongo_class.Server))

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

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_repsetcoll2(self, mock_load):

        """Function:  test_use_uri_repsetcoll2

        Description:  Test RepSetColl class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_repsetcoll(self, mock_load):

        """Function:  test_use_uri_repsetcoll

        Description:  Test RepSetColl class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_repset2(self, mock_load):

        """Function:  test_use_uri_repset2

        Description:  Test RepSet class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertTrue(isinstance(mongo, mongo_class.RepSet))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_repset(self, mock_load):

        """Function:  test_use_uri_repset

        Description:  Test RepSet class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_coll2(self, mock_load):

        """Function:  test_use_uri_coll2

        Description:  Test Coll class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_coll(self, mock_load):

        """Function:  test_use_uri_coll

        Description:  Test Coll class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_db2(self, mock_load):

        """Function:  test_use_uri_db2

        Description:  Test DB class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertTrue(isinstance(mongo, mongo_class.DB))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_db(self, mock_load):

        """Function:  test_use_uri_db

        Description:  Test DB class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_slaverep2(self, mock_load):

        """Function:  test_use_uri_slaverep2

        Description:  Test SlaveRep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertTrue(isinstance(mongo, mongo_class.SlaveRep))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_slaverep(self, mock_load):

        """Function:  test_use_uri_slaverep

        Description:  Test SlaveRep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_masterrep2(self, mock_load):

        """Function:  test_use_uri_masterrep2

        Description:  Test MasterRep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertTrue(isinstance(mongo, mongo_class.MasterRep))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_masterrep(self, mock_load):

        """Function:  test_use_uri_masterrep

        Description:  Test MasterRep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_rep2(self, mock_load):

        """Function:  test_use_uri_rep2

        Description:  Test Rep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertTrue(isinstance(mongo, mongo_class.Rep))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_rep(self, mock_load):

        """Function:  test_use_uri_rep2

        Description:  Test Rep class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_server2(self, mock_load):

        """Function:  test_use_uri_server2

        Description:  Test Server class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertTrue(isinstance(mongo, mongo_class.Server))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_use_uri_server(self, mock_load):

        """Function:  test_use_uri_server

        Description:  Test Server class with use_uri attribute.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mock_load.return_value = self.cfg

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             True))

    def test_use_arg_repsetcoll2(self):

        """Function:  test_use_arg_repsetcoll2

        Description:  Test RepSetColl class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_use_arg_repsetcoll(self):

        """Function:  test_use_arg_repsetcoll

        Description:  Test RepSetColl class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_repset2(self):

        """Function:  test_use_arg_repset2

        Description:  Test RepSet class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertTrue(isinstance(mongo, mongo_class.RepSet))

    def test_use_arg_repset(self):

        """Function:  test_use_arg_repset

        Description:  Test RepSet class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSet)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_coll2(self):

        """Function:  test_use_arg_coll2

        Description:  Test Coll class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_use_arg_coll(self):

        """Function:  test_use_arg_coll

        Description:  Test Coll class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_db2(self):

        """Function:  test_use_arg_db2

        Description:  Test DB class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertTrue(isinstance(mongo, mongo_class.DB))

    def test_use_arg_db(self):

        """Function:  test_use_arg_db

        Description:  Test DB class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.DB)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_slaverep2(self):

        """Function:  test_use_arg_slaverep2

        Description:  Test SlaveRep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertTrue(isinstance(mongo, mongo_class.SlaveRep))

    def test_use_arg_slaverep(self):

        """Function:  test_use_arg_slaverep

        Description:  Test SlaveRep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.SlaveRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_masterrep2(self):

        """Function:  test_use_arg_masterrep2

        Description:  Test MasterRep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertTrue(isinstance(mongo, mongo_class.MasterRep))

    def test_use_arg_masterrep(self):

        """Function:  test_use_arg_masterrep

        Description:  Test MasterRep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_rep2(self):

        """Function:  test_use_arg_rep2

        Description:  Test Rep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertTrue(isinstance(mongo, mongo_class.Rep))

    def test_use_arg_rep(self):

        """Function:  test_use_arg_rep2

        Description:  Test Rep class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Rep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_use_arg_server2(self):

        """Function:  test_use_arg_server2

        Description:  Test Server class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertTrue(isinstance(mongo, mongo_class.Server))

    def test_use_arg_server(self):

        """Function:  test_use_arg_server

        Description:  Test Server class with use_arg attribute.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file,
             self.cfg.use_arg))

    def test_create_repsetcoll2(self):

        """Function:  test_create_repsetcoll2

        Description:  Test creating RepSetColl class instance.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.RepSetColl)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

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

        self.assertTrue(isinstance(mongo, mongo_class.RepSet))

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

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

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

        self.assertTrue(isinstance(mongo, mongo_class.DB))

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

        self.assertTrue(isinstance(mongo, mongo_class.SlaveRep))

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

        self.assertTrue(isinstance(mongo, mongo_class.MasterRep))

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

        self.assertTrue(isinstance(mongo, mongo_class.Rep))

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

        self.assertTrue(isinstance(mongo, mongo_class.Server))

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
