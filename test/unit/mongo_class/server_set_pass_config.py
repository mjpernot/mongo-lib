# Classification (U)

"""Program:  server_set_pass_config.py

    Description:  Unit testing of Server.set_pass_config method in
        mysql_class.py.

    Usage:
        test/unit/mmongo_class/server_set_pass_config.py

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
        setUp
        test_change_pass
        test_call_set_pass_config
        test_set_pass_config

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_japd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.conf_file = "Conf_File"
        self.new_japd = "new_mongo_japd"

    def test_change_pass(self):

        """Function:  test_change_pass

        Description:  Test change passwd and update config.

        Arguments:

        """

        global KEY1
        global KEY2

        new_config = {KEY1 + KEY2: self.new_japd}
        new_config["authMechanism"] = "SCRAM-SHA-1"
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)
        mongo.japd = self.new_japd
        mongo.set_pass_config()

        self.assertEqual(
            (mongo.config, mongo.japd), (new_config, self.new_japd))

    def test_call_set_pass_config(self):

        """Function:  test_call_set_pass_config

        Description:  Test configuration settings with direct call.

        Arguments:

        """

        global KEY1
        global KEY2

        config = {KEY1 + KEY2: self.japd}
        config["authMechanism"] = "SCRAM-SHA-1"
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)
        mongo.set_pass_config()

        self.assertEqual(mongo.config, config)

    def test_set_pass_config(self):

        """Function:  test_set_pass_config

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


if __name__ == "__main__":
    unittest.main()
