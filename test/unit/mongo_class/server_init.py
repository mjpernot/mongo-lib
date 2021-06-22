#!/usr/bin/python
# Classification (U)

"""Program:  server_init.py

    Description:  Unit testing of Server.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_init.py

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

# Global
KEY1 = "pass"
KEY2 = "word"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_set_pass -> Test with default config settings.
        test_config_attr3 -> Test with SCRAM-SHA-1 setting.
        test_config_attr2 -> Test with MONGODB-CR setting.
        test_auth_mech -> Test passing arg to auth_mech attribute.
        test_default_auth_mech -> Test auth_mech default setting.
        test_uptime_attr -> Test uptime attribute.
        test_port_attr -> Test port attribute.
        test_host_attr -> Test host attribute.
        test_japd_attr -> Test japd attribute.
        test_user_attr -> Test user attribute.
        test_name_attr -> Test name attribute.
        test_log_path_attr -> Test log_path attribute.
        test_db_path_attr -> Test db_path attribute.
        test_conn_attr -> Test conn attribute.
        test_no_conf_file_attr -> Test no conf_file attribute passed.
        test_conf_file_attr -> Test conf_file attribute passed.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_no_auth_db -> Test using no auth_db attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_no_using_arg -> Test with auth and no arg present.
        test_using_arg -> Test with auth and arg present.
        test_no_auth_uri -> Test with auth and no uri present.
        test_auth_uri -> Test with auth and uri present.
        test_auth_false -> Test with auth passed as False.
        test_auth_true -> Test with auth passed as True.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        global KEY1
        global KEY2

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.config = {KEY1 + KEY2: self.japd}
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config file"
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
        self.config2 = {KEY1 + KEY2: self.japd,
                        "authMechanism": self.auth_mech2}

    def test_set_pass(self):

        """Function:  test_set_pass

        Description:  Test setting configuration settings.

        Arguments:

        """

        global KEY1
        global KEY2

        config = {KEY1 + KEY2: self.japd}
        config["authMechanism"] = "SCRAM-SHA-1"
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)

        self.assertEqual(mongo.config, config)

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_auth_mech2(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    def test_auth_mech(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech2)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_default_auth_mech(self):

        """Function:  test_default_auth_mech

        Description:  Test auth_mech default setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_uptime_attr(self):

        """Function:  test_uptime_attr

        Description:  Test uptime attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.uptime)

    def test_port_attr(self):

        """Function:  test_port_attr

        Description:  Test port attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.port, self.port)

    def test_host_attr(self):

        """Function:  test_host_attr

        Description:  Test host attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.host, self.host)

    def test_japd_attr(self):

        """Function:  test_japd_attr

        Description:  Test japd attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.japd, self.japd)

    def test_user_attr(self):

        """Function:  test_user_attr

        Description:  Test user attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.user, self.user)

    def test_name_attr(self):

        """Function:  test_name_attr

        Description:  Test name attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.name, self.name)

    def test_log_path_attr(self):

        """Function:  test_log_path_attr

        Description:  Test log_path attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.log_path)

    def test_db_path_attr(self):

        """Function:  test_db_path_attr

        Description:  Test db_path attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.db_path)

    def test_conn_attr(self):

        """Function:  test_conn_attr

        Description:  Test conn attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.conn)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.config, self.config2)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test using the arg connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.use_uri)

    def test_using_uri(self):

        """Function:  test_using_uri

        Description:  Test using the uri connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth passed as False.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   host=self.host, port=self.port, auth=False)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.name, self.user, self.japd, self.host,
                          self.port, False))

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth passed as True.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   host=self.host, port=self.port, auth=True)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.name, self.user, self.japd, self.host,
                          self.port, True))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   host=self.host, port=self.port)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port),
                         (self.name, self.user, self.japd, self.host,
                          self.port))


if __name__ == "__main__":
    unittest.main()
