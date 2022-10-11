# Classification (U)

"""Program:  crt_base_cmd.py

    Description:  Unit testing of crt_base_cmd in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/crt_base_cmd.py

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
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.repset_hosts = "host:27017"
        self.config = {}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ssl_true
        test_ssl_false2
        test_ssl_false
        test_auth_no_pass
        test_auth_pass
        test_no_auth
        test_host
        test_repset
        test_repset_hosts

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        host = "--host="
        data = "--pass"
        data2 = "word="
        self.uname = "--username="
        self.japd2 = data + data2
        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.repset_hosts = "host:27017"
        self.prog_name = "program_name"
        self.host_port = host + self.repset + "/" + self.repset_hosts
        self.host_port2 = \
            host + self.repset + "/" + self.host + ":" + str(self.port)
        self.host_port3 = host + self.host + ":" + str(self.port)
        self.ssl = "--ssl"

    def test_ssl_true(self):

        """Function:  test_ssl_true

        Description:  Test with SSL option set to True.

        Arguments:

        """

        mongo = Mongo()
        mongo.config["ssl"] = True
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name),
            [self.prog_name, self.uname + self.user, self.host_port3,
             self.japd2 + self.japd, self.ssl])

    def test_ssl_false2(self):

        """Function:  test_ssl_false2

        Description:  Test with SSL option set to False.

        Arguments:

        """

        mongo = Mongo()
        mongo.config["ssl"] = False
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name),
            [self.prog_name, self.uname + self.user, self.host_port3,
             self.japd2 + self.japd])

    def test_ssl_false(self):

        """Function:  test_ssl_false

        Description:  Test with no SSL option present.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name),
            [self.prog_name, self.uname + self.user, self.host_port3,
             self.japd2 + self.japd])

    def test_auth_no_pass(self):

        """Function:  test_auth_no_pass

        Description:  Test with auth and no_pass set to True.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name, no_pass=True),
            [self.prog_name, self.uname + self.user, self.host_port3])

    def test_auth_pass(self):

        """Function:  test_auth_pass

        Description:  Test with auth and no_pass set to False.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name, no_pass=False),
            [self.prog_name, self.uname + self.user, self.host_port3,
             self.japd2 + self.japd])

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no authority needed.

        Arguments:

        """

        mongo = Mongo()
        mongo.auth = False
        self.assertEqual(mongo_libs.crt_base_cmd(mongo, self.prog_name),
                         [self.prog_name, self.host_port3])

    def test_host(self):

        """Function:  test_host

        Description:  Test with host name for connection.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name),
            [self.prog_name, self.uname + self.user, self.host_port3,
             self.japd2 + self.japd])

    def test_repset(self):

        """Function:  test_repset

        Description:  Test with repset name for connection.

        Arguments:

        """

        mongo = Mongo()
        mongo.repset_hosts = None
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name, use_repset=True),
            [self.prog_name, self.uname + self.user, self.host_port2,
             self.japd2 + self.japd])

    def test_repset_hosts(self):

        """Function:  test_repset_hosts

        Description:  Test with repset name and hosts for connection.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(
            mongo_libs.crt_base_cmd(mongo, self.prog_name, use_repset=True),
            [self.prog_name, self.uname + self.user, self.host_port,
             self.japd2 + self.japd])


if __name__ == "__main__":
    unittest.main()
