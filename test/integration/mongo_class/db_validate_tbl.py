#!/usr/bin/python
# Classification (U)

"""Program:  db_validate_tbl.py

    Description:  Integration testing of DB.validate_tbl in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_validate_tbl.py

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
        test_raise_exception2
        test_raise_exception
        test_full_scan3
        test_full_scan2
        test_full_scan
        test_table3
        test_table2
        test_table

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
        self.tbl_name = "system.users"
        self.tbl_name2 = "no_table_exists"
        self.mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.database, use_arg=self.cfg.use_arg)
        self.mongo.connect()
        self.mongo.chg_db(self.database)

    def test_raise_exception2(self):

        """Function:  test_raise_exception2

        Description:  Test with raising exception.

        Arguments:

        """

        errmsg = "ns not found"
        _, data = self.mongo.validate_tbl(self.tbl_name2, scan=True)
        results = "%s" % data

        self.assertEqual(results, errmsg)

    def test_raise_exception(self):

        """Function:  test_raise_exception

        Description:  Test with raising exception.

        Arguments:

        """

        status, _ = self.mongo.validate_tbl(self.tbl_name2, scan=True)

        self.assertFalse(status)

    def test_full_scan3(self):

        """Function:  test_full_scan3

        Description:  Test validate_tbl method with full scan argument.

        Arguments:

        """

        _, data = self.mongo.validate_tbl(self.tbl_name, scan=True)

        self.assertTrue(data["valid"])

    def test_full_scan2(self):

        """Function:  test_full_scan2

        Description:  Test validate_tbl method with full scan argument.

        Arguments:

        """

        _, data = self.mongo.validate_tbl(self.tbl_name, scan=True)

        self.assertTrue(isinstance(data, dict))

    def test_full_scan(self):

        """Function:  test_full_scan

        Description:  Test validate_tbl method with full scan argument.

        Arguments:

        """

        status, _ = self.mongo.validate_tbl(self.tbl_name, scan=True)

        self.assertTrue(status)

    def test_table3(self):

        """Function:  test_table3

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        _, data = self.mongo.validate_tbl(self.tbl_name)

        self.assertTrue(data["valid"])

    def test_table2(self):

        """Function:  test_table2

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        _, data = self.mongo.validate_tbl(self.tbl_name)

        self.assertTrue(isinstance(data, dict))

    def test_table(self):

        """Function:  test_table

        Description:  Test validate_tbl method with default arguments.

        Arguments:

        """

        status, _ = self.mongo.validate_tbl(self.tbl_name)

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
