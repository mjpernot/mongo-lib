#!/usr/bin/python
# Classification (U)

"""Program:  repsetcoll_init.py

    Description:  Unit testing of RepSetColl.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_init.py

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
        test_auth_mech2 -> Test passing arg to auth_mech attribute.
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
        test_config_attr3 -> Test with SCRAM-SHA-1 setting.
        test_config_attr2 -> Test with MONGODB-CR setting.
        test_db_auth_conn_attr -> Test db_auth_conn attribute.
        test_db_coll_attr -> Test db_coll attribute.
        test_db_conn_attr -> Test db_conn attribute.
        test_no_repset_hosts_attr -> Test no repset_hosts attribute passed.
        test_repset_hosts_attr -> Test repset_hosts attribute passed.
        test_no_repset_attr -> Test no repset attribute passed.
        test_repset_attr -> Test repset attribute passed.
        test_no_conf_file_attr -> Test no conf_file attribute passed.
        test_conf_file_attr -> Test conf_file attribute passed.
        test_no_auth_attr -> Test with auth attribute passed.
        test_auth_attr2 -> Test with auth attribute False.
        test_auth_attr -> Test with auth attribute True.
        test_db_auth_attr -> Test db_auth attribute passed.
        test_no_db_auth_attr -> Test no db_auth attribute passed.
        test_coll_attr -> Test coll attribute passed.
        test_no_coll_attr -> Test no coll attribute passed.
        test_db_attr -> Test db attribute passed.
        test_no_db_attr -> Test no db attribute passed.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_using_no_auth_db -> Test using no auth_db attribute.
        test_using_auth_db -> Test using the auth_db attribute.
        test_no_using_arg -> Test with auth and no arg present.
        test_using_arg -> Test with auth and arg present.
        test_no_auth_uri -> Test with auth and no uri present.
        test_auth_uri -> Test with auth and uri present.
        test_no_auth -> Test with no auth present.

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
        self.db_auth = "minedb1"
        self.repset = "mongo_repset"
        self.use_uri = True
        self.use_arg = True
        self.auth_db = "sysmon"
        self.mydb = "minedb"
        self.mycoll = "minecollection"
        self.conn_list = [self.host + ":" + str(self.port)]
        self.conf_file = "Config File"
        self.repset_hosts = ["host1:port", "host2:port"]
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

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config7)

    def test_ssl_all_phrase(self):

        """Function:  test_ssl_all_phrase

        Description:  Test with all ssl arguments and phrase present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

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

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config6)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca, coll=self.coll,
            repset=self.repset)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_ca, self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_key_phrase2(self):

        """Function:  test_ssl_client_key_phrase2

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config5)

    def test_ssl_client_key_phrase(self):

        """Function:  test_ssl_client_key_phrase

        Description:  Test with cert, key and phrase present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.ssl_client_phrase, self.ssl_client_phrase)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config4)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert, coll=self.coll,
            repset=self.repset)

        self.assertEqual(
            (mongo.ssl_client_ca, mongo.ssl_client_phrase), (None, None))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert, coll=self.coll,
            repset=self.repset)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca8(self):

        """Function:  test_ssl_client_ca8

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca7(self):

        """Function:  test_ssl_client_ca7

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_phrase=self.ssl_client_phrase, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca6(self):

        """Function:  test_ssl_client_ca6

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca5(self):

        """Function:  test_ssl_client_ca5

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.config, self.config3)

    def test_ssl_client_ca4(self):

        """Function:  test_ssl_client_ca4

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            coll=self.coll, repset=self.repset)

        self.assertEqual(
            (mongo.ssl_client_key, mongo.ssl_client_cert,
             mongo.ssl_client_phrase), (None, None, None))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_ca3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, ssl_client_ca=self.ssl_client_ca,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_phrase2(self):

        """Function:  test_ssl_client_phrase2

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_phrase="Phrase", coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.ssl_client_phrase, "Phrase")

    def test_ssl_client_phrase(self):

        """Function:  test_ssl_client_phrase

        Description:  Test with ssl_client_phrase attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.ssl_client_phrase, None)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_cert=self.ssl_client_cert, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.ssl_client_cert, self.ssl_client_cert)

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.ssl_client_cert, None)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_key=self.ssl_client_key, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.ssl_client_key, self.ssl_client_key)

    def test_test_ssl_client_key(self):

        """Function:  test_test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.ssl_client_key, None)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            ssl_client_ca=self.ssl_client_ca, coll=self.coll,
            repset=self.repset)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

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
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file, coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.config, config)

    def test_auth_mech2(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech, coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.auth_mech, self.auth_mech)

    def test_auth_mech(self):

        """Function:  test_auth_mech

        Description:  Test passing arg to auth_mech attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth_mech=self.auth_mech2, coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_default_auth_mech(self):

        """Function:  test_default_auth_mech

        Description:  Test auth_mech default setting.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.auth_mech, self.auth_mech2)

    def test_uptime_attr(self):

        """Function:  test_uptime_attr

        Description:  Test uptime attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertFalse(mongo.uptime)

    def test_port_attr(self):

        """Function:  test_port_attr

        Description:  Test port attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.port, self.port)

    def test_host_attr(self):

        """Function:  test_host_attr

        Description:  Test host attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.host, self.host)

    def test_japd_attr(self):

        """Function:  test_japd_attr

        Description:  Test japd attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.japd, self.japd)

    def test_user_attr(self):

        """Function:  test_user_attr

        Description:  Test user attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.user, self.user)

    def test_name_attr(self):

        """Function:  test_name_attr

        Description:  Test name attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertEqual(mongo.name, self.name)

    def test_log_path_attr(self):

        """Function:  test_log_path_attr

        Description:  Test log_path attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertFalse(mongo.log_path)

    def test_db_path_attr(self):

        """Function:  test_db_path_attr

        Description:  Test db_path attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertFalse(mongo.db_path)

    def test_conn_attr(self):

        """Function:  test_conn_attr

        Description:  Test conn attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            coll=self.coll, repset=self.repset)

        self.assertFalse(mongo.conn)

    def test_config_attr3(self):

        """Function:  test_config_attr3

        Description:  Test with SCRAM-SHA-1 setting.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_mech=self.auth_mech2)

        self.assertEqual(mongo.config, self.config2)

    def test_config_attr2(self):

        """Function:  test_config_attr2

        Description:  Test with MONGODB-CR setting.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_mech=self.auth_mech)

        self.assertEqual(mongo.config, self.config)

    def test_db_auth_conn_attr(self):

        """Function:  test_db_auth_conn_attr

        Description:  Test db_auth attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_auth)

    def test_db_coll_attr(self):

        """Function:  test_db_coll_attr

        Description:  Test db_coll attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_coll)

    def test_db_conn_attr(self):

        """Function:  test_db_conn_attr

        Description:  Test db_conn attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertFalse(mongo.db_conn)

    def test_no_repset_hosts_attr(self):

        """Function:  test_no_repset_hosts_attr

        Description:  Test no repset_hosts attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.repset_hosts)

    def test_repset_hosts_attr(self):

        """Function:  test_repset_hosts_attr

        Description:  Test repset_hosts attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset_hosts=self.repset_hosts)

        self.assertEqual(mongo.repset_hosts, self.repset_hosts)

    def test_no_repset_attr(self):

        """Function:  test_no_repset_attr

        Description:  Test no repset attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port)

        self.assertFalse(mongo.repset)

    def test_repset_attr(self):

        """Function:  test_repset_attr

        Description:  Test repset attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.repset, self.repset)

    def test_no_conf_file_attr(self):

        """Function:  test_no_conf_file_attr

        Description:  Test no conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.conf_file)

    def test_conf_file_attr(self):

        """Function:  test_conf_file_attr

        Description:  Test conf_file attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, conf_file=self.conf_file)

        self.assertEqual(mongo.conf_file, self.conf_file)

    def test_no_auth_attr(self):

        """Function:  test_no_auth_attr

        Description:  Test no auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertTrue(mongo.auth)

    def test_auth_attr2(self):

        """Function:  test_auth_attr2

        Description:  Test auth attribute False.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertFalse(mongo.auth)

    def test_auth_attr(self):

        """Function:  test_auth_attr

        Description:  Test auth attribute True.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertTrue(mongo.auth)

    def test_db_auth_attr(self):

        """Function:  test_db_auth_attr

        Description:  Test db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, db_auth=self.db_auth)

        self.assertEqual(mongo.db_auth, self.db_auth)

    def test_no_db_auth_attr(self):

        """Function:  test_no_db_auth_attr

        Description:  Test no db_auth attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db_auth, None)

    def test_coll_attr(self):

        """Function:  test_coll_attr

        Description:  Test coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, coll=self.mycoll)

        self.assertEqual(mongo.coll, self.mycoll)

    def test_no_coll_attr(self):

        """Function:  test_no_coll_attr

        Description:  Test no coll attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.coll, None)

    def test_db_attr(self):

        """Function:  test_db_attr

        Description:  Test db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, db=self.mydb)

        self.assertEqual(mongo.db, self.mydb)

    def test_no_db_attr(self):

        """Function:  test_no_db_attr

        Description:  Test no db attribute passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.db, "test")

    def test_conn_list_attr(self):

        """Function:  test_conn_list_attr

        Description:  Test setting the conn_list attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.conn_list, self.conn_list)

    def test_config_attr(self):

        """Function:  test_config_attr

        Description:  Test setting the config attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.config, self.config2)

    def test_using_no_auth_db(self):

        """Function:  test_using_no_auth_db

        Description:  Test using no auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(mongo.auth_db, "admin")

    def test_using_auth_db(self):

        """Function:  test_using_auth_db

        Description:  Test using the auth_db attribute.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth_db=self.auth_db)

        self.assertEqual(mongo.auth_db, self.auth_db)

    def test_no_using_arg(self):

        """Function:  test_no_using_arg

        Description:  Test with auth and no arg present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, use_arg=self.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_no_auth_uri(self):

        """Function:  test_no_auth_uri

        Description:  Test with auth and no uri present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertFalse(mongo.use_uri)

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, use_uri=self.use_uri)

        self.assertTrue(mongo.use_uri)

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.db, mongo.coll, mongo.repset),
            (self.name, self.user, self.japd, self.host, self.port, self.dbs,
             self.coll, self.repset))


if __name__ == "__main__":
    unittest.main()
