#!/usr/bin/python
# Classification (U)

"""Program:  RepSetColl_ins_doc.py

    Description:  Unit testing of RepSetColl.ins_doc in mongo_class.py.

    Usage:
        test/unit/mongo_class/RepSetColl_ins_doc.py

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


class InsDoc(object):

    """Class:  InsDoc

    Description:  Class stub holder for RepSetColl class.

    Super-Class:

    Sub-Classes:

    Methods:
        insert_one -> Stub holder for RepSetColl.db_coll.insert_one method.

    """

    def insert_one(self):

        """Function:  insert_one

        Description:  Stub holder for RepSetColl.db_coll.insert_one method.

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
        test_ins_doc -> Test ins_doc method.

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
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"

    def test_ins_doc(self):

        """Function:  test_ins_doc

        Description:  Test ins_doc method.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset)
        mongo.db_coll = InsDoc()

        self.assertFalse(mongo.ins_doc())


if __name__ == "__main__":
    unittest.main()
