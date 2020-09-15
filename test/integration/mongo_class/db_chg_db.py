#!/usr/bin/python
# Classification (U)

"""Program:  db_chg_db.py

    Description:  Integration testing of DB.chg_db in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_chg_db.py

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
        test_database_passed -> Test with database passed.
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

    def test_database_passed2(self):

        """Function:  test_database_passed2

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)
        mongo.connect()
        mongo.chg_db(self.database)

        self.assertTrue(mongo.db)

    def test_database_passed(self):

        """Function:  test_database_passed

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)
        mongo.connect()
        mongo.chg_db(dbs=self.database)

        self.assertEqual(mongo.db_name, self.database)

    def test_no_database2(self):

        """Function:  test_no_database2

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)
        mongo.connect()
        mongo.chg_db()

        self.assertTrue(mongo.db)

    def test_no_database(self):

        """Function:  test_no_database

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)
        mongo.connect()
        mongo.chg_db()

        self.assertEqual(mongo.db_name, "test")


if __name__ == "__main__":
    unittest.main()
