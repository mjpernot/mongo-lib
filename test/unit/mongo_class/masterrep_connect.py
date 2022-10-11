# Classification (U)

"""Program:  masterrep_connect.py

    Description:  Unit testing of MasterRep.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/masterrep_connect.py

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
        setUp
        test_slaves_attr4
        test_slaves_attr3
        test_slaves_attr2
        test_slaves_attr
        test_repset_attr2
        test_repset_attr
        test_issecondary_attr2
        test_issecondary_attr
        test_ismaster_attr2
        test_ismaster_attr
        test_no_conn_list1
        test_no_conn_list
        test_fail_connection2
        test_fail_connection
        test_no_data2
        test_no_data
        test_default2
        test_default

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
        self.data = {"secondary": False, "ismaster": True,
                     "issecondary": False, "setName": "mongo_repset",
                     "hosts": ["slave1", "slave2"]}
        self.data2 = {"secondary": False, "ismaster": True,
                      "issecondary": False, "setName": "mongo_repset"}
        self.msg = "Error:  This is not a Master Replication server."

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_slaves_attr4(self, mock_fetch):

        """Function:  test_slaves_attr4

        Description:  Test slaves attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data2
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertEqual(mongo.slaves, [])

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_slaves_attr3(self, mock_fetch):

        """Function:  test_slaves_attr3

        Description:  Test slaves attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_slaves_attr2(self, mock_fetch):

        """Function:  test_slaves_attr2

        Description:  Test slaves attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertEqual(mongo.slaves, ["slave1", "slave2"])

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_slaves_attr(self, mock_fetch):

        """Function:  test_slaves_attr

        Description:  Test slaves attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_repset_attr2(self, mock_fetch):

        """Function:  test_repset_attr2

        Description:  Test repset attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertEqual(mongo.repset, "mongo_repset")

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_repset_attr(self, mock_fetch):

        """Function:  test_repset_attr

        Description:  Test repset attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_issecondary_attr2(self, mock_fetch):

        """Function:  test_issecondary_attr2

        Description:  Test issecondary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertFalse(mongo.issecondary)

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_issecondary_attr(self, mock_fetch):

        """Function:  test_issecondary_attr

        Description:  Test issecondary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_ismaster_attr2(self, mock_fetch):

        """Function:  test_ismaster_attr2

        Description:  Test ismaster attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertTrue(mongo.ismaster)

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_ismaster_attr(self, mock_fetch):

        """Function:  test_ismaster_attr

        Description:  Test ismaster attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_no_conn_list1(self, mock_fetch):

        """Function:  test_no_conn_list1

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.conn = True
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, True,
             False))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_no_conn_list(self, mock_fetch):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_fail_connection2(self, mock_fetch):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_fail_connection(self, mock_fetch):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (False, "Error Message"))

    @mock.patch("mongo_class.Server.disconnect", mock.Mock(return_value=True))
    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster", mock.Mock(return_value={}))
    def test_no_data2(self):

        """Function:  test_no_data2

        Description:  Test with no data returned.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None))

    @mock.patch("mongo_class.Server.disconnect", mock.Mock(return_value=True))
    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster", mock.Mock(return_value={}))
    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data returned.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (False, self.msg))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_default2(self, mock_fetch):

        """Function:  test_default2

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, True,
             False))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_default(self, mock_fetch):

        """Function:  test_default

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
