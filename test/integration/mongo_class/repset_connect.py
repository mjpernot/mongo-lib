#!/usr/bin/python
# Classification (U)

"""Program:  repset_connect.py

    Description:  Integration testing of RepSet.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/repset_connect.py

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
import pymongo

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
        setUp
        test_fail_get_srv_attr
        test_no_repset
        test_repset
        test_auth
        test_no_auth2
        test_no_auth
        test_conn_true2
        test_conn_true
        test_conn_false2
        test_conn_false
        test_connections_passed2
        test_connections_passed
        test_no_conn_list3
        test_no_conn_list2
        test_no_conn_list1
        test_no_conn_list

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

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_no_repset(self):

        """Function:  test_no_repset

        Description:  Test with no repset present.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))

    def test_repset(self):

        """Function:  test_repset

        Description:  Test with repset present.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with auth.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no authenication set.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect()

        self.assertFalse(mongo.auth)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no authenication set.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))

    def test_conn_true2(self):

        """Function:  test_conn_true2

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect()
        mongo.connect()

        self.assertTrue(mongo.auth)

    def test_conn_true(self):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect()

        self.assertEqual(mongo.connect(), (True, None))

    def test_conn_false2(self):

        """Function:  test_conn_false2

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect()

        self.assertTrue(isinstance(mongo.conn, pymongo.MongoClient))

    def test_conn_false(self):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))

    def test_connections_passed2(self):

        """Function:  test_connections_passed2

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect(connections=self.cfg.repset_hosts)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, None))

    def test_connections_passed(self):

        """Function:  test_connections_passed

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(connections=self.cfg.repset_hosts),
                         (True, None))

    def test_no_conn_list3(self):

        """Function:  test_no_conn_list3

        Description:  Test no connections passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.repset_hosts))

    def test_no_conn_list2(self):

        """Function:  test_no_conn_list2

        Description:  Test no connections passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_conn_list1(self):

        """Function:  test_no_conn_list2

        Description:  Test with no connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, None))

    def test_no_conn_list(self):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
