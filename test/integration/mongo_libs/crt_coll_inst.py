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
        test_auth_type_ssl
        test_auth_type_none
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

        self.assertIsInstance(mongo, mongo_class.Coll)

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

        self.assertIsInstance(mongo, mongo_class.RepSetColl)

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

        self.assertIsInstance(mongo, mongo_class.Coll)

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

        self.assertIsInstance(mongo, mongo_class.RepSetColl)

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

    def test_coll2(self):

        """Function:  test_coll2

        Description:  Test the mongo_class.Coll class.

        Arguments:

        """

        self.cfg.repset_hosts = None
        mongo = mongo_libs.crt_coll_inst(self.cfg, self.dbn, self.coll)

        self.assertIsInstance(mongo, mongo_class.Coll)

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

        self.assertIsInstance(mongo, mongo_class.RepSetColl)

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
