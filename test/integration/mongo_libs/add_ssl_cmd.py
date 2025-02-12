# Classification (U)

"""Program:  add_ssl_cmd.py

    Description:  Integration testing of add_ssl_cmd in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/add_ssl_cmd.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_libs                           # pylint:disable=E0401,C0413
import mongo_class                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ssl_ca_phrase
        test_ssl_phrase
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

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd,
            host=self.cfg.host, port=self.cfg.port, auth=self.cfg.auth,
            conf_file=self.cfg.conf_file, auth_db=self.cfg.auth_db,
            ssl_client_ca=self.cfg.ssl_client_ca,
            ssl_client_key=self.cfg.ssl_client_key,
            ssl_client_cert=self.cfg.ssl_client_cert,
            ssl_client_phrase=self.cfg.ssl_client_phrase)

        self.cmd_line = ["program_name"]
        self.ssl = "--ssl"
        self.ssl_ca = "--sslCAFile="
        self.ssl_key = "--sslPEMKeyFile="
        self.ssl_phrase = "--sslPEMKeyPass"
        self.ca_file = "CAFile"
        self.key_file = "KeyFile"
        self.key_phrase = "KeyPhraseFile"

    def test_ssl_ca_phrase(self):

        """Function:  test_ssl_ca_phrase

        Description:  Test with CA File and PEMKey phrase file.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        self.mongo.config["ssl_keyfile"] = self.key_file
        self.mongo.config["ssl_pem_passphrase"] = self.key_phrase
        self.mongo.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)
        result_cmd.append(self.ssl_key + self.key_file)
        result_cmd.append(self.ssl_phrase + "word=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_phrase(self):

        """Function:  test_ssl_phrase

        Description:  Test with PEMKey phrase file.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        self.mongo.config["ssl_keyfile"] = self.key_file
        self.mongo.config["ssl_pem_passphrase"] = self.key_phrase
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_key + self.key_file)
        result_cmd.append(self.ssl_phrase + "word=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_ca_key(self):

        """Function:  test_ssl_ca_key

        Description:  Test with CA file and PEMKey file.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        self.mongo.config["ssl_keyfile"] = self.key_file
        self.mongo.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)
        result_cmd.append(self.ssl_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_key(self):

        """Function:  test_ssl_key

        Description:  Test with PEMKey file.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        self.mongo.config["ssl_keyfile"] = self.key_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_ca(self):

        """Function:  test_ssl_ca

        Description:  Test with CA file.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        self.mongo.config["ssl_ca_certs"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)
        result_cmd.append(self.ssl_ca + self.ca_file)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_true(self):

        """Function:  test_ssl_true

        Description:  Test with ssl set to True.

        Arguments:

        """

        self.mongo.config["ssl"] = True
        self.mongo.config.pop("ssl_ca_certs", None)
        self.mongo.config.pop("ssl_keyfile", None)
        self.mongo.config.pop("ssl_pem_passphrase", None)
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.ssl)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_ssl_false(self):

        """Function:  test_ssl_false

        Description:  Test with ssl set to False.

        Arguments:

        """

        self.mongo.config["ssl"] = False
        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_no_ssl(self):

        """Function:  test_no_ssl

        Description:  Test with no ssl in config.

        Arguments:

        """

        self.mongo.config.pop("ssl", None)
        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.add_ssl_cmd(self.mongo, self.cmd_line), result_cmd)


if __name__ == "__main__":
    unittest.main()
