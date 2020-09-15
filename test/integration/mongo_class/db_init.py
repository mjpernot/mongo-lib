#!/usr/bin/python
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
        setUp -> Initialize testing environment.
        test_no_db_name_attr -> Test no db_name attribute passed.
        test_db_name_attr -> Test db_name attribute passed.
        test_default_conf_file -> Test using the default conf_file setting.
        test_using_conf_file -> Test using the conf_file connection.
        test_default_auth -> Test using the default auth setting.
        test_using_auth -> Test using the auth connection.
        test_conn_list_attr -> Test setting the conn_list attribute.
        test_config_attr -> Test setting the config attribute.
        test_default_auth_db -> Test using the default auth_db setting.
        test_using_auth_db -> Test using the auth_db attribute.
        test_default_arg -> Test using the default arg setting.
        test_using_arg -> Test using the arg connection.
        test_default_uri -> Test using the default uri setting.
        test_using_uri -> Test using the uri connection.
        test_default -> Test with minimum number of arguments.

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
        key1 = "pass"
        key2 = "word"
        self.config = {key1 + key2: self.cfg.japd}
        self.conn_list = [self.cfg.host + ":" + str(self.cfg.port)]
        self.db_name = "admin"

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

        self.assertEqual(mongo.config, self.config)

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

    def test_default_arg(self):

        """Function:  test_default_arg

        Description:  Test using the default arg setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.use_arg)

    def test_using_arg(self):

        """Function:  test_using_arg

        Description:  Test using the arg connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_arg=self.cfg.use_arg)

        self.assertTrue(mongo.use_arg)

    def test_default_uri(self):

        """Function:  test_default_uri

        Description:  Test using the default uri setting.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port)

        self.assertFalse(mongo.use_uri)

    def test_using_uri(self):

        """Function:  test_using_uri

        Description:  Test using the uri connection.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.port, use_uri=True)

        self.assertTrue(mongo.use_uri)

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
