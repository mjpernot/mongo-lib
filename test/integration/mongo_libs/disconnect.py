# Classification (U)

"""Program:  disconnect.py

    Description:  Integration testing of disconnect in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/disconnect.py

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
import mongo_libs
import mongo_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_combo_servers
        test_multiple_list_servers
        test_single_list_server
        test_multiple_servers
        test_single_server

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"

        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)

    def test_combo_servers(self):

        """Function:  test_combo_servers

        Description:  Test with in a combination of servers and list.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        mongo2 = mongo_libs.create_instance(self.config_name, self.config_dir,
                                            mongo_class.Server)
        mongo3 = mongo_libs.create_instance(self.config_name, self.config_dir,
                                            mongo_class.Server)
        mongo.connect()
        mongo2.connect()
        mongo3.connect()
        mongo_libs.disconnect([mongo, mongo2], mongo3)
        self.assertFalse(mongo.conn or mongo2.conn or mongo3.conn)

    def test_multiple_list_servers(self):

        """Function:  test_multiple_list_servers

        Description:  Test with multiple servers in a list.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        mongo2 = mongo_libs.create_instance(self.config_name, self.config_dir,
                                            mongo_class.Server)
        mongo.connect()
        mongo2.connect()
        mongo_libs.disconnect([mongo, mongo2])
        self.assertFalse(mongo.conn or mongo2.conn)

    def test_single_list_server(self):

        """Function:  test_single_list_server

        Description:  Test with one server in list.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        mongo.connect()
        mongo_libs.disconnect([mongo])
        self.assertFalse(mongo.conn)

    def test_multiple_servers(self):

        """Function:  test_multiple_servers

        Description:  Test with multiple servers.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        mongo2 = mongo_libs.create_instance(self.config_name, self.config_dir,
                                            mongo_class.Server)
        mongo.connect()
        mongo2.connect()
        mongo_libs.disconnect(mongo, mongo2)
        self.assertFalse(mongo.conn or mongo2.conn)

    def test_single_server(self):

        """Function:  test_single_server

        Description:  Test with one server.

        Arguments:

        """

        mongo = mongo_libs.create_instance(self.config_name, self.config_dir,
                                           mongo_class.Server)
        mongo.connect()
        mongo_libs.disconnect(mongo)
        self.assertFalse(mongo.conn)


if __name__ == "__main__":
    unittest.main()
