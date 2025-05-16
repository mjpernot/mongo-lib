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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_libs                               # pylint:disable=E0401,C0413
import mongo_class                              # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
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
            conf_file=self.cfg.conf_file, auth_db=self.cfg.auth_db)
        host = "--host="
        data = "--pass"
        data2 = "word="
        self.uname = "--username="
        self.japd2 = data + data2
        self.prog_name = "crt_base_cmd.py"
        self.host_port = self.cfg.host + ":" + str(self.cfg.port)
        self.host_str = host + self.cfg.host + ":" + str(self.cfg.port)
        self.results = [self.prog_name, self.uname + self.cfg.user,
                        self.host_str, self.japd2 + self.cfg.japd]
        self.results4 = [self.prog_name, self.host_str]
        self.results5 = [self.prog_name, self.uname + self.cfg.user,
                         self.host_str]

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


if __name__ == "__main__":
    unittest.main()
