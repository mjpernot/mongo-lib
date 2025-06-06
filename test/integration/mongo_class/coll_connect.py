# Classification (U)

"""Program:  coll_connect.py

    Description:  Integration testing of Coll.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/coll_connect.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class                              # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_miss_coll_coll2
        test_miss_coll_coll
        test_fail_get_srv_attr2
        test_fail_get_srv_attr
        test_auth
        test_no_auth2
        test_no_auth
        test_fail_connection2
        test_fail_connection
        test_connection2
        test_connection

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
        self.database = "admin"
        self.coll = "system.users"
        self.errmsg = "Error:  Server not detected."
        self.errmsg2 = "Error:  Unable to connect, no collection passed."

    def test_miss_coll_coll2(self):

        """Function:  test_miss_coll_coll2

        Description:  Test with no Collection passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.connect()

        self.assertFalse(mongo.coll)
        mongo.disconnect()

    def test_miss_coll_coll(self):

        """Function:  test_miss_coll_coll

        Description:  Test with no Collection passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertEqual(mongo.connect(), (False, self.errmsg2))
        mongo.disconnect()

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.connect()

        self.assertFalse(mongo.coll)

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertFalse(mongo.connect()[0])

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with auth present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertFalse(mongo.connect()[0])

    def test_fail_connection2(self):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        mongo.connect()

        self.assertFalse(mongo.coll)

    def test_fail_connection(self):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertFalse(mongo.connect()[0])

    def test_connection2(self):

        """Function:  test_connection2

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertIsNone(mongo.coll)

    def test_connection(self):

        """Function:  test_connection

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, coll=self.coll,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()


if __name__ == "__main__":
    unittest.main()
