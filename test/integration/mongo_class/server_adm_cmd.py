#!/usr/bin/python
# Classification (U)

"""Program:  server_adm_cmd.py

    Description:  Integration testing of Server.adm_cmd in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_adm_cmd.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_arg -> Test with argument passed.
        test_adm_cmd -> Test adm_cmd method.

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
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=self.cfg.use_uri, auth=self.cfg.auth,
            use_arg=self.cfg.use_arg, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file)
        self.mongo.connect()

    def test_arg1(self):

        """Function:  test_arg1

        Description:  Test with argument passed.

        Arguments:

        """

        data = self.mongo.adm_cmd("getLog", arg1="global")

        self.assertTrue(isinstance(data["log"], list))

    def test_arg(self):

        """Function:  test_arg

        Description:  Test with argument passed.

        Arguments:

        """

        data = self.mongo.adm_cmd("getLog", arg1="global")

        self.assertTrue(data["totalLinesWritten"] >= 0)

    def test_adm_cmd(self):

        """Function:  test_adm_cmd

        Description:  Test adm_cmd method.

        Arguments:

        """

        data = self.mongo.adm_cmd("listDatabases")
        db_list = [item["name"] for item in data["databases"]]

        self.assertTrue("admin" in db_list)


if __name__ == "__main__":
    unittest.main()
