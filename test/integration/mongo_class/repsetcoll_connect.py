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
import unittest
import pymongo

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
        test_db_auth_passed2
        test_db_auth_passed
        test_coll_passed2
        test_coll_passed
        test_db_not_passed2
        test_db_not_passed
        test_db_passed2
        test_db_passed
        test_auth
        test_auth_false
        test_fail_get_srv_attr2
        test_fail_get_srv_attr
        test_auth_true2
        test_auth_true
        test_no_auth2
        test_no_auth
        test_conn_false2
        test_conn_false
        test_conn_true2
        test_conn_true
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
        self.dbs = "admin"
        self.coll = "system.users"
        self.db_auth = "admin"

    def test_db_auth_passed2(self):

        """Function:  test_db_auth_passed2

        Description:  Test with db_auth passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)
        mongo.connect()

        self.assertTrue(mongo.db_auth, self.cfg.auth_db)
        mongo.disconnect()

    def test_db_auth_passed(self):

        """Function:  test_db_auth_passed

        Description:  Test with db_auth passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_coll_passed2(self):

        """Function:  test_coll_passed2

        Description:  Test with coll passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)
        mongo.connect()

        self.assertTrue(mongo.coll, self.coll)
        mongo.disconnect()

    def test_coll_passed(self):

        """Function:  test_coll_passed

        Description:  Test with coll passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_db_not_passed2(self):

        """Function:  test_db_not_passed2

        Description:  Test with db not passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db)
        mongo.connect()

        self.assertEqual(mongo.db_name, "test")
        mongo.disconnect()

    def test_db_not_passed(self):

        """Function:  test_db_not_passed

        Description:  Test with db not passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_db_passed2(self):

        """Function:  test_db_passed2

        Description:  Test with db passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)
        mongo.connect()

        self.assertEqual(mongo.db_name, self.dbs)
        mongo.disconnect()

    def test_db_passed(self):

        """Function:  test_db_passed

        Description:  Test with db passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with auth.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=True, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.cfg.auth_db, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=None, db=self.dbs)

        self.assertFalse(mongo.connect()[0])

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertFalse(mongo.conn)

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertFalse(mongo.connect()[0])

    def test_auth_true2(self):

        """Function:  test_auth_true2

        Description:  Test with auth set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertTrue(mongo.db_auth)
        mongo.disconnect()

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertIsNone(mongo.conn)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with auth set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertFalse(mongo.connect()[0])

    def test_conn_false2(self):

        """Function:  test_conn_false2

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertIsNone(mongo.conn)

    def test_conn_false(self):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertFalse(mongo.connect()[0])

    def test_conn_true2(self):

        """Function:  test_conn_true2

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()
        mongo.connect()

        self.assertIsNone(mongo.conn)

    def test_conn_true(self):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertFalse(mongo.connect()[0])

    def test_connections_passed2(self):

        """Function:  test_connections_passed2

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, None))
        mongo.disconnect()

    def test_connections_passed(self):

        """Function:  test_connections_passed

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(connections=self.cfg.repset_hosts),
                         (True, None))
        mongo.disconnect()

    def test_no_conn_list3(self):

        """Function:  test_no_conn_list3

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts, coll=self.coll,
            db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.repset_hosts))
        mongo.disconnect()

    def test_no_conn_list2(self):

        """Function:  test_no_conn_list2

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            repset_hosts=self.cfg.repset_hosts, coll=self.coll,
            db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_no_conn_list1(self):

        """Function:  test_no_conn_list2

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, None))
        mongo.disconnect()

    def test_no_conn_list(self):

        """Function:  test_no_conn_list

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, repset=self.cfg.repset,
            coll=self.coll, db_auth=self.db_auth, db=self.dbs)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()


if __name__ == "__main__":
    unittest.main()
