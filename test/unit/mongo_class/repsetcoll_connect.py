# Classification (U)

"""Program:  repsetcoll_connect.py

    Description:  Unit testing of RepSetColl.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_connect.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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
        test_auth_mech4
        test_auth_mech3
        test_auth_mech2
        test_auth_mech
        test_no_auth_mech2
        test_no_auth_mech
        test_db_auth_passed2
        test_db_auth_passed
        test_coll_passed2
        test_coll_passed
        test_db_not_passed2
        test_db_not_passed
        test_db_passed2
        test_db_passed
        test_auth
        test_auth_false
        test_fail_get_srv_attr2
        test_fail_get_srv_attr
        test_auth_true2
        test_auth_true
        test_no_auth2
        test_no_auth
        test_conn_false2
        test_conn_false
        test_conn_true2
        test_conn_true
        test_connections_passed2
        test_connections_passed
        test_no_conn_list3
        test_no_conn_list2
        test_no_conn_list1
        test_no_conn_list

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
        self.connections = ["mongo1:27017", "mongo2:27017", "mongo3:27017"]
        self.conn = "Mongo_Connection"
        self.conn2 = {"db_name": RepSetColl(), "test": {"coll_name": True}}
        self.dbn = "MyDatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.auth_mech2 = "MONGODB-CR"

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_mech4(self, mock_mongo):

        """Function:  test_auth_mech4

        Description:  Test with authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True, auth_mech=self.auth_mech2)
        mongo.connect()

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_mech3(self, mock_mongo):

        """Function:  test_auth_mech3

        Description:  Test with authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_mech2(self, mock_mongo):

        """Function:  test_auth_mech2

        Description:  Test with authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True, auth_mech=self.auth_mech)
        mongo.connect()

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_mech(self, mock_mongo):

        """Function:  test_auth_mech

        Description:  Test with authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True, auth_mech=self.auth_mech)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_auth_mech2(self, mock_mongo):

        """Function:  test_no_auth_mech2

        Description:  Test with no authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)
        mongo.connect()

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_auth_mech(self, mock_mongo):

        """Function:  test_no_auth_mech

        Description:  Test with no authenticate mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_auth_passed2(self, mock_mongo):

        """Function:  test_db_auth_passed2

        Description:  Test with db_auth passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)
        mongo.connect()

        self.assertEqual(mongo.db_auth, self.db_auth)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_auth_passed(self, mock_mongo):

        """Function:  test_db_auth_passed

        Description:  Test with db_auth passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_coll_passed2(self, mock_mongo):

        """Function:  test_coll_passed2

        Description:  Test with coll passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)
        mongo.connect()

        self.assertEqual(mongo.coll, self.coll)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_coll_passed(self, mock_mongo):

        """Function:  test_coll_passed

        Description:  Test with coll passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_not_passed2(self, mock_mongo):

        """Function:  test_db_not_passed2

        Description:  Test with db not passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            auth=True)
        mongo.connect()

        self.assertEqual(mongo.db, "test")

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_not_passed(self, mock_mongo):

        """Function:  test_db_not_passed

        Description:  Test with db not passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_passed2(self, mock_mongo):

        """Function:  test_db_passed2

        Description:  Test with db passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "MyDatabase": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            auth=True, db=self.dbn)
        mongo.connect()

        self.assertEqual(mongo.db, self.dbn)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_passed(self, mock_mongo):

        """Function:  test_db_passed

        Description:  Test with db passed.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "MyDatabase": {"coll_name": True}}

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            auth=True, db=self.dbn)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth(self, mock_mongo):

        """Function:  test_auth

        Description:  Test with auth present.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_false(self, mock_mongo):

        """Function:  test_auth_false

        Description:  Test with auth set to false.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=None,
            db=self.dbs, auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_get_srv_attr2(self, mock_mongo):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_get_srv_attr(self, mock_mongo):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertEqual(mongo.connect(), (False, "Error Message"))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_true2(self, mock_mongo):

        """Function:  test_auth_true2

        Description:  Test with auth set to true.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)
        mongo.connect()

        self.assertEqual((mongo.auth), (True))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_auth_true(self, mock_mongo):

        """Function:  test_auth_true

        Description:  Test with auth set to true.

        Arguments:

        """

        mock_mongo.return_value = {"db_name": RepSetColl(),
                                   "test": {"coll_name": True}}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.coll, db_auth=self.db_auth,
            db=self.dbs, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_auth2(self, mock_mongo):

        """Function:  test_no_auth2

        Description:  Test with auth set to false.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_auth(self, mock_mongo):

        """Function:  test_no_auth

        Description:  Test with auth set to false.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_conn_false2(self, mock_mongo):

        """Function:  test_conn_false2

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_conn_false(self, mock_mongo):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_conn_true2(self, mock_mongo):

        """Function:  test_conn_true2

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_conn_true(self, mock_mongo):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_mongo.return_value = self.conn
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_connections_passed2(self):

        """Function:  test_connections_passed2

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_connections_passed(self):

        """Function:  test_connections_passed

        Description:  Test with connections passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.conn = True

        self.assertEqual(mongo.connect(connections=self.connections),
                         (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_no_conn_list3(self):

        """Function:  test_no_conn_list3

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, repset_hosts=self.repset_hosts)
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             self.repset_hosts))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_no_conn_list2(self):

        """Function:  test_no_conn_list2

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, repset_hosts=self.repset_hosts)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_no_conn_list1(self):

        """Function:  test_no_conn_list2

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))

    @mock.patch("mongo_class.Server.get_srv_attr",
                mock.Mock(return_value=(True, None)))
    def test_no_conn_list(self):

        """Function:  test_no_conn_list

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
