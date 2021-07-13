#!/usr/bin/python
# Classification (U)

"""Program:  server_set_ssl_config.py

    Description:  Unit testing of Server.set_ssl_config in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_set_ssl_config.py

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
import mongo_class
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "word"
KEY3 = "ssl_pem_"
KEY4 = "phrase"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ssl_all_phrase2
        test_ssl_all_phrase
        test_ssl_all2
        test_ssl_all
        test_ssl_client_key_phrase2
        test_ssl_client_key_phrase
        test_ssl_client_key_cert3
        test_ssl_client_key_cert2
        test_ssl_client_key_cert
        test_ssl_client_ca6
        test_ssl_client_ca5
        test_ssl_client_ca4
        test_ssl_client_ca3
        test_ssl_client_ca2
        test_ssl_client_ca

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        global KEY1
        global KEY2
        global KEY3
        global KEY4

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_japd"
        self.host = "host_server"
        self.port = 27017
        self.conf_file = "Conf_File"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"

        self.config = {}
        self.config[KEY1 + KEY2] = self.japd
        self.config["authMechanism"] = "SCRAM-SHA-1"
        self.config["ssl"] = True
        self.config["ssl_ca_certs"] = "CAFile"

        self.config2 = {}
        self.config2[KEY1 + KEY2] = self.japd
        self.config2["authMechanism"] = "SCRAM-SHA-1"
        self.config2["ssl"] = True
        self.config2["ssl_keyfile"] = "KeyFile"
        self.config2["ssl_certfile"] = "CertFile"

        self.config3 = {}
        self.config3[KEY1 + KEY2] = self.japd
        self.config3["authMechanism"] = "SCRAM-SHA-1"
        self.config3["ssl"] = True
        self.config3["ssl_keyfile"] = "KeyFile"
        self.config3["ssl_certfile"] = "CertFile"
        self.config3[KEY3 + KEY1 + KEY4] = "MyPhrase"

        self.config4 = {}
        self.config4[KEY1 + KEY2] = self.japd
        self.config4["authMechanism"] = "SCRAM-SHA-1"
        self.config4["ssl"] = True
        self.config4["ssl_ca_certs"] = "CAFile"
        self.config4["ssl_keyfile"] = "KeyFile"
        self.config4["ssl_certfile"] = "CertFile"

        self.config5 = {}
        self.config5[KEY1 + KEY2] = self.japd
        self.config5["authMechanism"] = "SCRAM-SHA-1"
        self.config5["ssl"] = True
        self.config5["ssl_ca_certs"] = "CAFile"
        self.config5["ssl_keyfile"] = "KeyFile"
        self.config5["ssl_certfile"] = "CertFile"
        self.config5[KEY3 + KEY1 + KEY4] = "MyPhrase"

    def test_ssl_all_phrase(self):

        """Function:  test_ssl_all_phrase

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert, mongo.ssl_client_ca,
             mongo.ssl_client_phrase),
            (self.ssl_client_key, self.ssl_client_cert, self.ssl_client_ca,
             self.ssl_client_phrase))

    def test_ssl_all2(self):

        """Function:  test_ssl_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config4)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_ca, self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_key_phrase2(self):

        """Function:  test_ssl_client_key_phrase2

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_key_phrase(self):

        """Function:  test_ssl_client_key_phrase

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.ssl_client_phrase, self.ssl_client_phrase)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.config, self.config2)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_phrase), (None, None))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca6(self):

        """Function:  test_ssl_client_ca6

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config)

    def test_ssl_client_ca5(self):

        """Function:  test_ssl_client_ca5

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config)

    def test_ssl_client_ca4(self):

        """Function:  test_ssl_client_ca4

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.config, self.config)

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_ca3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert,
             mongo.ssl_client_phrase), (None, None, None))

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)


if __name__ == "__main__":
    unittest.main()
