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

# Global
KEY1 = "pass"
KEY3 = "ssl_pem_"
KEY4 = "phrase"


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
        self.results5 = [self.prog_name, self.uname + self.cfg.user,
                         self.host_str]
        self.ssl = "--ssl"
        self.ssl_ca = "--sslCAFile="
        self.ssl_key = "--sslPEMKeyFile="
        self.ssl_phrase = "--sslPEMKeyPass"
        self.results6 = [self.prog_name, self.uname + self.cfg.user,
                         self.host_str, self.japd2 + self.cfg.japd, self.ssl]

    def test_ssl_true(self):

        """Function:  test_ssl_true

        Description:  Test with SSL option set to True.

        Arguments:

        """

        global KEY1
        global KEY3
        global KEY4

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop(KEY3 + KEY1 + KEY4, None)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo, self.prog_name),
            self.results6)


    def test_ssl_false2(self):

        """Function:  test_ssl_false2

        Description:  Test with SSL option set to False.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo, self.prog_name),
            self.results)

    def test_ssl_false(self):

        """Function:  test_ssl_false

        Description:  Test with no SSL option present.

        Arguments:

        """

        self.mongo.config.pop("ssl", None)
        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo, self.prog_name),
            self.results)

    def test_auth_no_pass(self):

        """Function:  test_auth_no_pass

        Description:  Test with auth and no_pass set to True.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name,
                                          no_pass=True)

        self.assertEqual(cmdline, self.results5)

    def test_auth_pass(self):

        """Function:  test_auth_pass

        Description:  Test with auth and no_pass set to False.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name,
                                          no_pass=False)

        self.assertEqual(cmdline, self.results)

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with authority needed.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no authority needed.

        Arguments:

        """

        self.mongo.auth = False
        self.mongo.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results4)

    def test_host(self):

        """Function:  test_host

        Description:  Test with host name for connection.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongo, self.prog_name)

        self.assertEqual(cmdline, self.results)

    def test_repset(self):

        """Function:  test_repset

        Description:  Test with repset name for connection.

        Arguments:

        """

        self.mongorep.config["ssl"] = False
        cmdline = mongo_libs.crt_base_cmd(self.mongorep, self.prog_name,
                                          use_repset=True)

        self.assertEqual(cmdline, self.results2)

    def test_repset_hosts(self):

        """Function:  test_repset_hosts

        Description:  Test with repset name and hosts for connection.

        Arguments:

        """

        self.mongorep.repset_hosts = self.host_port
        self.mongorep.config["ssl"] = False

        cmdline = mongo_libs.crt_base_cmd(self.mongorep, self.prog_name,
                                          use_repset=True)

        self.assertEqual(cmdline, self.results3)


if __name__ == "__main__":
    unittest.main()
