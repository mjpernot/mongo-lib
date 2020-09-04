#!/usr/bin/python
# Classification (U)

"""Program:  repsetcoll_connect.py

    Description:  Integration testing of RepSetColl.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/repsetcoll_connect.py

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
        setUp -> Initialize testing environment.
        test_auth_false -> Test with auth set to false.
        test_fail_get_srv_attr2 -> Test with failed get_srv_attr call.
        test_fail_get_srv_attr -> Test with failed get_srv_attr call.
        test_auth_true2 -> Test with auth set to true.
        test_auth_true -> Test with auth set to true.
        test_no_auth2 -> Test with auth set to false.
        test_no_auth -> Test with auth set to false.
        test_conn_false2 -> Test with conn set to false.
        test_conn_false -> Test with conn set to false.
        test_conn_true2 -> Test with conn set to true.
        test_conn_true -> Test with conn set to true.
        test_connections_passed2 -> Test with connections passed.
        test_connections_passed -> Test with connections passed.
        test_no_conn_list3 -> Test no conn_list passed, set by repset_hosts.
        test_no_conn_list2 -> Test no conn_list passed, set by repset_hosts.
        test_no_conn_list1 -> Test with no conn_list passed.
        test_no_conn_list -> Test with no conn_list passed.

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
        self.dbs = "admin"
        self.coll = "system.users"
        self.db_auth = "admin"

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=None, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertFalse(mongo.conn)

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error: Auth flag/login params is incorrect: %s" % msg

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_auth_true2(self):

        """Function:  test_auth_true2

        Description:  Test with auth set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertTrue(mongo.db_auth)

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertTrue(isinstance(mongo.conn, pymongo.MongoClient))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))

    def test_conn_false2(self):

        """Function:  test_conn_false2

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertTrue(isinstance(mongo.conn, pymongo.MongoClient))

    def test_conn_false(self):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))

    def test_conn_true2(self):

        """Function:  test_conn_true2

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()
        mongo.connect()

        self.assertTrue(isinstance(mongo.conn, pymongo.MongoClient))

    def test_conn_true(self):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertEqual(mongo.connect(), (True, None))

    def test_connections_passed2(self):

        """Function:  test_connections_passed2

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

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

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(connections=self.cfg.repset_hosts),
                         (True, None))

    def test_no_conn_list3(self):

        """Function:  test_no_conn_list3

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts, coll=self.coll,
            db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.repset_hosts))

    def test_no_conn_list2(self):

        """Function:  test_no_conn_list2

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts, coll=self.coll,
            db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_conn_list1(self):

        """Function:  test_no_conn_list2

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, None))

    def test_no_conn_list(self):

        """Function:  test_no_conn_list

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
