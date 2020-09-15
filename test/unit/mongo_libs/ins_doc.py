#!/usr/bin/python
# Classification (U)

"""Program:  ins_doc.py

    Description:  Unit testing of ins_doc in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/ins_doc.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo.Coll class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for Mongo.Coll.connect method.
        ins_doc -> Stub holder for Mongo.Coll.ins_doc method.

    """

    def __init__(self, success):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:
         (input) success -> True|False - Connection is successful.

        """

        self.doc = None
        self.success = success

    def connect(self):

        """Function:  connect

        Description:  Stub holder for Mongo.Coll.connect method.

        Arguments:

        """

        if self.success:
            return True, None

        return False, "Error message"

    def ins_doc(self, doc):

        """Function:  ins_doc

        Description:  Stub holder for Mongo.Coll.ins_doc method.

        Arguments:
            (input) doc -> Document.

        """

        self.doc = doc

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fail_connection -> Test with failed connection.
        test_ins_doc -> Test ins_doc function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo_cfg = "MongoCfg"
        self.dbs = "DBName"
        self.tbl = "TableName"
        self.data = {"key": "value"}

    @mock.patch("mongo_libs.crt_coll_inst")
    def test_fail_connection(self, mock_inst):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mock_inst.return_value = Mongo(success=False)

        self.assertEqual(
            mongo_libs.ins_doc(self.mongo_cfg, self.dbs, self.tbl, self.data),
            (False, "Error message"))

    @mock.patch("mongo_libs.cmds_gen.disconnect")
    @mock.patch("mongo_libs.crt_coll_inst")
    def test_ins_doc(self, mock_inst, mock_cmd):

        """Function:  test_ins_doc

        Description:  Test ins_doc function.

        Arguments:

        """

        mock_inst.return_value = Mongo(success=True)
        mock_cmd.return_value = True

        self.assertEqual(
            mongo_libs.ins_doc(self.mongo_cfg, self.dbs, self.tbl, self.data),
            (True, None))


if __name__ == "__main__":
    unittest.main()
