#!/usr/bin/python
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
        setUp -> Initialize testing environment.
        test_is_not_master2 -> Test with connecting to slave node.
        test_is_not_master -> Test with connecting to slave node.
        test_slaves2 -> Test slaves attribute.
        test_slaves -> Test slaves attribute.
        test_repset -> Test repset attribute.
        test_issecondary -> Test issecondary attribute.
        test_ismaster -> Test ismaster attribute.
        test_fail_get_srv_attr -> Test with failed get_srv_attr call.
        test_auth_arg2 -> Test with auth and arg present.
        test_auth_arg -> Test with auth and arg present.
        test_auth_uri2 -> Test with auth and uri present.
        test_auth_uri -> Test with auth and uri present.
        test_no_auth2 -> Test with no auth present.
        test_no_auth -> Test with no auth present.

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
            host=self.cfg2.host, port=self.cfg2.port,
            use_uri=self.cfg2.use_uri, auth=self.cfg2.auth,
            use_arg=self.cfg2.use_arg, auth_db=self.cfg2.auth_db,
            conf_file=self.cfg2.conf_file)
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
            host=self.cfg2.host, port=self.cfg2.port,
            use_uri=self.cfg2.use_uri, auth=self.cfg2.auth,
            use_arg=self.cfg2.use_arg, auth_db=self.cfg2.auth_db,
            conf_file=self.cfg2.conf_file)
        mongo.connect()

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_slaves2(self):

        """Function:  test_slaves2

        Description:  Test slaves attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
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
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (False, errmsg))

    def test_auth_arg2(self):

        """Function:  test_auth_arg2

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=False, auth_db=True, conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))

    def test_no_auth2(self):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=False,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
