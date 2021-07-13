#!/usr/bin/python
# Classification (U)

"""Program:  repsetcoll_db_auth.py

    Description:  Unit testing of RepSetColl._db_auth in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_db_auth.py

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


class RepSetColl(object):

    """Class:  RepSetColl

    Description:  Class stub holder for RepSetColl class.

    Methods:
        __init__
        authenticate

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.user = None
        self.japd = None

    def authenticate(self, user, japd):

        """Function:  authenticate

        Description:  Stub for method.

        Arguments:
            (input) user
            (input) japd

        """

        self.user = user
        self.japd = japd

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_auth_true

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
        self.db_auth = "db_name"
        self.repset = "mongo_repset"
        self.repset_hosts = "host1:27017, host2:27107"
        self.conf_file = "Conf_File"
        self.use_uri = True
        self.use_arg = True
        self.connections = ["mongo1:27017", "mongo2:27017", "mongo3:27017"]
        self.conn = {"db_name": RepSetColl(), "test": {"coll_name": True}}

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth set to true.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)
        mongo.conn = self.conn
        mongo.db_conn = mongo.conn[self.db_auth]

        self.assertEqual(mongo._db_auth(), (True, None))


if __name__ == "__main__":
    unittest.main()
