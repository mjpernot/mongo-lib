#!/usr/bin/python
# Classification (U)

"""Program:  add_ssl_cmd.py

    Description:  Unit testing of add_ssl_cmd in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/add_ssl_cmd.py

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
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "word"
KEY3 = "ssl_pem_"
KEY4 = "phrase"


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.repset_hosts = "host:27017"
        self.config = {}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        ssl_ca_phrase
        ssl_phrase
        test_ssl_ca_key
        test_ssl_key
        test_ssl_ca
        test_ssl_true
        test_ssl_false
        test_no_ssl

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()
        self.mongo2 = Mongo()
        self.mongo2.config["ssl"] = True
        self.cmd_line = ["program_name"]
        self.ssl = "--ssl"
        self.ssl_ca = "--sslCAFile="
        self.ssl_key = "--sslPEMKeyFile="
        self.ssl_phrase = "--sslPEMKeyPass"
        self.ca_file = "CAFile"
        self.key_file = "KeyFile"
        self.key_phrase = "KeyPhraseFile"

    def ssl_ca_phrase(self):

        """Function:  ssl_ca_phrase

        Description:  Test with CA File and PEMKey phrase file.

        Arguments:

        """

        global KEY1
        global KEY2
        global KEY3
        global KEY4

        self.mongo2.config["ssl_keyfile"] = self.key_file
        self.mongo2.config[KEY3 + KEY1 + KEY4] = self.key_phrase
        self.mongo2.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)
        result_cmd.append(self.ssl_key + self.key_file)
        result_cmd.append(self.ssl_phrase + KEY2 + "=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo2, self.cmd_line), result_cmd)

    def ssl_phrase(self):

        """Function:  ssl_phrase

        Description:  Test with PEMKey phrase file.

        Arguments:

        """

        self.mongo2.config["ssl_keyfile"] = self.key_file
        self.mongo2.config[KEY3 + KEY1 + KEY4] = self.key_phrase
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_key + self.key_file)
        result_cmd.append(self.ssl_phrase + KEY2 + "=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_ssl_ca_key(self):

        """Function:  test_ssl_ca_key

        Description:  Test with CA file and PEMKey file.

        Arguments:

        """

        self.mongo2.config["ssl_keyfile"] = self.key_file
        self.mongo2.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)
        result_cmd.append(self.ssl_key + self.key_file)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_ssl_key(self):

        """Function:  test_ssl_key

        Description:  Test with PEMKey file.

        Arguments:

        """

        self.mongo2.config["ssl_keyfile"] = self.key_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_key + self.key_file)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_ssl_ca(self):

        """Function:  test_ssl_ca

        Description:  Test with CA file.

        Arguments:

        """

        self.mongo2.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_ssl_true(self):

        """Function:  test_ssl_true

        Description:  Test with ssl set to True.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_false(self):

        """Function:  test_ssl_false

        Description:  Test with ssl set to False.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.crt_base_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_no_ssl(self):

        """Function:  test_no_ssl

        Description:  Test with no ssl in config.

        Arguments:

        """

        result_cmd = list(self.cmd_line)
       
        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)


if __name__ == "__main__":
    unittest.main()

