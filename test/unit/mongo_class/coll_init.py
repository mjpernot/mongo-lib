#!/usr/bin/python
# Classification (U)

"""Program:  coll_init.py

    Description:  Unit testing of Coll.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/coll_init.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_coll_attr -> Test coll attribute.
        test_no_coll_db_attr -> Test no coll_db attribute passed.
        test_coll_db_attr -> Test coll_db attribute passed.
        test_no_coll_coll_attr -> Test no coll_col attribute passed.
        test_coll_coll_attr -> Test coll_col attribute passed.
        test_no_conf_file_attr -> Test no conf_file attribute passed.
        test_conf_file_attr -> Test conf_file attribute passed.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_no_auth_db -> Test using no auth_db attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_no_using_arg -> Test with auth and no arg present.
        test_using_arg -> Test with auth and arg present.
        test_no_auth_uri -> Test with auth and no uri present.
        test_auth_uri -> Test with auth and uri present.
        test_auth_false -> Test with auth passed as False.
        test_auth_true -> Test with auth passed as True.
        test_no_auth -> Test with no auth present.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        key1 = "pass"
        key2 = "word"
        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = "coll_name"
        self.db_auth = None
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.config = {key1 + key2: self.japd}
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config file"
        self.coll_db = "MyDatabase"

    def test_coll_attr(self):

        """Function:  test_coll_attr

        Description:  Test coll attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.coll)

    def test_no_coll_db_attr(self):

        """Function:  test_no_coll_db_attr

        Description:  Test no coll_db attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertEqual(mongo.coll_db, "test")

    def test_coll_db_attr(self):

        """Function:  test_coll_db_attr

        Description:  Test coll_db attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            db=self.coll_db)

        self.assertEqual(mongo.coll_db, self.coll_db)

    def test_no_coll_coll_attr(self):

        """Function:  test_no_coll_coll_attr

        Description:  Test no coll_col attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.coll_coll)

    def test_coll_coll_attr(self):

        """Function:  test_coll_coll_attr

        Description:  Test coll_col attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertEqual(mongo.coll_coll, self.coll)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertEqual(mongo.config, self.config)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll)

        self.assertFalse(mongo.use_uri)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth passed as False.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, auth=False)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.coll_db, mongo.coll_coll, mongo.auth),
            (self.name, self.user, self.japd, self.host, self.port, self.dbs,
             self.coll, False))

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth passed as True.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, auth=True)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.coll_db, mongo.coll_coll, mongo.auth),
            (self.name, self.user, self.japd, self.host, self.port, self.dbs,
             self.coll, True))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd,
                                 self.host, self.port, coll=self.coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.coll_db, mongo.coll_coll),
            (self.name, self.user, self.japd, self.host, self.port, self.dbs,
             self.coll))


if __name__ == "__main__":
    unittest.main()
