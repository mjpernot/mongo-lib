# Classification (U)

"""Program:  add_tls_cmd.py

    Description:  Unit testing of add_tls_cmd in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/add_tls_cmd.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class Mongo():                                  # pylint:disable=R0903

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

        self.mongo = Mongo()
        self.mongo2 = Mongo()
        self.mongo2.config["tls"] = True
        self.cmd_line = ["program_name"]
        self.tls = "--tls"
        self.tls_ca = "--tlsCAFile="
        self.tls_key = "--tlsCertificateKeyFile="
        self.tls_phrase = "--tlsCertificateKeyFilePassword"
        self.ca_file = "tlsCAFile"
        self.key_file = "tlsCertificateKeyFile"
        self.key_phrase = "tlsCertificateKeyFilePassword"

    def test_tls_ca_phrase(self):

        """Function:  test_tls_ca_phrase

        Description:  Test with CA File and PEMKey phrase file.

        Arguments:

        """

        self.mongo2.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo2.config["tlsCertificateKeyFilePassword"] = self.key_phrase
        self.mongo2.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)
        result_cmd.append(self.tls_key + self.key_file)
        result_cmd.append(self.tls_phrase + "=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_tls_phrase(self):

        """Function:  test_tls_phrase

        Description:  Test with PEMKey phrase file.

        Arguments:

        """

        self.mongo2.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo2.config["tlsCertificateKeyFilePassword"] = self.key_phrase
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_key + self.key_file)
        result_cmd.append(self.tls_phrase + "=" + self.key_phrase)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_tls_ca_key(self):

        """Function:  test_tls_ca_key

        Description:  Test with CA file and PEMKey file.

        Arguments:

        """

        self.mongo2.config["tlsCertificateKeyFile"] = self.key_file
        self.mongo2.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)
        result_cmd.append(self.tls_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_tls_key(self):

        """Function:  test_tls_key

        Description:  Test with PEMKey file.

        Arguments:

        """

        self.mongo2.config["tlsCertificateKeyFile"] = self.key_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_key + self.key_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_tls_ca(self):

        """Function:  test_tls_ca

        Description:  Test with CA file.

        Arguments:

        """

        self.mongo2.config["tlsCAFile"] = self.ca_file
        result_cmd = list(self.cmd_line)
        result_cmd.append(self.tls)
        result_cmd.append(self.tls_ca + self.ca_file)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo2, self.cmd_line), result_cmd)

    def test_tls_true(self):

        """Function:  test_tls_true

        Description:  Test with tls set to True.

        Arguments:

        """

        self.mongo.config["tls"] = True
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

        result_cmd = list(self.cmd_line)

        self.assertEqual(
            mongo_libs.add_tls_cmd(self.mongo, self.cmd_line), result_cmd)


if __name__ == "__main__":
    unittest.main()
