#!/usr/bin/python
# Classification (U)

"""Program:  RepSetColl_init.py

    Description:  Unit testing of RepSetColl.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/RepSetColl_init.py

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
        test_auth_db_attr -> Test auth_db attribute passed.
        test_no_auth_db_attr -> Test no auth_db attribute passed.
        test_db_auth_attr -> Test db_auth attribute passed.
        test_no_db_auth_attr -> Test no db_auth attribute passed.
        test_coll_attr -> Test coll attribute passed.
        test_no_coll_attr -> Test no coll attribute passed.
        test_db_attr -> Test db attribute passed.
        test_no_db_attr -> Test no db attribute passed.
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
        self.japwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = "minedb1"
        self.repset = "mongo_repset"
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.mydb = "minedb"
        self.mycoll = "minecollection"
        self.config = {key1 + key2: self.japwd}
        self.conn_list = [self.host + ":" + str(self.port)]

    def test_auth_db_attr(self):

        """Function:  test_auth_db_attr

        Description:  Test auth_db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_auth_db_attr(self):

        """Function:  test_no_auth_db_attr

        Description:  Test no auth_db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.auth_db, "admin")

    def test_db_auth_attr(self):

        """Function:  test_db_auth_attr

        Description:  Test db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, db_auth=self.db_auth)

        self.assertEqual(mongo.db_auth, self.db_auth)

    def test_no_db_auth_attr(self):

        """Function:  test_no_db_auth_attr

        Description:  Test no db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db_auth, None)

    def test_coll_attr(self):

        """Function:  test_coll_attr

        Description:  Test coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, coll=self.mycoll)

        self.assertEqual(mongo.coll, self.mycoll)

    def test_no_coll_attr(self):

        """Function:  test_no_coll_attr

        Description:  Test no coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.coll, None)

    def test_db_attr(self):

        """Function:  test_db_attr

        Description:  Test db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, db=self.mydb)

        self.assertEqual(mongo.db, self.mydb)

    def test_no_db_attr(self):

        """Function:  test_no_db_attr

        Description:  Test no db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db, "test")

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config)

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japwd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port,
             mongo.db, mongo.coll, mongo.repset),
            (self.name, self.user, self.japwd, self.host, self.port, self.dbs,
             self.coll, self.repset))


if __name__ == "__main__":
    unittest.main()
