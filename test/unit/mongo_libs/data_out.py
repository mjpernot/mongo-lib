# Classification (U)

"""Program:  data_out.py

    Description:  Unit testing of data_out in mongo_libs.py.

    Usage:
        python test/unit/mongo_libs/data_out.py
        python3 test/unit/mongo_libs/data_out.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import json
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs

import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mongo_error
        test_mongo
        test_dict_out_false
        test_dict_out_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"key": "value", "key2": ["list1", "list2"]}
        self.mongo = "mongo"
        self.db_tbl = "db1:tbl1"
        self.results = (True, None)
        self.results2 = (False, "Error: Is not a dictionary")
        self.results3 = (False, "Error Message")

    @mock.patch("mongo_libs.ins_doc")
    @mock.patch("mongo_libs.gen_class.dict_out")
    def test_mongo_error(self, mock_out, mock_mongo):

        """Function:  test_mongo_error

        Description:  Test with mongo option with an error status.

        Arguments:

        """

        mock_out.return_value = (True, None)
        mock_mongo.return_value = (False, "Error Message")

        self.assertEqual(
            mongo_libs.data_out(
                self.data, mongo=self.mongo, db_tbl=self.db_tbl),
            self.results3)

    @mock.patch("mongo_libs.ins_doc")
    @mock.patch("mongo_libs.gen_class.dict_out")
    def test_mongo(self, mock_out, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_out.return_value = (True, None)
        mock_mongo.return_value = (True, None)

        self.assertEqual(
            mongo_libs.data_out(
                self.data, mongo=self.mongo, db_tbl=self.db_tbl), self.results)

    @mock.patch("mongo_libs.gen_class.dict_out")
    def test_dict_out_false(self, mock_out):

        """Function:  test_dict_out_false

        Description:  Test data is not a dictionary.

        Arguments:

        """

        mock_out.return_value = (False, "Error: Is not a dictionary")

        self.assertEqual(mongo_libs.data_out(self.data), self.results2)

    @mock.patch("mongo_libs.gen_class.dict_out")
    def test_dict_out_true(self, mock_out):

        """Function:  test_dict_out_true

        Description:  Test data is a dictionary.

        Arguments:

        """

        mock_out.return_value = (True, None)

        self.assertEqual(mongo_libs.data_out(self.data), self.results)


if __name__ == "__main__":
    unittest.main()
