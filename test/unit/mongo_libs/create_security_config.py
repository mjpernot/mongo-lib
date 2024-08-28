# Classification (U)

"""Program:  create_security_config.py

    Description:  Unit testing of create_security_config in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/create_security_config.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs
import version

__version__ = version.__version__


class Cfg(object):

    """Class:  Cfg

    Description:  Class stub holder for Cfg class.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

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
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"


class Cfg2(object):

    """Class:  Cfg2

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

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
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg3(object):

    """Class:  Cfg3

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

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
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg4(object):

    """Class:  Cfg4

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

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
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.auth_type = "SSL"
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg5(object):

    """Class:  Cfg5

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

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
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = "TLS"
        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertKeyFile"
        self.tls_certkey_phrase = "tlsCertKeyPhrase"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_cfg_passed
        test_set_tls_certkey_phrase
        test_set_tls_certkey
        test_set_tls_ca_certs2
        test_set_tls_ca_certs
        test_auth_type_tls
        test_auth_type_ssl
        test_auth_type_none
        test_coll_set_ssl
        test_rep_set_ssl
        test_coll_none_ssl
        test_rep_none_ssl
        test_coll_no_ssl
        test_rep_no_ssl

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repset_hosts = "host:port"
        self.tls_ca_certs = "tlsCAFile"
        self.auth_type = "TLS"
        self.cfg_file = "cfg_file"
        self.dir_path = "dir_path"
        self.cfg5 = Cfg5()
        self.tls_certkey = "tlsCertKeyFile"
        self.tls_certkey_phrase = "tlsCertKeyPhrase"

    def test_no_cfg_passed(self):

        """Function:  test_no_cfg_passed

        Description:  Test with no config objects passed.

        Arguments:

        """

        mongo = mongo_libs.create_security_config()

        self.assertFalse(mongo)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase(self, mock_load):

        """Function:  test_set_tls_certkey_phrase

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5

        mongo = mongo_libs.create_security_config(
            cfg_file=self.cfg_file, dir_path=self.dir_path)

        self.assertEqual(mongo["tls_certkey_phrase"], self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey(self, mock_load):

        """Function:  test_set_tls_certkey

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5

        mongo = mongo_libs.create_security_config(
            cfg_file=self.cfg_file, dir_path=self.dir_path)

        self.assertEqual(mongo["tls_certkey"], self.tls_certkey)

    def test_set_tls_ca_certs2(self):

        """Function:  test_set_tls_ca_certs2

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        cfg = Cfg5(self.repset_hosts)
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["tls_ca_certs"], self.tls_ca_certs)

    def test_set_tls_ca_certs(self):

        """Function:  test_set_tls_ca_certs

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        cfg = Cfg5()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["tls_ca_certs"], self.tls_ca_certs)

    def test_auth_type_tls(self):

        """Function:  test_auth_type_tls

        Description:  Test with auth_type set to TLS.

        Arguments:

        """

        cfg = Cfg5()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["auth_type"], self.auth_type)

    def test_auth_type_ssl(self):

        """Function:  test_auth_type_ssl

        Description:  Test with auth_type set to SSL.

        Arguments:

        """

        cfg = Cfg4()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["auth_type"], "SSL")

    def test_auth_type_none(self):

        """Function:  test_auth_type_none

        Description:  Test with auth_type set to None.

        Arguments:

        """

        cfg = Cfg3()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["auth_type"], None)

    def test_coll_set_ssl(self):

        """Function:  test_coll_set_ssl

        Description:  Test mongo_class.Coll class with SSL set.

        Arguments:

        """

        cfg = Cfg3()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["ssl_client_ca"], cfg.ssl_client_ca)

    def test_rep_set_ssl(self):

        """Function:  test_rep_set_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set.

        Arguments:

        """

        cfg = Cfg3(self.repset_hosts)
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertEqual(mongo["ssl_client_ca"], cfg.ssl_client_ca)

    def test_coll_none_ssl(self):

        """Function:  test_coll_none_ssl

        Description:  Test mongo_class.Coll class with SSL set to none.

        Arguments:

        """

        cfg = Cfg2()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertFalse(mongo["ssl_client_ca"])

    def test_rep_none_ssl(self):

        """Function:  test_rep_none_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set to none.

        Arguments:

        """

        cfg = Cfg2(self.repset_hosts)
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertFalse(mongo["ssl_client_ca"])

    def test_coll_no_ssl(self):

        """Function:  test_coll_no_ssl

        Description:  Test the mongo_class.Coll class with no ssl.

        Arguments:

        """

        cfg = Cfg()
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertFalse(mongo["ssl_client_ca"])

    def test_rep_no_ssl(self):

        """Function:  test_rep_no_ssl

        Description:  Test the mongo_class.RepSetColl class with no ssl.

        Arguments:

        """

        cfg = Cfg(self.repset_hosts)
        mongo = mongo_libs.create_security_config(cfg=cfg)

        self.assertFalse(mongo["ssl_client_ca"])


if __name__ == "__main__":
    unittest.main()
