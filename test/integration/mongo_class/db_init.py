# Classification (U)

"""Program:  db_init.py

    Description:  Integration testing of DB.__init__ in mongo_class.py.

    Usage:
        test/integration/mongo_class/db_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class
import lib.gen_libs as gen_libs
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
        test_auth_type_none
        test_auth_type_ssl
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
        test_ssl_all_phrase2
        test_ssl_all_phrase
        test_ssl_all2
        test_ssl_all
        test_ssl_client_key_phrase2
        test_ssl_client_key_phrase
        test_ssl_client_key_cert3
        test_ssl_client_key_cert2
        test_ssl_client_key_cert
        test_ssl_client_ca8
        test_ssl_client_ca7
        test_ssl_client_ca6
        test_ssl_client_ca5
        test_ssl_client_ca4
        test_ssl_client_ca3
        test_ssl_client_phrase2
        test_ssl_client_phrase
        test_ssl_client_cert2
        test_ssl_client_cert
        test_ssl_client_key2
        test_ssl_client_key
        test_ssl_client_ca2
        test_ssl_client_ca
        test_set_pass
        test_auth_mech2
        test_auth_mech
        test_default_auth_mech
        test_uptime_attr
        test_port_attr
        test_host_attr
        test_japd_attr
        test_user_attr
        test_name_attr
        test_log_path_attr
        test_db_path_attr
        test_conn_attr
        test_config_attr3
        test_config_attr2
        test_no_db_name_attr
        test_db_name_attr
        test_default_conf_file
        test_using_conf_file
        test_default_auth
        test_using_auth
        test_conn_list_attr
        test_config_attr
        test_default_auth_db
        test_using_auth_db
        test_default

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

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
        self.conn_list = [self.cfg.host + ":" + str(self.cfg.port)]
        self.db_name = "admin"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.conf_file = "MyConf"

        self.config = {}
        self.config[KEY1 + KEY2] = self.cfg.japd

        self.config2 = {}
        self.config2[KEY1 + KEY2] = self.cfg.japd
        self.config2["authMechanism"] = self.auth_mech2

        self.config3 = {}
        self.config3[KEY1 + KEY2] = self.cfg.japd
        self.config3["authMechanism"] = self.auth_mech2
        self.config3["ssl"] = True
        self.config3["ssl_ca_certs"] = self.ssl_client_ca

        self.config4 = {}
        self.config4[KEY1 + KEY2] = self.cfg.japd
        self.config4["authMechanism"] = self.auth_mech2
        self.config4["ssl"] = True
        self.config4["ssl_keyfile"] = self.ssl_client_key
        self.config4["ssl_certfile"] = self.ssl_client_cert

        self.config5 = {}
        self.config5[KEY1 + KEY2] = self.cfg.japd
        self.config5["authMechanism"] = self.auth_mech2
        self.config5["ssl"] = True
        self.config5["ssl_keyfile"] = self.ssl_client_key
        self.config5["ssl_certfile"] = self.ssl_client_cert
        self.config5[KEY3 + KEY1 + KEY4] = self.ssl_client_phrase

        self.config6 = {}
        self.config6[KEY1 + KEY2] = self.cfg.japd
        self.config6["authMechanism"] = self.auth_mech2
        self.config6["ssl"] = True
        self.config6["ssl_ca_certs"] = self.ssl_client_ca
        self.config6["ssl_keyfile"] = self.ssl_client_key
        self.config6["ssl_certfile"] = self.ssl_client_cert

        self.config7 = {}
        self.config7[KEY1 + KEY2] = self.cfg.japd
        self.config7["authMechanism"] = self.auth_mech2
        self.config7["ssl"] = True
        self.config7["ssl_ca_certs"] = self.ssl_client_ca
        self.config7["ssl_keyfile"] = self.ssl_client_key
        self.config7["ssl_certfile"] = self.ssl_client_cert
        self.config7[KEY3 + KEY1 + KEY4] = self.ssl_client_phrase


        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertificationKeyFile"
        self.tls_certkey_phrase = "tlsCertificationKeyFilePassword"

        config = dict()
        config["password"] = self.japd
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

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config7)

    def test_auth_type_ssl(self):

        """Function:  test_auth_type_tls

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase, auth_type="SSL")

        self.assertEqual(mongo.config, self.config7)

    def test_auth_type_tls(self):

        """Function:  test_auth_type_tls

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey,
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

        mongo = mongo_class.DB(
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

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey=self.tls_certkey, auth_type="TLS")

        self.assertEqual(mongo.config, self.config6a)

    def test_tls_cert_key_config2(self):

        """Function:  test_tls_cert_key_config2

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_certkey=self.tls_certkey,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config5a)

    def test_tls_cert_key_config(self):

        """Function:  test_tls_cert_key_config

        Description:  Test with tls_cert_key_config with config attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_certkey=self.tls_certkey,
            auth_type="TLS")

        self.assertEqual(mongo.config, self.config4a)

    def test_tls_ca_certs_config2(self):

        """Function:  test_tls_ca_certs_config2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)

    def test_tls_ca_certs_config(self):

        """Function:  test_tls_ca_certs_config

        Description:  Test with tls_ca_certs with config attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, tls_ca_certs=self.tls_ca_certs,
            auth_type="TLS")

        self.assertEqual(mongo.config, self.config3a)

    def test_tls_certkey_phrase2(self):

        """Function:  test_tls_certkey_phrase2

        Description:  Test with tls_certkey_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            tls_certkey_phrase=self.tls_certkey_phrase, auth_type="TLS")

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    def test_tls_certkey_phrase(self):

        """Function:  test_tls_certkey_phrase

        Description:  Test with tls_certkey_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_type="TLS")

        self.assertEqual(mongo.ssl_client_phrase, None)

    def test_tls_cert_key2(self):

        """Function:  test_tls_cert_key2

        Description:  Test with tls_cert_key attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            tls_certkey=self.tls_certkey, auth_type="TLS")

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    def test_tls_cert_key(self):

        """Function:  test_tls_cert_key

        Description:  Test with no tls_cert_key attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_type="TLS")

        self.assertEqual(mongo.tls_certkey, None)

    def test_tls_client_ca2(self):

        """Function:  test_tls_client_ca2

        Description:  Test with tls_ca_certs attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            tls_ca_certs=self.tls_ca_certs, auth_type="TLS")

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    def test_tls_ca_certs(self):

        """Function:  test_tls_ca_certs

        Description:  Test with no tls_ca_certs attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_type="TLS")

        self.assertEqual(mongo.tls_ca_certs, None)

    def test_ssl_all_phrase2(self):

        """Function:  test_ssl_all_phrase2

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config7)

    def test_ssl_all_phrase(self):

        """Function:  test_ssl_all_phrase

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
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

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config6)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
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

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config5)

    def test_ssl_client_key_phrase(self):

        """Function:  test_ssl_client_key_phrase

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.ssl_client_phrase, self.ssl_client_phrase)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.config, self.config4)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_phrase), (None, None))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca8(self):

        """Function:  test_ssl_client_ca8

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca7(self):

        """Function:  test_ssl_client_ca7

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca6(self):

        """Function:  test_ssl_client_ca6

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca5(self):

        """Function:  test_ssl_client_ca5

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca4(self):

        """Function:  test_ssl_client_ca4

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert,
             mongo.ssl_client_phrase), (None, None, None))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_ca3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.conf_file,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_phrase2(self):

        """Function:  test_ssl_client_phrase2

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.ssl_client_phrase, self.ssl_client_phrase)

    def test_ssl_client_phrase(self):

        """Function:  test_ssl_client_phrase

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_phrase, None)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.ssl_client_cert, self.ssl_client_cert)

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_cert, None)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.ssl_client_key, self.ssl_client_key)

    def test_test_ssl_client_key(self):

        """Function:  test_test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_key, None)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_ca, None)

    def test_set_pass(self):

        """Function:  test_set_pass

        Description:  Test setting configuration settings.

        Arguments:

        """

        global KEY1
        global KEY2

        config = {KEY1 + KEY2: self.cfg.japd}
        config["authMechanism"] = self.auth_mech2
        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file=self.cfg.conf_file)

        self.assertEqual(mongo.config, config)

    def test_auth_mech2(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    def test_auth_mech(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_default_auth_mech(self):

        """Function:  test_default_auth_mech

        Description:  Test auth_mech default setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_uptime_attr(self):

        """Function:  test_uptime_attr

        Description:  Test uptime attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.uptime)

    def test_port_attr(self):

        """Function:  test_port_attr

        Description:  Test port attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.port, self.cfg.port)

    def test_host_attr(self):

        """Function:  test_host_attr

        Description:  Test host attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.host, self.cfg.host)

    def test_japd_attr(self):

        """Function:  test_japd_attr

        Description:  Test japd attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.japd, self.cfg.japd)

    def test_user_attr(self):

        """Function:  test_user_attr

        Description:  Test user attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.user, self.cfg.user)

    def test_name_attr(self):

        """Function:  test_name_attr

        Description:  Test name attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.name, self.cfg.name)

    def test_log_path_attr(self):

        """Function:  test_log_path_attr

        Description:  Test log_path attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.log_path)

    def test_db_path_attr(self):

        """Function:  test_db_path_attr

        Description:  Test db_path attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.db_path)

    def test_conn_attr(self):

        """Function:  test_conn_attr

        Description:  Test conn attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.conn)

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_no_db_name_attr(self):

        """Function:  test_no_db_name_attr

        Description:  Test no db_name attribute passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.db_name, "test")

    def test_db_name_attr(self):

        """Function:  test_db_name_attr

        Description:  Test db_name attribute passed.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, db=self.db_name)

        self.assertEqual(mongo.db_name, self.db_name)

    def test_default_conf_file(self):

        """Function:  test_default_conf_file

        Description:  Test using the default conf_file setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.conf_file)

    def test_using_conf_file(self):

        """Function:  test_using_conf_file

        Description:  Test using the conf_file connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file="myfile")

        self.assertEqual(mongo.conf_file, "myfile")

    def test_default_auth(self):

        """Function:  test_default_auth

        Description:  Test using the default auth setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertTrue(mongo.auth)

    def test_using_auth(self):

        """Function:  test_using_auth

        Description:  Test using the auth connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False)

        self.assertFalse(mongo.auth)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.DB(self.cfg.name, self.cfg.user, self.cfg.japd,
                               host=self.cfg.host, port=self.cfg.port)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.DB(self.cfg.name, self.cfg.user, self.cfg.japd,
                               host=self.cfg.host, port=self.cfg.port)

        self.assertEqual(mongo.config, self.config2)

    def test_default_auth_db(self):

        """Function:  test_default_auth_db

        Description:  Test using the default auth_db setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.auth_db, self.cfg.auth_db)

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_db=self.cfg.auth_db)

        self.assertEqual(mongo.auth_db, self.cfg.auth_db)

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.cfg.name, self.cfg.user, self.cfg.japd,
                               host=self.cfg.host, port=self.cfg.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.cfg.name, self.cfg.user, self.cfg.japd, self.cfg.host,
             self.cfg.port))


if __name__ == "__main__":
    unittest.main()
