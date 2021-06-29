#!/usr/bin/python
# Classification (U)

"""Program:  masterrep_init.py

    Description:  Unit testing of MasterRep.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/masterrep_init.py

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
        test_slaves_attr
        test_repset_attr
        test_issecondary_attr
        test_ismaster_attr
        test_no_conf_file_attr
        test_conf_file_attr
        test_conn_list_attr
        test_config_attr
        test_using_no_auth_db
        test_using_auth_db
        test_no_using_arg
        test_using_arg
        test_no_auth_uri
        test_auth_uri
        test_auth_false
        test_auth_true
        test_no_auth

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        global KEY1
        global KEY2

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config file"
        self.auth_mech = "MONGODB-CR"
        self.auth_mech2 = "SCRAM-SHA-1"
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
        self.config3["ssl_ca_certs"] = self.ssl_client_ca

        self.config4 = {}
        self.config4[KEY1 + KEY2] = self.japd
        self.config4["authMechanism"] = self.auth_mech2
        self.config4["ssl_keyfile"] = self.ssl_client_key
        self.config4["ssl_certfile"] = self.ssl_client_cert

        self.config5 = {}
        self.config5[KEY1 + KEY2] = self.japd
        self.config5["authMechanism"] = self.auth_mech2
        self.config5["ssl_keyfile"] = self.ssl_client_key
        self.config5["ssl_certfile"] = self.ssl_client_cert
        self.config5["ssl_pem_passphrase"] = self.ssl_client_phrase

        self.config6 = {}
        self.config6[KEY1 + KEY2] = self.japd
        self.config6["authMechanism"] = self.auth_mech2
        self.config6["ssl_ca_certs"] = self.ssl_client_ca
        self.config6["ssl_keyfile"] = self.ssl_client_key
        self.config6["ssl_certfile"] = self.ssl_client_cert

        self.config7 = {}
        self.config7[KEY1 + KEY2] = self.japd
        self.config7["authMechanism"] = self.auth_mech2
        self.config7["ssl_ca_certs"] = self.ssl_client_ca
        self.config7["ssl_keyfile"] = self.ssl_client_key
        self.config7["ssl_certfile"] = self.ssl_client_cert
        self.config7["ssl_pem_passphrase"] = self.ssl_client_phrase

    def test_ssl_all_phrase2(self):

        """Function:  test_ssl_all_phrase2

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config7)

    def test_ssl_all_phrase(self):

        """Function:  test_ssl_all_phrase

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config6)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config5)

    def test_ssl_client_key_phrase(self):

        """Function:  test_ssl_client_key_phrase

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.config, self.config4)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
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

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca8(self):

        """Function:  test_ssl_client_ca8

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca7(self):

        """Function:  test_ssl_client_ca7

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca6(self):

        """Function:  test_ssl_client_ca6

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca5(self):

        """Function:  test_ssl_client_ca5

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca4(self):

        """Function:  test_ssl_client_ca4

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert,
             mongo.ssl_client_phrase), (None, None, None))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_ca3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_phrase2(self):

        """Function:  test_ssl_client_phrase2

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_phrase="Phrase")

        self.assertEqual(mongo.ssl_client_phrase, "Phrase")

    def test_ssl_client_phrase(self):

        """Function:  test_ssl_client_phrase

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.ssl_client_phrase, None)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mongo.ssl_client_cert, self.ssl_client_cert)

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.ssl_client_cert, None)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_key=self.ssl_client_key)

        self.assertEqual(mongo.ssl_client_key, self.ssl_client_key)

    def test_test_ssl_client_key(self):

        """Function:  test_test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.ssl_client_key, None)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.ssl_client_ca, None)

    def test_set_pass(self):

        """Function:  test_set_pass

        Description:  Test setting configuration settings.

        Arguments:

        """

        global KEY1
        global KEY2

        config = {KEY1 + KEY2: self.japd}
        config["authMechanism"] = self.auth_mech2
        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)

        self.assertEqual(mongo.config, config)

    def test_auth_mech2(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    def test_auth_mech(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech2)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_default_auth_mech(self):

        """Function:  test_default_auth_mech

        Description:  Test auth_mech default setting.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_uptime_attr(self):

        """Function:  test_uptime_attr

        Description:  Test uptime attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.uptime)

    def test_port_attr(self):

        """Function:  test_port_attr

        Description:  Test port attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.port, self.port)

    def test_host_attr(self):

        """Function:  test_host_attr

        Description:  Test host attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.host, self.host)

    def test_japd_attr(self):

        """Function:  test_japd_attr

        Description:  Test japd attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.japd, self.japd)

    def test_user_attr(self):

        """Function:  test_user_attr

        Description:  Test user attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.user, self.user)

    def test_name_attr(self):

        """Function:  test_name_attr

        Description:  Test name attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.name, self.name)

    def test_log_path_attr(self):

        """Function:  test_log_path_attr

        Description:  Test log_path attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.log_path)

    def test_db_path_attr(self):

        """Function:  test_db_path_attr

        Description:  Test db_path attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.db_path)

    def test_conn_attr(self):

        """Function:  test_conn_attr

        Description:  Test conn attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertFalse(mongo.conn)

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_slaves_attr(self):

        """Function:  test_slaves_attr

        Description:  Test slaves attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertFalse(mongo.slaves)

    def test_repset_attr(self):

        """Function:  test_repset_attr

        Description:  Test repset attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertFalse(mongo.repset)

    def test_issecondary_attr(self):

        """Function:  test_issecondary_attr

        Description:  Test issecondary attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertFalse(mongo.issecondary)

    def test_ismaster_attr(self):

        """Function:  test_ismaster_attr

        Description:  Test ismaster attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertFalse(mongo.ismaster)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db, conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(mongo.config, self.config2)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.use_uri)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(
            self.name, self.user, self.japd, self.host, self.port,
            use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_auth_false(self):

        """Function:  test_auth_false

        Description:  Test with auth passed as False.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port, auth=False)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary, mongo.auth),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None, False))

    def test_auth_true(self):

        """Function:  test_auth_true

        Description:  Test with auth passed as True.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port, auth=True)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary, mongo.auth),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None, True))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.MasterRep(self.name, self.user, self.japd,
                                      self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None))


if __name__ == "__main__":
    unittest.main()
