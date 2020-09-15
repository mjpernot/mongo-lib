#!/usr/bin/python
# Classification (U)

"""Program:  server_disconnect.py

    Description:  Unit testing of Server.disconnect in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_disconnect.py

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
import mongo_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_disconnect -> Test disconnect method.

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
        self.conf_file = "Conf_File"

    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_disconnect(self, mock_client):

        """Function:  test_disconnect

        Description:  Test disconnect method.

        Arguments:

        """

        mock_client.close.return_value = True
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host, self.port)

        mongo.disconnect()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.conn),
            (self.name, self.user, self.japd, self.host, self.port, None))


if __name__ == "__main__":
    unittest.main()
