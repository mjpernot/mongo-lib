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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Methods:
        __init__

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
        self.config = {}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_missing_arg
        test_args
        test_args_array
        test_full_test
        test_crt_base_cmd
        test_add_cmd_list
        test_add_cmd_empty
        test_is_add_cmd
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        data = "--pass"
        data2 = "word="
        pwd = data + data2
        self.path = "/base/path"
        self.mongo = Mongo()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-m": True, "-p": self.path}
        self.prog_name = "mongostats"
        self.path_opt = "-p"
        self.req_arg = ["--required"]
        self.opt_arg = {"-m": "-m=1"}
        self.result = [self.path + "/" + self.prog_name, "-m=1"]
        self.result2 = [self.path + "/" + self.prog_name, "--required", "-m=1"]
        self.result3 = [
            self.path + "/" + self.prog_name, "--username=username",
            "--host=IP:27017", pwd + "userpd", "--required", "-m=1"]

    @mock.patch("mongo_libs.gen_libs.is_add_cmd")
    @mock.patch("mongo_libs.gen_libs.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    def test_missing_arg(self, mock_cmd, mock_add, mock_is_add):

        """Function:  test_missing_arg

        Description:  Test with the missing option in args_array.

        Arguments:

        """

        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = ["Base_Crt_Program_Arg_Plus"]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args2, self.prog_name, self.path_opt,
                req_arg=self.req_arg), ["Base_Crt_Program_Arg_Plus"])

    @mock.patch("mongo_libs.gen_libs.is_add_cmd")
    @mock.patch("mongo_libs.gen_libs.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    def test_args(self, mock_cmd, mock_add, mock_is_add):

        """Function:  test_args

        Description:  Test with the gen_class.ArgsParser class.

        Arguments:

        """

        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = ["Base_Crt_Program_Arg_Plus"]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                req_arg=self.req_arg), ["Base_Crt_Program_Arg_Plus"])

    @mock.patch("mongo_libs.gen_libs.is_add_cmd")
    @mock.patch("mongo_libs.gen_libs.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    def test_args_array(self, mock_cmd, mock_add, mock_is_add):

        """Function:  test_args_array

        Description:  Test with the args_array dictionary (old method).

        Arguments:

        """

        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = ["Base_Crt_Program_Arg_Plus"]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                req_arg=self.req_arg), ["Base_Crt_Program_Arg_Plus"])

    def test_full_test(self):

        """Function:  test_full_test

        Description:  Test with all external calls.

        Arguments:

        """

        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                opt_arg=self.opt_arg, req_arg=self.req_arg), self.result3)

    def test_crt_base_cmd(self):

        """Function:  test_crt_base_cmd

        Description:  Test with crt_base_cmd call.

        Arguments:

        """

        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                opt_arg=self.opt_arg, req_arg=self.req_arg), self.result3)

    @mock.patch("mongo_libs.crt_base_cmd")
    def test_add_cmd_list(self, mock_cmd):

        """Function:  test_add_cmd_list

        Description:  Test with list.

        Arguments:

        """

        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                opt_arg=self.opt_arg, req_arg=self.req_arg), self.result2)

    @mock.patch("mongo_libs.crt_base_cmd")
    def test_add_cmd_empty(self, mock_cmd):

        """Function:  test_add_cmd_empty

        Description:  Test with empty list.

        Arguments:

        """

        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                opt_arg=self.opt_arg), self.result)

    @mock.patch("mongo_libs.crt_base_cmd")
    def test_is_add_cmd(self, mock_cmd):

        """Function:  test_is_add_cmd

        Description:  Test with is_add_cmd call.

        Arguments:

        """

        mock_cmd.return_value = [self.path + "/" + self.prog_name]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                opt_arg=self.opt_arg), self.result)

    @mock.patch("mongo_libs.gen_libs.is_add_cmd")
    @mock.patch("mongo_libs.gen_libs.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    def test_default(self, mock_cmd, mock_add, mock_is_add):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = ["Base_Crt_Program_Arg_Plus"]
        self.assertEqual(
            mongo_libs.create_cmd(
                self.mongo, self.args, self.prog_name, self.path_opt,
                req_arg=self.req_arg), ["Base_Crt_Program_Arg_Plus"])


if __name__ == "__main__":
    unittest.main()
