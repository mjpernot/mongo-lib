#!/usr/bin/python
# Classification (U)

"""Program:  db_db_connect.py

    Description:  Integration testing of DB.db_connect in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_db_connect.py

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
        test_fail_connection2 -> Test with failed connection.
        test_fail_connection -> Test with failed connection.
        test_none_database_passed2 -> Test with none database passed.
        test_none_database_passed -> Test with none database passed.
        test_database_passed2 -> Test with database passed.
        test_database_passed -> Test with database passed.
        test_no_database2 -> Test with no database passed.
        test_no_database -> Test with no database passed.

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

    def test_fail_connection2(self):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        mongo.db_connect("testdb")

        self.assertFalse(mongo.db)

    def test_fail_connection(self):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        msg = "Authentication failed."
        errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, "mytestpd", host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.db_connect("testdb"), (False, errmsg))

    def test_none_database_passed2(self):

        """Function:  test_none_database_passed2

        Description:  Test with none database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)
        mongo.db_connect(dbs=None)

        self.assertTrue(mongo.db)

    def test_none_database_passed(self):

        """Function:  test_none_database_passed

        Description:  Test with none database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)

        self.assertEqual(mongo.db_connect(dbs=None), (True, None))

    def test_database_passed2(self):

        """Function:  test_database_passed2

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)
        mongo.db_connect(self.database)

        self.assertEqual(mongo.db_name, self.database)

    def test_database_passed(self):

        """Function:  test_database_passed

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)

        self.assertEqual(mongo.db_connect(self.database), (True, None))

    def test_no_database2(self):

        """Function:  test_no_database2

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)
        mongo.db_connect()

        self.assertEqual(mongo.db_name, "test")

    def test_no_database(self):

        """Function:  test_no_database

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)

        self.assertEqual(mongo.db_connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
