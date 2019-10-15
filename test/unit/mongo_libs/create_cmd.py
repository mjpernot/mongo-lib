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
        test_create_cmd -> Test create_cmd function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = "Mongo_Class"
        self.args_array = {}
        self.prog_name = "progam_name"
        self.path_opt = "/dir_path/"
        self.req_arg = "-d"

    @mock.patch("mongo_libs.cmds_gen.is_add_cmd")
    @mock.patch("mongo_libs.cmds_gen.add_cmd")
    @mock.patch("mongo_libs.crt_base_cmd")
    @mock.patch("mongo_libs.arg_parser.arg_set_path")
    def test_create_cmd(self, mock_arg, mock_cmd, mock_add, mock_is_add):

        """Function:  test_create_cmd

        Description:  Test create_cmd function.

        Arguments:

        """

        mock_arg.return_value = "Base_Program"
        mock_cmd.return_value = "Base_Crt_Program"
        mock_add.return_value = "Base_Crt_Program_Arg"
        mock_is_add.return_value = "Base_Crt_Program_Arg_Plus"
        self.assertEqual(mongo_libs.create_cmd(self.mongo, self.args_array,
                                               self.prog_name, self.path_opt,
                                               req_arg=self.req_arg),
                         "Base_Crt_Program_Arg_Plus")


if __name__ == "__main__":
    unittest.main()
