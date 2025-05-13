# Classification (U)                                    # pylint:disable=C0302

"""Program:  server_init.py

    Description:  Integration testing of Server.__init__ in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_init.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_auth_type_none
        test_auth_type_tls
        test_tls_all2
        test_tls_all
        test_tls_cert_key_config2
        test_tls_cert_key_config
        test_tls_ca_certs_config2
        test_tls_ca_certs_config
        test_tls_certkey_phrase2
        test_tls_certkey_phrase
        test_tls_cert_key2
        test_tls_clientkey
        test_tls_client_ca2
        test_tls_ca_certs

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
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
        self.conn_list = [self.cfg.host + ":" + str(self.cfg.port)]
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.conf_file = "MyConf"

        self.config = {}
        self.config["password"] = self.cfg.japd

        self.config2 = {}
        self.config2["password"] = self.cfg.japd
        self.config2["authMechanism"] = self.auth_mech2

        self.config3 = {}
        self.config3["password"] = self.cfg.japd
        self.config3["authMechanism"] = self.auth_mech2
        self.config3["ssl"] = True
        self.config3["ssl_ca_certs"] = self.ssl_client_ca

        self.config4 = {}
        self.config4["password"] = self.cfg.japd
        self.config4["authMechanism"] = self.auth_mech2
        self.config4["ssl"] = True
        self.config4["ssl_keyfile"] = self.ssl_client_key
        self.config4["ssl_certfile"] = self.ssl_client_cert

        self.config5 = {}
        self.config5["password"] = self.cfg.japd
        self.config5["authMechanism"] = self.auth_mech2
        self.config5["ssl"] = True
        self.config5["ssl_keyfile"] = self.ssl_client_key
        self.config5["ssl_certfile"] = self.ssl_client_cert
        self.config5["ssl_pem_passphrase"] = self.ssl_client_phrase

        self.config6 = {}
        self.config6["password"] = self.cfg.japd
        self.config6["authMechanism"] = self.auth_mech2
        self.config6["ssl"] = True
        self.config6["ssl_ca_certs"] = self.ssl_client_ca
        self.config6["ssl_keyfile"] = self.ssl_client_key
        self.config6["ssl_certfile"] = self.ssl_client_cert

        self.config7 = {}
        self.config7["password"] = self.cfg.japd
        self.config7["authMechanism"] = self.auth_mech2
        self.config7["ssl"] = True
        self.config7["ssl_ca_certs"] = self.ssl_client_ca
        self.config7["ssl_keyfile"] = self.ssl_client_key
        self.config7["ssl_certfile"] = self.ssl_client_cert
        self.config7["ssl_pem_passphrase"] = self.ssl_client_phrase

        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertificationKeyFile"
        self.tls_certkey_phrase = "tlsCertificationKeyFilePassword"

        config = {}
        config["password"] = self.cfg.japd
        config["authMechanism"] = self.auth_mech2
        config["tls"] = True

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

    def test_auth_type_none(self):

        """Function:  test_auth_type_tls

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs, tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config7)

    def test_auth_type_tls(self):

        """Function:  test_auth_type_tls

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs, tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config7a)

    def test_tls_all2(self):

        """Function:  test_tls_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs, tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config7a)

    def test_tls_all(self):

        """Function:  test_tls_all

        Description:  Test with all tls arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs, tls_certkey=self.tls_certkey,
            auth_type="TLS")

        self.assertEqual(mongo.config, self.config6a)

    def test_tls_cert_key_config2(self):

        """Function:  test_tls_cert_key_config2

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config5a)

    def test_tls_cert_key_config(self):

        """Function:  test_tls_cert_key_config

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_certkey=self.tls_certkey, auth_type="TLS")

        self.assertEqual(mongo.config, self.config4a)

    def test_tls_ca_certs_config2(self):

        """Function:  test_tls_ca_certs_config2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)

    def test_tls_ca_certs_config(self):

        """Function:  test_tls_ca_certs_config

        Description:  Test with tls_ca_certs with config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            tls_ca_certs=self.tls_ca_certs, auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)

    def test_tls_certkey_phrase2(self):

        """Function:  test_tls_certkey_phrase2

        Description:  Test with tls_certkey_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, tls_certkey_phrase=self.tls_certkey_phrase,
            auth_type="TLS")

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    def test_tls_certkey_phrase(self):

        """Function:  test_tls_certkey_phrase

        Description:  Test with tls_certkey_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_type="TLS")

        self.assertIsNone(mongo.ssl_client_phrase)

    def test_tls_cert_key2(self):

        """Function:  test_tls_cert_key2

        Description:  Test with tls_cert_key attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, tls_certkey=self.tls_certkey, auth_type="TLS")

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    def test_tls_cert_key(self):

        """Function:  test_tls_cert_key

        Description:  Test with no tls_cert_key attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_type="TLS")

        self.assertIsNone(mongo.tls_certkey)

    def test_tls_client_ca2(self):

        """Function:  test_tls_client_ca2

        Description:  Test with tls_ca_certs attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, tls_ca_certs=self.tls_ca_certs,
            auth_type="TLS")

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    def test_tls_ca_certs(self):

        """Function:  test_tls_ca_certs

        Description:  Test with no tls_ca_certs attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_type="TLS")

        self.assertIsNone(mongo.tls_ca_certs)


if __name__ == "__main__":
    unittest.main()
