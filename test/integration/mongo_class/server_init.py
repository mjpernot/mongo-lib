#!/usr/bin/python
# Classification (U)

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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mongo_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "word"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_ssl_all_phrase2 -> Test with all ssl arguments and phrase present.
        test_ssl_all_phrase -> Test with all ssl arguments and phrase present.
        test_ssl_all2 -> Test with all ssl arguments present.
        test_ssl_all -> Test with all ssl arguments present.
        test_ssl_client_key_phrase2 -> Test with cert, key and phrase present.
        test_ssl_client_key_phrase -> Test with cert, key and phrase present.
        test_ssl_client_key_cert3 -> Test with both cert and key present.
        test_ssl_client_key_cert2 -> Test with both cert and key present.
        test_ssl_client_key_cert -> Test with both cert and key present.
        test_ssl_client_ca8 -> Test with ssl_client_ca only present.
        test_ssl_client_ca7 -> Test with ssl_client_ca only present.
        test_ssl_client_ca6 -> Test with ssl_client_ca only present.
        test_ssl_client_ca5 -> Test with ssl_client_ca only present.
        test_ssl_client_ca4 -> Test with ssl_client_ca only present.
        test_ssl_client_ca3 -> Test with ssl_client_ca only present.
        test_ssl_client_phrase2 -> Test with ssl_client_phrase attribute.
        test_ssl_client_phrase -> Test with ssl_client_phrase attribute.
        test_ssl_client_cert2 -> Test with ssl_client_cert attribute.
        test_ssl_client_cert -> Test with ssl_client_cert attribute.
        test_ssl_client_key2 -> Test with ssl_client_key attribute.
        test_ssl_client_key -> Test with ssl_client_key attribute.
        test_ssl_client_ca2 -> Test with ssl_client_ca attribute.
        test_ssl_client_ca -> Test with ssl_client_ca attribute.
        test_set_pass -> Test with default config settings.
        test_config_attr3 -> Test with SCRAM-SHA-1 setting.
        test_config_attr2 -> Test with MONGODB-CR setting.
        test_auth_mech -> Test passing arg to auth_mech attribute.
        test_default_auth_mech -> Test auth_mech default setting.
        test_uptime_attr -> Test uptime attribute.
        test_port_attr -> Test port attribute.
        test_host_attr -> Test host attribute.
        test_japd_attr -> Test japd attribute.
        test_user_attr -> Test user attribute.
        test_name_attr -> Test name attribute.
        test_log_path_attr -> Test log_path attribute.
        test_db_path_attr -> Test db_path attribute.
        test_conn_attr -> Test conn attribute.
        test_no_conf_file_attr -> Test no conf_file attribute passed.
        test_conf_file_attr -> Test conf_file attribute passed.
        test_default_auth -> Test using the default auth setting.
        test_using_auth -> Test using the auth connection.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_no_auth_db -> Test using no auth_db attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_no_using_arg -> Test with auth and no arg present.
        test_using_arg -> Test using the arg connection.
        test_no_auth_uri -> Test with auth and no uri present.
        test_using_uri -> Test using the uri connection.
        test_auth_false -> Test with auth passed as False.
        test_auth_true -> Test with auth passed as True.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        global KEY1
        global KEY2

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mongo"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        key1 = "pass"
        key2 = "word"
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
        self.config = {key1 + key2: self.cfg.japd}
        self.config2 = {key1 + key2: self.cfg.japd,
                        "authMechanism": self.auth_mech2}
        self.conn_list = [self.cfg.host + ":" + str(self.cfg.port)]

        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"

        self.config = {}
        self.config[KEY1 + KEY2] = self.japd

        self.config2 = {}
        self.config2[KEY1 + KEY2] = self.japd
        self.config2["authMechanism"] = self.auth_mech2

        self.config3 = {}
        self.config3[KEY1 + KEY2] = self.japd
        self.config3["authMechanism"] = self.auth_mech2
        self.config3["ssl_ca_certs"] = "CAFile"

        self.config4 = {}
        self.config4[KEY1 + KEY2] = self.japd
        self.config4["authMechanism"] = "SCRAM-SHA-1"
        self.config4["ssl_keyfile"] = "KeyFile"
        self.config4["ssl_certfile"] = "CertFile"

        self.config5 = {}
        self.config5[KEY1 + KEY2] = self.japd
        self.config5["authMechanism"] = "SCRAM-SHA-1"
        self.config5["ssl_keyfile"] = "KeyFile"
        self.config5["ssl_certfile"] = "CertFile"
        self.config5["ssl_pem_passphrase"] = "MyPhrase"

        self.config6 = {}
        self.config6[KEY1 + KEY2] = self.japd
        self.config6["authMechanism"] = "SCRAM-SHA-1"
        self.config6["ssl_ca_certs"] = "CAFile"
        self.config6["ssl_keyfile"] = "KeyFile"
        self.config6["ssl_certfile"] = "CertFile"

        self.config7 = {}
        self.config7[KEY1 + KEY2] = self.japd
        self.config7["authMechanism"] = "SCRAM-SHA-1"
        self.config7["ssl_ca_certs"] = "CAFile"
        self.config7["ssl_keyfile"] = "KeyFile"
        self.config7["ssl_certfile"] = "CertFile"
        self.config7["ssl_pem_passphrase"] = "MyPhrase"

    def test_ssl_all_phrase2(self):

        """Function:  test_ssl_all_phrase2

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config7)

    def test_ssl_all_phrase(self):

        """Function:  test_ssl_all_phrase

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert, mongo.ssl_client_sa,
            mongo.ssl_client_phrase),
            (self.ssl_client_key, self.ssl_client_cert, self.ssl_client_sa,
            self.ssl_client_phrase))

    def test_ssl_all2(self):

        """Function:  test_ssl_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config6)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
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
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config5)

    def test_ssl_client_key_phrase(self):

        """Function:  test_ssl_client_key_phrase

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.ssl_client_phrase, self.ssl_client_phrase)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.config, self.config4)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_phrase), (None, None))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca8(self):

        """Function:  test_ssl_client_ca8

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca7(self):

        """Function:  test_ssl_client_ca7

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca6(self):

        """Function:  test_ssl_client_ca6

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca5(self):

        """Function:  test_ssl_client_ca5

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca4(self):

        """Function:  test_ssl_client_ca4

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert,
             mongo.ssl_client_phrase), (None, None, None))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_ca3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_phrase2(self):

        """Function:  test_ssl_client_phrase2

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_phrase="Phrase")

        self.assertEqual(mongo.ssl_client_phrase, "Phrase")

    def test_ssl_client_phrase(self):

        """Function:  test_ssl_client_phrase

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_phrase, None)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_cert="CertFile")

        self.assertEqual(mongo.ssl_client_cert, "CertFile")

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_cert, None)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_key="KeyFile")

        self.assertEqual(mongo.ssl_client_key, "KeyFile")

    def test_test_ssl_client_key(self):

        """Function:  test_test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_key, None)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, ssl_client_ca="CAFile")

        self.assertEqual(mongo.ssl_client_ca, "CAFile")

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.ssl_client_ca, None)

    def test_set_pass(self):

        """Function:  test_set_pass

        Description:  Test setting configuration settings.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_auth_mech(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_default_auth_mech(self):

        """Function:  test_default_auth_mech

        Description:  Test auth_mech default setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_uptime_attr(self):

        """Function:  test_uptime_attr

        Description:  Test uptime attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.uptime)

    def test_port_attr(self):

        """Function:  test_port_attr

        Description:  Test port attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.port, self.cfg.port)

    def test_host_attr(self):

        """Function:  test_host_attr

        Description:  Test host attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.host, self.cfg.host)

    def test_japd_attr(self):

        """Function:  test_japd_attr

        Description:  Test japd attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.japd, self.cfg.japd)

    def test_user_attr(self):

        """Function:  test_user_attr

        Description:  Test user attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.user, self.cfg.user)

    def test_name_attr(self):

        """Function:  test_name_attr

        Description:  Test name attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.name, self.cfg.name)

    def test_log_path_attr(self):

        """Function:  test_log_path_attr

        Description:  Test log_path attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.log_path)

    def test_db_path_attr(self):

        """Function:  test_db_path_attr

        Description:  Test db_path attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.db_path)

    def test_conn_attr(self):

        """Function:  test_conn_attr

        Description:  Test conn attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.conn)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, conf_file="myfile")

        self.assertEqual(mongo.conf_file, "myfile")

    def test_default_auth(self):

        """Function:  test_default_auth

        Description:  Test using the default auth setting.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertTrue(mongo.auth)

    def test_using_auth(self):

        """Function:  test_using_auth

        Description:  Test using the auth connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False)

        self.assertFalse(mongo.auth)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.config, self.config2)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mongo.auth_db, self.cfg.auth_db)

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth_db=self.cfg.auth_db)

        self.assertEqual(mongo.auth_db, self.cfg.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test using the arg connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.use_uri)

    def test_using_uri(self):

        """Function:  test_using_uri

        Description:  Test using the uri connection.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=True)

        self.assertTrue(mongo.use_uri)

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth passed as False.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, auth=False)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.cfg.name, self.cfg.user, self.cfg.japd,
                          self.cfg.host, self.cfg.port, False))

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth passed as True.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port, mongo.auth),
                         (self.cfg.name, self.cfg.user, self.cfg.japd,
                          self.cfg.host, self.cfg.port, True))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual((mongo.name, mongo.user, mongo.japd, mongo.host,
                          mongo.port),
                         (self.cfg.name, self.cfg.user, self.cfg.japd,
                          self.cfg.host, self.cfg.port))


if __name__ == "__main__":
    unittest.main()
