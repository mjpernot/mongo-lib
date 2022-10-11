# Classification (U)

"""Program:  masterrep_connect.py

    Description:  Integration testing of MasterRep.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/masterrep_connect.py

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
        setUp
        test_is_not_master2
        test_is_not_master
        test_slaves2
        test_slaves
        test_repset
        test_issecondary
        test_ismaster
        test_fail_get_srv_attr
        test_auth
        test_no_auth2
        test_no_auth

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.config_name2 = "slave_mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.cfg2 = gen_libs.load_module(self.config_name2, self.config_dir)
        self.database = "admin"

    def test_is_not_master2(self):

        """Function:  test_is_not_master2

        Description:  Test with connecting to slave node.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg2.name, self.cfg2.user, self.cfg2.japd,
            host=self.cfg2.host, port=self.cfg2.port, auth=self.cfg2.auth,
            auth_db=self.cfg2.auth_db, conf_file=self.cfg2.conf_file)
        mongo.connect()

        self.assertFalse(mongo.ismaster)

    def test_is_not_master(self):

        """Function:  test_is_not_master

        Description:  Test with connecting to slave node.

        Arguments:

        """

        errmsg = "Error:  This is not a Master Replication server."

        mongo = mongo_class.MasterRep(
            self.cfg2.name, self.cfg2.user, self.cfg2.japd,
            host=self.cfg2.host, port=self.cfg2.port, auth=self.cfg2.auth,
            auth_db=self.cfg2.auth_db, conf_file=self.cfg2.conf_file)
        mongo.connect()

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_slaves2(self):

        """Function:  test_slaves2

        Description:  Test slaves attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(mongo.slaves)

    def test_slaves(self):

        """Function:  test_slaves

        Description:  Test slaves attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(isinstance(mongo.slaves, list))

    def test_repset(self):

        """Function:  test_repset

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertEqual(mongo.repset, self.cfg.repset)

    def test_issecondary(self):

        """Function:  test_issecondary

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertFalse(mongo.issecondary)

    def test_ismaster(self):

        """Function:  test_ismaster

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(mongo.ismaster)

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with uri present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=True,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
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

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
