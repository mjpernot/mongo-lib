#!/usr/bin/python
# Classification (U)

"""Program:  create_cmd.py

    Description:  Integration testing of create_cmd in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/create_cmd.py

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
        setUp -> Initialize testing environment.
        test_full_test -> Test with all external calls.
        test_crt_base_cmd2 -> Test with combinations.
        test_crt_base_cmd -> Test with combinations.
        test_is_add_cmd_dict -> Test with multiple dictionary.
        test_add_cmd_list -> Test with multiple list.
        test_is_add_cmd_empty -> Test with empty dictionary.
        test_add_cmd_empty -> Test with empty list.
        test_is_and_add_cmd -> Test with is_add_cmd and add_cmd calls.
        test_is_add_cmd -> Test with is_add_cmd call.
        test_add_cmd -> Test with add_cmd call.
        test_default -> Test with default settings.

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
        self.args_array = {"-p": os.getcwd()}
        self.args_array2 = {"-p": os.getcwd(), "-m": True}
        self.args_array3 = {"-p": os.getcwd(), "-m": True, "-n": True}
        self.prog_name = "create_cmd.py"
        self.path_opt = "-p"
        self.hosts = self.cfg.host + ":" + str(self.cfg.port)
        self.req_arg = ["--keeparg"]
        self.req_arg2 = ["--keeparg", "--keeparg2"]
        self.opt_arg = {"-m": "-m=1"}
        self.opt_arg2 = {"-m": "-m=1", "-n": "-n=0"}
        self.cmd_result = [os.path.join(self.args_array["-p"], self.prog_name),
                           "--username=" + self.cfg.user,
                           "--host=" + self.hosts,
                           "--password=" + self.cfg.japd]
        self.cmd_result2 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg[0]]
        self.cmd_result3 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.opt_arg["-m"]]
        self.cmd_result4 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg[0], self.opt_arg["-m"]]
        self.cmd_result5 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg2[0], self.req_arg2[1]]
        self.cmd_result6 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.opt_arg2["-m"], self.opt_arg2["-n"]]
        self.cmd_result7 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg2[0], self.req_arg2[1],
                            self.opt_arg["-m"]]
        self.cmd_result8 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg[0],
                            self.opt_arg2["-m"], self.opt_arg2["-n"]]
        self.cmd_result9 = [os.path.join(self.args_array["-p"],
                                         self.prog_name),
                            "--username=" + self.cfg.user,
                            "--host=" + self.hosts,
                            "--password=" + self.cfg.japd,
                            self.req_arg2[0], self.req_arg2[1],
                            self.opt_arg2["-m"], self.opt_arg2["-n"]]

    def test_full_test(self):

        """Function:  test_full_test

        Description:  Test with all external calls.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array3, self.prog_name, self.path_opt,
            req_arg=self.req_arg2, opt_arg=self.opt_arg2)

        self.assertEqual(cmd_line, self.cmd_result9)

    def test_crt_base_cmd2(self):

        """Function:  test_crt_base_cmd2

        Description:  Test with combinations.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array3, self.prog_name, self.path_opt,
            req_arg=self.req_arg, opt_arg=self.opt_arg2)

        self.assertEqual(cmd_line, self.cmd_result8)


    def test_is_add_cmd_dict(self):

        """Function:  test_is_add_cmd_dict

        Description:  Test with multiple dictionary.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array3, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg2)

        self.assertEqual(cmd_line, self.cmd_result6)

    def test_add_cmd_list(self):

        """Function:  test_add_cmd_list

        Description:  Test with multiple list.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array, self.prog_name, self.path_opt,
            req_arg=self.req_arg2)

        self.assertEqual(cmd_line, self.cmd_result5)

    def test_is_add_cmd_empty(self):

        """Function:  test_is_add_cmd_empty

        Description:  Test with empty dictionary.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array, self.prog_name, self.path_opt,
            opt_arg={})

        self.assertEqual(cmd_line, self.cmd_result)

    def test_add_cmd_empty(self):

        """Function:  test_add_cmd_empty

        Description:  Test with empty list.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array, self.prog_name, self.path_opt,
            req_arg=[])

        self.assertEqual(cmd_line, self.cmd_result)

    def test_is_and_add_cmd(self):

        """Function:  test_is_and_add_cmd

        Description:  Test with is_add_cmd and add_cmd calls.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array2, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg, req_arg=self.req_arg)

        self.assertEqual(cmd_line, self.cmd_result4)

    def test_is_add_cmd(self):

        """Function:  test_is_add_cmd

        Description:  Test with is_add_cmd call.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array2, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg)

        self.assertEqual(cmd_line, self.cmd_result3)

    def test_add_cmd(self):

        """Function:  test_add_cmd

        Description:  Test with add_cmd call.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array, self.prog_name, self.path_opt,
            req_arg=self.req_arg)

        self.assertEqual(cmd_line, self.cmd_result2)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args_array, self.prog_name, self.path_opt)

        self.assertEqual(cmd_line, self.cmd_result)


if __name__ == "__main__":
    unittest.main()
