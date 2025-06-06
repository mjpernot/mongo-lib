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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_libs                               # pylint:disable=E0401,C0413
import mongo_class                              # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        arg_set_path
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Return True|False if argument exists.

        Arguments:

        """

        return arg in self.args_array

    def arg_set_path(self, arg_opt):

        """Method:  arg_set_path

        Description:  Return dir path from argument list or return empty
            string.

        Arguments:

        """

        path = os.path.join(
            self.args_array[arg_opt] if arg_opt in self.args_array else "")

        return path

    def get_val(self, skey, **kwargs):

        """Method:  get_val

        Description:  Return value for argument.

        Arguments:

        """
        def_val = kwargs.get("def_val", None)

        if isinstance(def_val, list):
            def_val = list(def_val)

        elif isinstance(def_val, dict):
            def_val = dict(def_val)

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_args
        test_args_array
        test_full_test
        test_crt_base_cmd2
        test_crt_base_cmd
        test_is_add_cmd_dict
        test_add_cmd_list
        test_is_add_cmd_empty
        test_add_cmd_empty
        test_is_and_add_cmd
        test_is_add_cmd
        test_add_cmd
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        username = "--username="
        host = "--host="
        data = "--pass"
        data2 = "word="
        japd2 = data + data2
        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth, auth_db=self.cfg.auth_db,
            conf_file=self.cfg.conf_file, ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-p": os.getcwd()}
        self.args2.args_array = {"-p": os.getcwd(), "-m": True}
        self.args3.args_array = {"-p": os.getcwd(), "-m": True, "-n": True}
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
        self.cmd_result = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd]
        self.cmd_result2 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg[0]]
        self.cmd_result3 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.opt_arg["-m"]]
        self.cmd_result4 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg[0], self.opt_arg["-m"]]
        self.cmd_result5 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg2[0], self.req_arg2[1]]
        self.cmd_result6 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.opt_arg2["-m"], self.opt_arg2["-n"]]
        self.cmd_result7 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg2[0], self.req_arg2[1], self.opt_arg["-m"]]
        self.cmd_result8 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg[0], self.opt_arg2["-m"], self.opt_arg2["-n"]]
        self.cmd_result9 = [
            os.path.join(self.args_array["-p"], self.prog_name),
            username + self.cfg.user, host + self.hosts, japd2 + self.cfg.japd,
            self.req_arg2[0], self.req_arg2[1], self.opt_arg2["-m"],
            self.opt_arg2["-n"]]

    def test_args(self):

        """Function:  test_args

        Description:  Test with the gen_class.ArgParser class.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result)

    def test_args_array(self):

        """Function:  test_args_array

        Description:  Test with args_array (old method).

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result)

    def test_full_test(self):

        """Function:  test_full_test

        Description:  Test with all external calls.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args3, self.prog_name, self.path_opt,
            req_arg=self.req_arg2, opt_arg=self.opt_arg2)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result9)

    def test_crt_base_cmd2(self):

        """Function:  test_crt_base_cmd2

        Description:  Test with combinations.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args3, self.prog_name, self.path_opt,
            req_arg=self.req_arg, opt_arg=self.opt_arg2)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result8)

    def test_is_add_cmd_dict(self):

        """Function:  test_is_add_cmd_dict

        Description:  Test with multiple dictionary.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args3, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg2)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result6)

    def test_add_cmd_list(self):

        """Function:  test_add_cmd_list

        Description:  Test with multiple list.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt,
            req_arg=self.req_arg2)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result5)

    def test_is_add_cmd_empty(self):

        """Function:  test_is_add_cmd_empty

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt,
            opt_arg={})
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result)

    def test_add_cmd_empty(self):

        """Function:  test_add_cmd_empty

        Description:  Test with empty list.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt,
            req_arg=[])
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result)

    def test_is_and_add_cmd(self):

        """Function:  test_is_and_add_cmd

        Description:  Test with is_add_cmd and add_cmd calls.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args2, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg, req_arg=self.req_arg)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result4)

    def test_is_add_cmd(self):

        """Function:  test_is_add_cmd

        Description:  Test with is_add_cmd call.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args2, self.prog_name, self.path_opt,
            opt_arg=self.opt_arg)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result3)

    def test_add_cmd(self):

        """Function:  test_add_cmd

        Description:  Test with add_cmd call.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt,
            req_arg=self.req_arg)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result2)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.mongo.connect()
        self.mongo.config["ssl"] = False
        cmd_line = mongo_libs.create_cmd(
            self.mongo, self.args, self.prog_name, self.path_opt)
        self.mongo.disconnect()

        self.assertEqual(cmd_line, self.cmd_result)


if __name__ == "__main__":
    unittest.main()
