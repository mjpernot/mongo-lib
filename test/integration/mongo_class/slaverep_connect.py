# Classification (U)

"""Program:  slaverep_connect.py

    Description:  Integration testing of SlaveRep.connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/slaverep_connect.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_is_not_slave2
        test_is_not_slave
        test_primary2
        test_primary
        test_repset2
        test_repset
        test_issecondary2
        test_issecondary
        test_ismaster2
        test_ismaster
        test_fail_get_srv_attr2
        test_fail_get_srv_attr
        test_auth
        test_no_auth

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mongo"
        self.config_name2 = "master_mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.cfg2 = gen_libs.load_module(self.config_name2, self.config_dir)
        self.database = "admin"

    def test_is_not_slave2(self):

        """Function:  test_is_not_slave2

        Description:  Test with connecting to master node.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg2.name, self.cfg2.user, self.cfg2.japd,
            host=self.cfg2.host, port=self.cfg2.port, auth=self.cfg2.auth,
            auth_db=self.cfg2.auth_db, conf_file=self.cfg2.conf_file,
            direct_connect=self.cfg2.direct_connect)
        mongo.connect()

        self.assertFalse(mongo.ismaster)

    def test_is_not_slave(self):

        """Function:  test_is_not_slave

        Description:  Test with connecting to master node.

        Arguments:

        """

        errmsg = "Error:  This is not a Slave Replication server."

        mongo = mongo_class.SlaveRep(
            self.cfg2.name, self.cfg2.user, self.cfg2.japd,
            host=self.cfg2.host, port=self.cfg2.port, auth=self.cfg2.auth,
            auth_db=self.cfg2.auth_db, conf_file=self.cfg2.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_primary2(self):

        """Function:  test_primary2

        Description:  Test primary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_primary(self):

        """Function:  test_primary

        Description:  Test primary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertTrue(mongo.primary)
        mongo.disconnect()

    def test_repset2(self):

        """Function:  test_repset2

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_repset(self):

        """Function:  test_repset

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertIsNotNone(mongo.repset)
        mongo.disconnect()

    def test_issecondary2(self):

        """Function:  test_issecondary2

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_issecondary(self):

        """Function:  test_issecondary

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertTrue(mongo.issecondary)
        mongo.disconnect()

    def test_ismaster2(self):

        """Function:  test_ismaster2

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_ismaster(self):

        """Function:  test_ismaster

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertFalse(mongo.ismaster)
        mongo.disconnect()

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.cfg.name, self.cfg.user, "mytestpd", self.cfg.host,
             self.cfg.port))

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertFalse(mongo.connect()[0])

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with auth.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertEqual(mongo.connect(), (True, None))
        mongo.disconnect()

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file,
            direct_connect=self.cfg.direct_connect)

        self.assertFalse(mongo.connect()[0])


if __name__ == "__main__":
    unittest.main()
