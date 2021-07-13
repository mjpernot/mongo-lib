#!/usr/bin/python
# Classification (U)

"""Program:  crt_coll_inst.py

    Description:  Integration testing of crt_coll_inst in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/crt_coll_inst.py

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
        setUp
        test_coll_set_ssl
        test_rep_set_ssl
        test_coll_none_ssl
        test_rep_none_ssl
        test_coll_auth_mech3
        test_coll_auth_mech2
        test_coll_auth_mech
        test_repset_auth_mech3
        test_repset_auth_mech2
        test_repset_auth_mech
        test_auth_db_coll2
        test_auth_db_coll
        test_auth_db_repsetcoll2
        test_auth_db_repsetcoll
        test_use_uri_coll2
        test_use_uri_coll
        test_use_uri_repsetcoll2
        test_use_uri_repsetcoll
        test_use_arg_coll2
        test_use_arg_coll
        test_use_arg_repsetcoll2
        test_use_arg_repsetcoll
        test_coll2
        test_coll
        test_repsetcoll2
        test_repsetcoll

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

    def test_coll_auth_mech3(self):

        """Function:  test_coll_auth_mech3

        Description:  Test with authentication mechanism - MONGODB-CR.

        Arguments:

        """

        self.cfg.repset_hosts = None
        self.cfg.auth_mech = "MONGODB-CR"
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual((mongo.auth_db, mongo.auth_mech),
                         (self.cfg.auth_db, self.cfg.auth_mech))

    def test_coll_auth_mech2(self):

        """Function:  test_coll_auth_mech2

        Description:  Test with authentication mechanism.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_coll_auth_mech(self):

        """Function:  test_coll_auth_mech

        Description:  Test with authentication mechanism.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual((mongo.auth_db, mongo.auth_mech),
                         (self.cfg.auth_db, self.cfg.auth_mech))

    def test_repset_auth_mech3(self):

        """Function:  test_repset_auth_mech3

        Description:  Test with authentication mechanism - MONGODB-CR.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.cfg.auth_mech = "MONGODB-CR"

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual((mongo.auth_db, mongo.auth_mech),
                         (self.cfg.auth_db, self.cfg.auth_mech))

    def test_repset_auth_mech2(self):

        """Function:  test_repset_auth_mech2

        Description:  Test with authentication mechanism.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_repset_auth_mech(self):

        """Function:  test_repset_auth_mech

        Description:  Test with authentication mechanism.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual((mongo.auth_db, mongo.auth_mech),
                         (self.cfg.auth_db, self.cfg.auth_mech))

    def test_auth_db_coll2(self):

        """Function:  test_auth_db_coll2

        Description:  Test mongo_class.Coll using auth_db attr.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_auth_db_coll(self):

        """Function:  test_auth_db_coll

        Description:  Test mongo_class.Coll using auth_db attr.

        Arguments:

        """

        self.cfg.auth_db = "test"

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, "test"))

    def test_auth_db_repsetcoll2(self):

        """Function:  test_auth_db_repsetcoll2

        Description:  Test mongo_class.RepSetColl using auth_db attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.cfg.auth_db = "test"

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_auth_db_repsetcoll(self):

        """Function:  test_auth_db_repsetcoll

        Description:  Test mongo_class.RepSetColl using auth_db attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.cfg.auth_db = "test"

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.auth_db),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, "test"))

    def test_use_uri_coll2(self):

        """Function:  test_use_uri_coll2

        Description:  Test mongo_class.Coll using use_uri attr.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True
        self.cfg.repset_hosts = None

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_use_uri_coll(self):

        """Function:  test_use_uri_coll

        Description:  Test mongo_class.Coll using use_uri attr.

        Arguments:

        """

        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, True))

    def test_use_uri_repsetcoll2(self):

        """Function:  test_use_uri_repsetcoll2

        Description:  Test mongo_class.RepSetColl using use_uri attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_use_uri_repsetcoll(self):

        """Function:  test_use_uri_repsetcoll

        Description:  Test mongo_class.RepSetColl using use_uri attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.cfg.use_arg = False
        self.cfg.use_uri = True

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, True))

    def test_use_arg_coll2(self):

        """Function:  test_use_arg_coll2

        Description:  Test mongo_class.Coll using use_arg attr.

        Arguments:

        """

        self.cfg.repset_hosts = None

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_use_arg_coll(self):

        """Function:  test_use_arg_coll

        Description:  Test mongo_class.Coll using use_arg attr.

        Arguments:

        """

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, True))

    def test_use_arg_repsetcoll2(self):

        """Function:  test_use_arg_repsetcoll2

        Description:  Test mongo_class.RepSetColl using use_arg attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_use_arg_repsetcoll(self):

        """Function:  test_use_arg_repsetcoll

        Description:  Test mongo_class.RepSetColl using use_arg attr.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file, mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file, True))

    def test_coll2(self):

        """Function:  test_coll2

        Description:  Test the mongo_class.Coll class.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.Coll))

    def test_coll(self):

        """Function:  test_coll

        Description:  Test the mongo_class.Coll class.

        Arguments:

        """

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))

    def test_repsetcoll2(self):

        """Function:  test_repsetcoll2

        Description:  Test the mongo_class.RepSetColl class.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertTrue(isinstance(mongo, mongo_class.RepSetColl))

    def test_repsetcoll(self):

        """Function:  test_repsetcoll

        Description:  Test the mongo_class.RepSetColl class.

        Arguments:

        """

        self.cfg.repset_hosts = self.cfg.host + ":" + str(self.cfg.port)

        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.auth, self.cfg.conf_file))


if __name__ == "__main__":
    unittest.main()
