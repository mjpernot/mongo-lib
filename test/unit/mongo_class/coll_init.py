#!/usr/bin/python
# Classification (U)

"""Program:  Coll_init.py

    Description:  Unit testing of Coll.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_init.py

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
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_using_arg -> Test with auth and arg present.
        test_auth_uri -> Test with auth and uri present.
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

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.Coll(
            self.name, self.user, self.japd, self.host, self.port,
            coll=self.coll, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

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
