#!/usr/bin/python
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
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.passwd = "passwd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.repset_hosts = "host:27017"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_no_auth -> Test with no authority needed.
        test_host -> Test with host name for connection.
        test_repset -> Test with repset name for connection.
        test_repset_hosts -> Test with repset name and hosts for connection.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.passwd = "passwd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.repset_hosts = "host:27017"
        self.prog_name = "program_name"
        self.host_port = "--host=" + self.repset + "/" + self.repset_hosts
        self.host_port2 = "--host=" + self.repset + "/" + self.host + ":" \
                          + str(self.port)
        self.host_port3 = "--host=" + self.host + ":" + str(self.port)

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
        self.assertEqual(mongo_libs.crt_base_cmd(mongo, self.prog_name),
                         [self.prog_name, "--username=" + self.user,
                          self.host_port3, "--password=" + self.passwd])

    def test_repset(self):

        """Function:  test_repset

        Description:  Test with repset name for connection.

        Arguments:

        """

        mongo = Mongo()
        mongo.repset_hosts = None
        self.assertEqual(mongo_libs.crt_base_cmd(mongo, self.prog_name,
                                                 use_repset=True),
                         [self.prog_name, "--username=" + self.user,
                          self.host_port2, "--password=" + self.passwd])

    def test_repset_hosts(self):

        """Function:  test_repset_hosts

        Description:  Test with repset name and hosts for connection.

        Arguments:

        """

        mongo = Mongo()
        self.assertEqual(mongo_libs.crt_base_cmd(mongo, self.prog_name,
                                                 use_repset=True),
                         [self.prog_name, "--username=" + self.user,
                          self.host_port, "--password=" + self.passwd])


if __name__ == "__main__":
    unittest.main()
