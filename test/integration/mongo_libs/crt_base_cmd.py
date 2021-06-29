#!/usr/bin/python
# Classification (U)

"""Program:  crt_base_cmd.py

    Description:  Integration testing of crt_base_cmd in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/crt_base_cmd.py

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
        test_auth
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

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd,
            host=self.cfg.host, port=self.cfg.port, auth=self.cfg.auth,
            conf_file=self.cfg.conf_file, auth_db=self.cfg.auth_db,
            use_arg=self.cfg.use_arg, use_uri=self.cfg.use_uri,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        self.mongorep = mongo_class.RepSet(
            self.cfg.name, self.cfg.user, self.cfg.japd,
            host=self.cfg.host, port=self.cfg.port, auth=self.cfg.auth,
            conf_file=self.cfg.conf_file, auth_db=self.cfg.auth_db,
            use_arg=self.cfg.use_arg, use_uri=self.cfg.use_uri,
            repset=self.cfg.repset, ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        host = "--host="
        data = "--pass"
        data2 = "word="
        self.uname = "--username="
        self.japd2 = data + data2
        self.prog_name = "crt_base_cmd.py"
        self.host_port = self.cfg.host + ":" + str(self.cfg.port)
        self.host_port_uri = host + self.cfg.repset + "/" + self.host_port
        self.host_str = host + self.cfg.host + ":" + str(self.cfg.port)
        self.host_str2 = host + self.cfg.repset + "/" + self.host_port
        self.results = [self.prog_name, self.uname + self.cfg.user,
                        self.host_str, self.japd2 + self.cfg.japd]
        self.results2 = [self.prog_name, self.uname + self.cfg.user,
                         self.host_str2, self.japd2 + self.cfg.japd]
        self.results3 = [self.prog_name, self.uname + self.cfg.user,
                         self.host_port_uri, self.japd2 + self.cfg.japd]
        self.results4 = [self.prog_name, self.host_str]

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with authority needed.

        Arguments:

        """

        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no authority needed.

        Arguments:

        """

        self.mongo.auth = False

        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results4)

    def test_host(self):

        """Function:  test_host

        Description:  Test with host name for connection.

        Arguments:

        """

        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results)

    def test_repset(self):

        """Function:  test_repset

        Description:  Test with repset name for connection.

        Arguments:

        """

        cmdline = mongo_libs.crt_base_cmd(self.mongorep, self.prog_name,
                                          use_repset=True)

        self.assertEqual(cmdline, self.results2)

    def test_repset_hosts(self):

        """Function:  test_repset_hosts

        Description:  Test with repset name and hosts for connection.

        Arguments:

        """

        self.mongorep.repset_hosts = self.host_port

        cmdline = mongo_libs.crt_base_cmd(self.mongorep, self.prog_name,
                                          use_repset=True)

        self.assertEqual(cmdline, self.results3)


if __name__ == "__main__":
    unittest.main()
