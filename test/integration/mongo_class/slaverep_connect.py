#!/usr/bin/python
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
        test_auth_arg2
        test_auth_arg
        test_auth_uri2
        test_auth_uri
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
        self.config_name = "slave_mongo"
        self.config_name2 = "mongo"
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
            host=self.cfg2.host, port=self.cfg2.port,
            use_uri=self.cfg2.use_uri, auth=self.cfg2.auth,
            use_arg=self.cfg2.use_arg, auth_db=self.cfg2.auth_db,
            conf_file=self.cfg2.conf_file)
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
            host=self.cfg2.host, port=self.cfg2.port,
            use_uri=self.cfg2.use_uri, auth=self.cfg2.auth,
            use_arg=self.cfg2.use_arg, auth_db=self.cfg2.auth_db,
            conf_file=self.cfg2.conf_file)
        mongo.connect()

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_primary2(self):

        """Function:  test_primary2

        Description:  Test primary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_primary(self):

        """Function:  test_primary

        Description:  Test primary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(mongo.primary)

    def test_repset2(self):

        """Function:  test_repset2

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_repset(self):

        """Function:  test_repset

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertEqual(mongo.repset, self.cfg.repset)

    def test_issecondary2(self):

        """Function:  test_issecondary2

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_issecondary(self):

        """Function:  test_issecondary

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertTrue(mongo.issecondary)

    def test_ismaster2(self):

        """Function:  test_ismaster2

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_ismaster(self):

        """Function:  test_ismaster

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertFalse(mongo.ismaster)

    def test_fail_get_srv_attr2(self):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.cfg.name, self.cfg.user, "mytestpd", self.cfg.host,
             self.cfg.port, self.cfg.use_arg))

    def test_fail_get_srv_attr(self):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_auth_arg2(self):

        """Function:  test_auth_arg2

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.use_arg))

    def test_auth_arg(self):

        """Function:  test_auth_arg

        Description:  Test with failed connection.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_auth_uri2(self):

        """Function:  test_auth_uri2

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=False, auth_db=True, conf_file=self.cfg.conf_file)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_uri),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port, self.cfg.use_uri))

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=False, auth_db=True, conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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

        mongo = mongo_class.SlaveRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
