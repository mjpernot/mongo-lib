#!/usr/bin/python
# Classification (U)

"""Program:  rep_fetch_nodes.py

    Description:  Unit testing of Rep.fetch_nodes in mongo_class.py.

    Usage:
        test/unit/mongo_class/rep_fetch_nodes.py

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


class Conn(object):

    """Class:  Conn

    Description:  Class stub holder for Rep class.

    Methods:
        insert_one

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for Rep.conn.nodes attribute.

        Arguments:

        """

        self.nodes = ["node1", "node2"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_nodes

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
        self.nodes = ["node1", "node2"]

    def test_fetch_nodes(self):

        """Function:  test_fetch_nodes

        Description:  Test fetch_nodes method.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)
        mongo.conn = Conn()

        self.assertEqual(mongo.fetch_nodes(), self.nodes)


if __name__ == "__main__":
    unittest.main()
