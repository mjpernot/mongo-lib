#!/usr/bin/python
# Classification (U)

"""Program:  rep_init.py

    Description:  Unit testing of Rep.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/rep_init.py

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
        test_isslave_attr -> Test isslave attribute.
        test_repset_attr -> Test repset attribute.
        test_ismaster_attr -> Test ismaster attribute.
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
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.config = {key1 + key2: self.japd}
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config file"

    def test_isslave_attr(self):

        """Function:  test_isslave_attr

        Description:  Test isslave attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.isslave)

    def test_repset_attr(self):

        """Function:  test_repset_attr

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.repset)

    def test_ismaster_attr(self):

        """Function:  test_ismaster_attr

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.ismaster)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertEqual(mongo.config, self.config)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertFalse(mongo.use_uri)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth passed as False.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, auth=False)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.name, self.user, self.japd, self.host,
                          self.port, False))

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth passed as True.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port, auth=True)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.name, self.user, self.japd, self.host,
                          self.port, True))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port),
                         (self.name, self.user, self.japd, self.host,
                          self.port))


if __name__ == "__main__":
    unittest.main()
