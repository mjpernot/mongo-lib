#!/usr/bin/python
# Classification (U)

"""Program:  repsetcoll_init.py

    Description:  Unit testing of RepSetColl.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_init.py

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
        test_config_attr3 -> Test with SCRAM-SHA-1 setting.
        test_config_attr2 -> Test with MONGODB-CR setting.
        test_db_auth_conn_attr -> Test db_auth_conn attribute.
        test_db_coll_attr -> Test db_coll attribute.
        test_db_conn_attr -> Test db_conn attribute.
        test_no_repset_hosts_attr -> Test no repset_hosts attribute passed.
        test_repset_hosts_attr -> Test repset_hosts attribute passed.
        test_no_repset_attr -> Test no repset attribute passed.
        test_repset_attr -> Test repset attribute passed.
        test_no_conf_file_attr -> Test no conf_file attribute passed.
        test_conf_file_attr -> Test conf_file attribute passed.
        test_no_auth_attr -> Test with auth attribute passed.
        test_auth_attr2 -> Test with auth attribute False.
        test_auth_attr -> Test with auth attribute True.
        test_db_auth_attr -> Test db_auth attribute passed.
        test_no_db_auth_attr -> Test no db_auth attribute passed.
        test_coll_attr -> Test coll attribute passed.
        test_no_coll_attr -> Test no coll attribute passed.
        test_db_attr -> Test db attribute passed.
        test_no_db_attr -> Test no db attribute passed.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_no_auth_db -> Test using no auth_db attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_no_using_arg -> Test with auth and no arg present.
        test_using_arg -> Test with auth and arg present.
        test_no_auth_uri -> Test with auth and no uri present.
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
        self.coll = None
        self.db_auth = "minedb1"
        self.repset = "mongo_repset"
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.mydb = "minedb"
        self.mycoll = "minecollection"
        self.config = {key1 + key2: self.japd}
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config File"
        self.repset_hosts = ["host1:port", "host2:port"]
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
        self.config2 = {key1 + key2: self.japd,
                        "authMechanism": self.auth_mech2}

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_db_auth_conn_attr(self):

        """Function:  test_db_auth_conn_attr

        Description:  Test db_auth attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_auth)

    def test_db_coll_attr(self):

        """Function:  test_db_coll_attr

        Description:  Test db_coll attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_coll)

    def test_db_conn_attr(self):

        """Function:  test_db_conn_attr

        Description:  Test db_conn attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_conn)

    def test_no_repset_hosts_attr(self):

        """Function:  test_no_repset_hosts_attr

        Description:  Test no repset_hosts attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.repset_hosts)

    def test_repset_hosts_attr(self):

        """Function:  test_repset_hosts_attr

        Description:  Test repset_hosts attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertEqual(mongo.repset_hosts, self.repset_hosts)

    def test_no_repset_attr(self):

        """Function:  test_no_repset_attr

        Description:  Test no repset attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.repset)

    def test_repset_attr(self):

        """Function:  test_repset_attr

        Description:  Test repset attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.repset, self.repset)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_no_auth_attr(self):

        """Function:  test_no_auth_attr

        Description:  Test no auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertTrue(mongo.auth)

    def test_auth_attr2(self):

        """Function:  test_auth_attr2

        Description:  Test auth attribute False.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertFalse(mongo.auth)

    def test_auth_attr(self):

        """Function:  test_auth_attr

        Description:  Test auth attribute True.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertTrue(mongo.auth)

    def test_db_auth_attr(self):

        """Function:  test_db_auth_attr

        Description:  Test db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, db_auth=self.db_auth)

        self.assertEqual(mongo.db_auth, self.db_auth)

    def test_no_db_auth_attr(self):

        """Function:  test_no_db_auth_attr

        Description:  Test no db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db_auth, None)

    def test_coll_attr(self):

        """Function:  test_coll_attr

        Description:  Test coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.mycoll)

        self.assertEqual(mongo.coll, self.mycoll)

    def test_no_coll_attr(self):

        """Function:  test_no_coll_attr

        Description:  Test no coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.coll, None)

    def test_db_attr(self):

        """Function:  test_db_attr

        Description:  Test db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, db=self.mydb)

        self.assertEqual(mongo.db, self.mydb)

    def test_no_db_attr(self):

        """Function:  test_no_db_attr

        Description:  Test no db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db, "test")

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config2)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.use_uri)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.db, mongo.coll, mongo.repset),
            (self.name, self.user, self.japd, self.host, self.port, self.dbs,
             self.coll, self.repset))


if __name__ == "__main__":
    unittest.main()
