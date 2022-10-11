# Classification (U)

"""Program:  repsetcoll_ins_doc.py

    Description:  Unit testing of RepSetColl.ins_doc in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_ins_doc.py

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

        Description:  Stub holder for RepSetColl.db_coll.insert_one method.

        Arguments:
            (input) doc -> Document

        """

        self.doc = doc

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ins_doc

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
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"
        self.doc = {"Document"}

    def test_ins_doc(self):

        """Function:  test_ins_doc

        Description:  Test ins_doc method.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = InsDoc()

        self.assertFalse(mongo.ins_doc(self.doc))


if __name__ == "__main__":
    unittest.main()
