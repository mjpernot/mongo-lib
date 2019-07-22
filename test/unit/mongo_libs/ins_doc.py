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

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for Mongo.Coll.connect method.
        ins_doc -> Stub holder for Mongo.Coll.ins_doc method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Function:  connect

        Description:  Stub holder for Mongo.Coll.connect method.

        Arguments:

        """

        return True

    def ins_doc(self):

        """Function:  ins_doc

        Description:  Stub holder for Mongo.Coll.ins_doc method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_ins_doc -> Test ins_doc function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo_cfg = "MongoCfg"
        self.db = "DBName"
        self.tbl = "TableName"
        self.data = {"key": "value"}

    @mock.patch("mongo_libs.cmds_gen.disconnect")
    @mock.patch("mongo_libs.crt_coll_inst")
    def test_ins_doc(self, mock_inst, mock_cmd):

        """Function:  test_ins_doc

        Description:  Test ins_doc function.

        Arguments:

        """

        mock_inst.return_value = Mongo()
        mock_cmd.return_value = True
        self.assertFalse(mongo_libs.ins_doc(self.mongo_cfg, self.db, self.tbl,
                                            self.data))


if __name__ == "__main__":
    unittest.main()
