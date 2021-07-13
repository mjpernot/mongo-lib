#!/usr/bin/python
# Classification (U)

"""Program:  coll_ins_doc.py

    Description:  Unit testing of Coll.ins_doc in mongo_class.py.

    Usage:
        test/unit/mongo_class/coll_ins_doc.py

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
import version

__version__ = version.__version__


class CollIns(object):

    """Class:  CollIns

    Description:  Class stub holder for Coll class.

    Methods:
        __init__
        insert_one

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.doc = None

    def insert_one(self, doc):

        """Function:  insert_one

        Description:  Stub for Coll.ins_doc method.

        Arguments:
            (input) doc

        """

        self.doc = doc

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_query
        test_empty_doc

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = "coll_name"
        self.db_auth = None

    def test_query(self):

        """Function:  test_query

        Description:  Test with query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.coll = CollIns()

        self.assertFalse(mongo.ins_doc({"Key": "Value"}))

    def test_empty_doc(self):

        """Function:  test_empty_doc

        Description:  Test with empty document.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.coll = CollIns()

        self.assertFalse(mongo.ins_doc({}))


if __name__ == "__main__":
    unittest.main()
