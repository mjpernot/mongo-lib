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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_is_add_cmd -> Test with is_add_cmd call.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = "MongoClass"
        self.args_array = {"-m": True, "-n": False}
        self.prog_name = "mongo_name"
        self.path_opt = "/dir/path"
        self.req_arg = []
        self.opt_arg = {"-m": "-m=1", "-n": "-n=2"}
        self.result = [self.path_opt + "/" + self.prog_name, "-m=1"]

    @mock.patch("mongo_libs.cmds_gen.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_is_add_cmd(self, mock_arg, mock_cmd, mock_add):

        """Function:  test_is_add_cmd

        Description:  Test with is_add_cmd call.

        Arguments:

        """

        mock_arg.return_value = self.path_opt + "/"
        mock_cmd.return_value = [self.path_opt + "/" + self.prog_name]
        mock_add.return_value = [self.path_opt + "/" + self.prog_name]
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
