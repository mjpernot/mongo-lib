#!/usr/bin/python
# Classification (U)

"""Program:  db_connect.py

    Description:  Integration testing of DB.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_connect.py

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
import mongo_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fail_get_srv_attr2 -> Test with failed get_srv_attr call.
        test_fail_get_srv_attr -> Test with failed get_srv_attr call.
        test_auth_arg2 -> Test with auth and arg present.
        test_auth_arg -> Test with auth and arg present.
        test_auth_uri2 -> Test with auth and uri present.
        test_auth_uri -> Test with auth and uri present.
        test_no_auth2 -> Test with no auth present.
        test_no_auth -> Test with no auth present.
        test_fail_connection2 -> Test with failed connection.
        test_fail_connection -> Test with failed connection.
        test_connection2 -> Test connection method.
        test_connection -> Test connection method.

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
        self.failure = "Authentication failed."
        self.ermsg = "Error:  Auth flag or login params is incorrect: %s"
        

    def test_db_attr2(self):

        """Function:  test_db_attr2

        Description:  Test db attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_db_attr(self):

        """Function:  test_db_attr

        Description:  Test db attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(mongo.db)

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = self.failure
        errmsg = self.ermsg % msg

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertFalse(mongo.db)

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = self.failure
        errmsg = self.ermsg % msg

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_auth_arg2(self):

        """Function:  test_auth_arg2

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_auth_arg(self):

        """Function:  test_auth_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.use_arg))

    def test_auth_uri2(self):

        """Function:  test_auth_uri2

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=False, auth_db=True, conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.use_uri))

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=False, auth_db=True, conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
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

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_fail_connection2(self):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)
        mongo.connect()

        self.assertFalse(mongo.db)

    def test_fail_connection(self):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        msg = self.failure
        errmsg = self.ermsg % msg

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_connection2(self):

        """Function:  test_connection2

        Description:  Test connection method.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)

        self.assertEqual(mongo.connect(), (True, None))

    def test_connection(self):

        """Function:  test_connection

        Description:  Test connection method.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)
        mongo.connect()

        self.assertEqual(mongo.db_name, self.database)


if __name__ == "__main__":
    unittest.main()
