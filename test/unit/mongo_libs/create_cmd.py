#!/usr/bin/python
# Classification (U)

"""Program:  create_cmd.py

    Description:  Unit testing of create_cmd in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/create_cmd.py

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

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepSetName"
        self.repset_hosts = "ServerName1:27017, ServerName2:27017"
        self.host = "IP"
        self.port = 27017
        self.user = "username"
        self.japd = "userpd"
        self.auth = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_full_test -> Test with all external calls.
        test_crt_base_cmd -> Test with crt_base_cmd call.
        test_add_cmd_list -> Test with list.
        test_add_cmd_empty -> Test with empty list.
        test_is_add_cmd -> Test with is_add_cmd call.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        data = "--pass"
        data2 = "word="
        pwd = data + data2
        self.mongo = Mongo()
        self.args_array = {"-m": True, "-p": "/dir/path"}
        self.prog_name = "mongostats"
        self.path = "/dir/path"
        self.path_opt = "-p"
        self.req_arg = ["--required"]
        self.opt_arg = {"-m": "-m=1"}
        self.result = [self.path + "/" + self.prog_name, "-m=1"]
        self.result2 = [self.path + "/" + self.prog_name, "--required", "-m=1"]
        self.result3 = [self.path + "/" + self.prog_name,
                        "--username=username", "--host=IP:27017", pwd,
                        "--required", "-m=1"]

    def test_full_test(self):

        """Function:  test_full_test

        Description:  Test with all external calls.

        Arguments:

        """

        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               opt_arg=self.opt_arg,
                                               req_arg=self.req_arg),
                         self.result3)

    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_crt_base_cmd(self, mock_arg):

        """Function:  test_crt_base_cmd

        Description:  Test with crt_base_cmd call.

        Arguments:

        """

        mock_arg.return_value = self.path + "/"
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               opt_arg=self.opt_arg,
                                               req_arg=self.req_arg),
                         self.result3)

    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_add_cmd_list(self, mock_arg, mock_cmd):

        """Function:  test_add_cmd_list

        Description:  Test with list.

        Arguments:

        """

        mock_arg.return_value = self.path + "/"
        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               opt_arg=self.opt_arg,
                                               req_arg=self.req_arg),
                         self.result2)

    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_add_cmd_empty(self, mock_arg, mock_cmd):

        """Function:  test_add_cmd_empty

        Description:  Test with empty list.

        Arguments:

        """

        mock_arg.return_value = self.path + "/"
        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               opt_arg=self.opt_arg),
                         self.result)

    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_is_add_cmd(self, mock_arg, mock_cmd):

        """Function:  test_is_add_cmd

        Description:  Test with is_add_cmd call.

        Arguments:

        """

        mock_arg.return_value = self.path + "/"
        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               opt_arg=self.opt_arg),
                         self.result)

    @mock.patch("mongo_libs.cmds_gen.is_add_cmd")
    @mock.patch("mongo_libs.cmds_gen.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_default(self, mock_arg, mock_cmd, mock_add, mock_is_add):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_arg.return_value = "Base_Program"
        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = ["Base_Crt_Program_Arg_Plus"]
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               req_arg=self.req_arg),
                         ["Base_Crt_Program_Arg_Plus"])


if __name__ == "__main__":
    unittest.main()
