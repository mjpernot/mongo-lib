# Classification (U)

"""Program:  server_set_tls_config.py

    Description:  Unit testing of Server.set_tls_config in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_set_tls_config.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_tls_all2
        test_tls_all
        test_tls_cert_key_config2
        test_tls_cert_key_config
        test_tls_ca_certs_config2
        test_tls_ca_certs_config

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_japd"
        self.host = "host_server"
        self.port = 27017
        self.conf_file = "Conf_File"
        self.auth_mech2 = "SCRAM-SHA-1"

        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertificationKeyFile"
        self.tls_certkey_phrase = "tlsCertificationKeyFilePassword"

        config = {}
        config["password"] = self.japd
        config["authMechanism"] = self.auth_mech2
        config["tls"] = True

        self.config2 = dict(config)
        self.config3a = dict(config)
        self.config4a = dict(config)
        self.config5a = dict(config)
        self.config6a = dict(config)
        self.config7a = dict(config)

        self.config3a["tlsCAFile"] = self.tls_ca_certs

        self.config4a["tlsCertificateKeyFile"] = self.tls_certkey

        self.config5a["tlsCertificateKeyFile"] = self.tls_certkey
        self.config5a[
            "tlsCertificateKeyFilePassword"] = self.tls_certkey_phrase

        self.config6a["tlsCAFile"] = self.tls_ca_certs
        self.config6a["tlsCertificateKeyFile"] = self.tls_certkey

        self.config7a["tlsCAFile"] = self.tls_ca_certs
        self.config7a["tlsCertificateKeyFile"] = self.tls_certkey
        self.config7a[
            "tlsCertificateKeyFilePassword"] = self.tls_certkey_phrase

    def test_tls_all2(self):

        """Function:  test_tls_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config7a)

    def test_tls_all(self):

        """Function:  test_tls_all

        Description:  Test with all tls arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey, auth_type="TLS")

        self.assertEqual(mongo.config, self.config6a)

    def test_tls_cert_key_config2(self):

        """Function:  test_tls_cert_key_config2

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config5a)

    def test_tls_cert_key_config(self):

        """Function:  test_tls_cert_key_config

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_certkey=self.tls_certkey,
            auth_type="TLS")

        self.assertEqual(mongo.config, self.config4a)

    def test_tls_ca_certs_config2(self):

        """Function:  test_tls_ca_certs_config2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)

    def test_tls_ca_certs_config(self):

        """Function:  test_tls_ca_certs_config

        Description:  Test with tls_ca_certs with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)


if __name__ == "__main__":
    unittest.main()
