#!/usr/bin/python
# Classification (U)

"""Program:  server_is_locked.py

    Description:  Integration testing of Server.is_locked in mongo_class.py.

    Usage:
        test/integration/mongo_class/server_is_locked.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_locked

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base_dir = "test/integration"
        config_dir = os.path.join(base_dir, "config")
        config_name = "mongo"
        cfg = gen_libs.load_module(config_name, config_dir)
        self.mongo = mongo_class.Server(
            cfg.name, cfg.user, cfg.japd, host=cfg.host, port=cfg.port,
            use_uri=cfg.use_uri, auth=cfg.auth, use_arg=cfg.use_arg,
            auth_db=cfg.auth_db, conf_file=cfg.conf_file,
            ssl_client_ca=cfg.ssl_client_ca, ssl_client_key=cfg.ssl_client_key,
            ssl_client_cert=cfg.ssl_client_cert,
            ssl_client_phrase=cfg.ssl_client_phrase)
        self.mongo.connect()

    def test_is_locked(self):

        """Function:  test_is_locked

        Description:  Test is_locked method.

        Arguments:

        """

        self.assertFalse(self.mongo.is_locked())


if __name__ == "__main__":
    unittest.main()
