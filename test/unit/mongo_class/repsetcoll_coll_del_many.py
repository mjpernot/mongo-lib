# Classification (U)

"""Program:  repsetcoll_coll_del_many.py

    Description:  Unit testing of RepSetColl.coll_del_many in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_coll_del_many.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class CollDelMany(object):

    """Class:  CollDelMany

    Description:  Class stub holder for RepSetColl class.

    Methods:
        __init__
        delete_many

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.qry = None

    def delete_many(self, qry):

        """Function:  delete_many

        Description:  Stub holder for RepSetColl.db_coll.delete_many method.

        Arguments:
            (input) qry

        """

        self.qry = qry

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_override
        test_qry
        test_no_qry

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

    def test_override(self):

        """Function:  test_override

        Description:  Test with override argument passed.

        Arguments:

        """

        override = True
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollDelMany()

        self.assertFalse(mongo.coll_del_many(override=override))

    def test_qry(self):

        """Function:  test_qry

        Description:  Test with query passed.

        Arguments:

        """

        qry = {"QueryHere"}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollDelMany()

        self.assertFalse(mongo.coll_del_many(qry))

    def test_no_qry(self):

        """Function:  test_no_qry

        Description:  Test with no query passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollDelMany()

        with gen_libs.no_std_out():
            self.assertFalse(mongo.coll_del_many())


if __name__ == "__main__":
    unittest.main()
