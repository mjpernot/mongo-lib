# Classification (U)

"""Program:  add_tls_cmd.py

    Description:  Integration testing of add_tls_cmd in mongo_libs.py.

    Usage:
        test/integration/mongo_libs/add_tls_cmd.py

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
        test_tls_ca_phrase
        test_tls_phrase
        test_tls_ca_key
        test_tls_key
        test_tls_ca
        test_tls_true
        test_tls_false
        test_no_tls

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
            auth_type=self.cfg.auth_type, tls_ca_certs=self.cfg.tls_ca_certs,
            tls_certkey=self.cfg.tls_certkey,
            tls_certkey_phrase=self.cfg.tls_certkey_phrase)

        self.cmd_line = ["program_name"]
        self.tls = "--ssl"
        self.tls_ca = "--sslCAFile="
        self.tls_key = "--sslPEMKeyFile="
        self.tls_phrase = "--sslPEMKeyPassword"
        self.ca_file = "tlsCAFile"
        self.key_file = "tlsCertificateKeyFile"
        self.key_phrase = "tlsCertificateKeyFilePassword"

#        self.tls = "--tls"
#        self.tls_ca = "--tlsCAFile="
#        self.tls_key = "--tlsCertificateKeyFile="
#        self.tls_phrase = "--tlsCertificateKeyFilePassword"
#        self.ca_file = "tlsCAFile"
#        self.key_file = "tlsCertificateKeyFile"
#        self.key_phrase = "tlsCertificateKeyFilePassword"

    def test_tls_ca_phrase(self):

        """Function:  test_tls_ca_phrase

        Description:  Test with CA File and PEMKey phrase file.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        self.mongo.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo.config["tlsCertificateKeyFilePassword"] = self.key_phrase
        self.mongo.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)
        result_cmd.append(self.tls_key + self.key_file)
        result_cmd.append(self.tls_phrase + "word=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_phrase(self):

        """Function:  test_tls_phrase

        Description:  Test with PEMKey phrase file.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        self.mongo.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo.config["tlsCertificateKeyFilePassword"] = self.key_phrase
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_key + self.key_file)
        result_cmd.append(self.tls_phrase + "word=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_ca_key(self):

        """Function:  test_tls_ca_key

        Description:  Test with CA file and PEMKey file.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        self.mongo.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)
        result_cmd.append(self.tls_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_key(self):

        """Function:  test_tls_key

        Description:  Test with PEMKey file.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        self.mongo.config["tlsCertificateKeyFile"] = self.key_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_ca(self):

        """Function:  test_tls_ca

        Description:  Test with CA file.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        self.mongo.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_true(self):

        """Function:  test_tls_true

        Description:  Test with tls set to True.

        Arguments:

        """

        self.mongo.config["tls"] = True
        self.mongo.config.pop("tlsCAFile", None)
        self.mongo.config.pop("tlsCertificateKeyFile", None)
        self.mongo.config.pop("tlsCertificateKeyFilePassword", None)
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_tls_false(self):

        """Function:  test_tls_false

        Description:  Test with tls set to False.

        Arguments:

        """

        self.mongo.config["tls"] = False
        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)

    def test_no_tls(self):

        """Function:  test_no_tls

        Description:  Test with no tls in config.

        Arguments:

        """

        self.mongo.config.pop("tls", None)
        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)


if __name__ == "__main__":
    unittest.main()
