#!/usr/bin/python
# Classification (U)

"""Program:  Coll_ins_doc.py

    Description:  Unit testing of Coll.ins_doc in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_ins_doc.py

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
        insert_one -> Stub for Coll.ins_doc method.

    """

    def insert_one(self, doc):

        """Function:  insert_one

        Description:  Stub for Coll.ins_doc method.

        Arguments:
            (input) doc -> Document.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_query -> Test with query command.
        test_empty_query -> Test with empty query command.
        test_no_query -> Test with no query command.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.passwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.db = "test"
        self.coll = "coll_name"
        self.db_auth = None


    def test_query(self):

        """Function:  test_query

        Description:  Test with query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.db = CollIns()

        self.assertTrue(mongo.ins_doc({"Key": "Value"}))

    def test_empty_query(self):

        """Function:  test_empty_query

        Description:  Test with empty query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.db = CollIns()

        self.assertTrue(mongo.ins_doc({}))

    def test_no_query(self):

        """Function:  test_no_query

        Description:  Test with no query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.db = CollIns()

        self.assertTrue(mongo.ins_doc())


if __name__ == "__main__":
    unittest.main()
