# Classification (U)

"""Program:  mongo_class.py

    Description:  Class definitions and methods for Mongo database system.

    Functions:
        fetch_cmd_line
        fetch_db_info
        fetch_ismaster

    Classes:
        Server
            DB
                Coll
            Rep
                MasterRep
                SlaveRep
                RepSet
                    RepSetColl

"""

# Libraries and Global Variables

# Standard
import time
import socket

# Third-party
import psutil
import pymongo

# Local
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "word"
KEY3 = "ssl_pem_"
KEY4 = "phrase"


def fetch_cmd_line(mongo):

    """Function:  fetch_cmd_line

    Description:  Calls adminstration command to run the getCmdLineOpts
        command.

    Arguments:
        (input) mongo -> Database instance.
        (output) -> Returns a document from the getCmdLineOpts command.

    """

    return mongo.adm_cmd("getCmdLineOpts")


def fetch_db_info(mongo):

    """Function:  fetch_db_info

    Description:  Calls adminstration command to run the listDatabases command.

    Arguments:
        (input) mongo -> Database instance.
        (output) -> Returns a document from the listDatabases command.

    """

    return mongo.adm_cmd("listDatabases")


def fetch_ismaster(mongo):

    """Function:  fetch_ismaster

    Description:  Calls the adminstration command to run the isMaster command.

    Arguments:
        (input) mongo -> Database instance.
        (output) -> Returns a document from the isMaster command.

    """

    return mongo.adm_cmd("isMaster")


class Server(object):

    """Class:  Server

    Description:  Class which is a representation of a Mongo database server.
        A server object is used as a proxy for operating with the
        server.  The basic methods and attributes include connection to
        the server and a number of methods to call the Pymongo client
        functions.

    Methods:
        __init__
        upd_srv_stat
        upd_server_attr
        get_srv_attr
        connect
        disconnect
        adm_cmd
        fetch_dbs
        is_primary
        fetch_adr
        fetch_svr_info
        unlock_db
        lock_db
        is_locked
        set_pass_config
        set_ssl_config

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Server class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authentication on.
                conf_file -> Location of mongo.conf file.
                use_uri -> True|False - Use uri to conenct to Mongo.
                use_arg -> True|False - Use arguments to connect to Mongo.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        global KEY1
        global KEY2

        self.name = name
        self.user = user
        self.host = host
        self.port = port
        self.auth = kwargs.get("auth", True)
        self.conf_file = kwargs.get("conf_file", None)
        self.conn = None
        self.db_path = None
        self.log_path = None
        self.uptime = None
        self.days_up = None
        self.cur_conn = None
        self.avl_conn = None
        self.max_conn = None
        self.prct_conn = None
        self.avl_sys_mem = None
        self.sys_mem_mb = None
        self.cur_mem = None
        self.max_mem = None
        self.prct_mem = None
        self.use_uri = kwargs.get("use_uri", False)
        self.use_arg = kwargs.get("use_arg", False)
        self.conn_list = [self.host + ":" + str(self.port)]
        self.auth_db = kwargs.get("auth_db", "admin")
        self.auth_mech = kwargs.get("auth_mech", "SCRAM-SHA-1")

        # Passwd configuration setup
        self.config = {}
        self.japd = japd
        self.set_pass_config()

        if self.auth_mech != "MONGODB-CR":
            self.config["authMechanism"] = self.auth_mech

        # SSL configuration settings
        self.ssl_client_ca = kwargs.get("ssl_client_ca", None)
        self.ssl_client_key = kwargs.get("ssl_client_key", None)
        self.ssl_client_cert = kwargs.get("ssl_client_cert", None)
        self.ssl_client_phrase = kwargs.get("ssl_client_phrase", None)
        self.set_ssl_config()

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Updates the Server's status attributes.

        Arguments:

        """

        udp_addr = "8.8." + "8.8"
        loopback = "127.0." + "0.1"
        data = self.adm_cmd("serverStatus")
        self.uptime = data["uptime"]
        self.cur_conn = data["connections"]["current"]
        self.avl_conn = data["connections"]["available"]
        self.cur_mem = data["mem"]["resident"]

        # Get local IP address.
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connecting to an UDP address doesn't send packets.
        sock.connect((udp_addr, 0))
        local_ip = sock.getsockname()[0]

        # Only get System Memory if on local machine.
        if self.host == local_ip or self.host == loopback:

            # Total Memory and percentage of memory used.
            self.avl_sys_mem = psutil.virtual_memory().available
            self.sys_mem_mb = int(float(self.avl_sys_mem) / (1024 * 1024))
            self.max_mem = self.sys_mem_mb + self.cur_mem
            self.prct_mem = int(float(self.cur_mem) / self.max_mem * 100)

        else:
            self.max_mem = "Unknown - Remote"

        # Days up since last recycle.
        self.days_up = int(float(self.uptime) / 3600 / 24)

        # Total connections and percentage of connections used.
        self.max_conn = self.cur_conn + self.avl_conn
        self.prct_conn = int(float(self.cur_conn) / self.max_conn * 100)

    def upd_server_attr(self):

        """Method:  upd_server_attr

        Description:  Update server information attributes.

        Arguments:

        """

        data = fetch_cmd_line(self)
        self.db_path = data["parsed"]["storage"]["dbPath"]
        self.log_path = data["parsed"]["systemLog"]["path"]

        if not self.conf_file and "config" in data["parsed"]:
            self.conf_file = data["parsed"]["config"]

    def get_srv_attr(self):

        """Method:  get_srv_attr

        Description:  Exception handling for the upd_server_attr method.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) msg -> Error message if connection failed.

        """

        status = True
        errmsg = None

        try:
            self.upd_server_attr()

        except pymongo.errors.ServerSelectionTimeoutError:
            self.disconnect()
            status = False
            errmsg = "Error:  Server not detected."

        except pymongo.errors.OperationFailure as msg:
            self.disconnect()
            status = False
            errmsg = "Error:  Auth flag or login params is incorrect: %s" % msg

        return status, errmsg

    def connect(self):

        """Method:  connect

        Description:  Sets up a connection to a Mongo database server and sets
            basic server attributes.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) msg -> Error message if connection failed.

        """

        if not self.conn:

            if self.auth:
                self.conn = pymongo.MongoClient(
                    self.conn_list, username=self.user,
                    authSource=self.auth_db, **self.config)

            else:
                self.conn = pymongo.MongoClient(self.host, self.port)

        status, errmsg = self.get_srv_attr()

        return status, errmsg

    def disconnect(self):

        """Method:  disconnect

        Description:  Disconnects from a Mongo database server connection.

        Arguments:

        """

        pymongo.MongoClient.close(self.conn)
        self.conn = None

    def adm_cmd(self, cmd, **kwargs):

        """Method:  adm_cmd

        Description:  Executes an administration command in the Mongo database.
            Will setup a connection to the database if not already connected.

        Arguments:
            (input) cmd -> Adminstration command.
            (input) **kwargs:
                arg1 -> Name of argument for command to work with.
            (output) Returns the output of the admin command.

        """

        return self.conn.admin.command(cmd, kwargs.get("arg1", None))

    def fetch_dbs(self):

        """Method:  fetch_dbs

        Description:  Get a list of databases in the database server.

        Arguments:
            (output) Returns a list of database names.

        """

        return self.conn.database_names()

    def is_primary(self):

        """Method:  is_primary

        Description:  Returns True if current server is standalone or is a
            primary database in a replica set, otherwise False.

        Arguments:
            (output) Returns True|False.

        """

        return self.conn.is_primary

    def fetch_adr(self):

        """Method:  fetch_adr

        Description:  Gets hostname & port from the current database server.

        Arguments:
            (output) Returns a tuple of host and port.

        """

        return self.conn.address

    def fetch_svr_info(self):

        """Method:  fetch_svr_info

        Description:  Returns information about a Mongo database server.

        Arguments:
            (output) Returns a dictionary with the server information.

        """

        return self.conn.server_info()

    def unlock_db(self):

        """Method:  unlock_db

        Description:  Unlocks a Mongo database server.

        Arguments:
            (output) Returns any output from the unlock command.

        """

        return self.conn.unlock()

    def lock_db(self, **kwargs):

        """Method:  lock_db

        Description:  Locks a Mongo database server.

        Arguments:
            (input) **kwargs:
                lock -> True|False - To lock the database.
            (output) Returns any output from the lock command.

        """

        if "lock" in kwargs:
            return self.conn.fsync(lock=kwargs["lock"])

    def is_locked(self):

        """Method:  is_locked

        Description:  Checks to see if the Mongo database is locked.

        Arguments:
            (output) Returns True|False based on the database status.

        """

        return self.conn.is_locked

    def set_pass_config(self):

        """Method:  set_pass_config

        Description:  Set the passwd config attributes.

        Arguments:

        """

        global KEY1
        global KEY2

        self.config[KEY1 + KEY2] = self.japd

    def set_ssl_config(self):

        """Method:  set_ssl_config

        Description:  Append SSL attributes to config.

        Arguments:

        """

        global KEY1
        global KEY3
        global KEY4

        if self.ssl_client_ca or self.ssl_client_cert:
            self.config["ssl"] = True

            if self.ssl_client_ca:
                self.config["ssl_ca_certs"] = self.ssl_client_ca

            if self.ssl_client_cert:
                self.config["ssl_certfile"] = self.ssl_client_cert

            if self.ssl_client_key and self.ssl_client_cert:
                self.config["ssl_keyfile"] = self.ssl_client_key

            if self.ssl_client_phrase and self.ssl_client_cert:
                self.config[KEY3 + KEY1 + KEY4] = self.ssl_client_phrase


class DB(Server):

    """Class:  DB

    Description:  Class which is a representation of a database instance in a
        Mongo database server.  The basic methods and attributes include
        setting up a database instance connection.

    Methods:
        __init__
        connect
        db_connect
        db_cmd
        validate_tbl
        isvalid_tbl
        get_tbl_list
        chg_db

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the DB class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                db -> Name of database.
                auth -> True|False - Authenication on.
                conf_file -> Location of mongo.conf file.
                use_uri -> True|False - Use uri to conenct to Mongo.
                use_arg -> True|False - Use arguments to connect to Mongo.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(DB, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            use_uri=kwargs.get("use_uri", False),
            use_arg=kwargs.get("use_arg", False),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.db_name = kwargs.get("db", "test")
        self.db = None

    def connect(self):

        """Method:  connect

        Description:  Connect to a Mongo database.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        status, errmsg = super(DB, self).connect()

        if status:
            self.db = self.conn[self.db_name]

        return status, errmsg

    def db_connect(self, dbs="test"):

        """Method:  db_connect

        Description:  Sets up an instance to a Mongo database.

        Arguments:
            (input) dbs -> Name of database.
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        status = True
        errmsg = None

        if not self.conn:
            status, errmsg = self.connect()

        if status:
            if dbs:
                self.db = self.conn[dbs]

            else:
                self.db = self.conn.test

        return status, errmsg

    def chg_db(self, dbs=None):

        """Method:  chg_db

        Description:  Changes database instance to a new database.  If no
            database passed then will default to test database.

        Arguments:
            (input) dbs -> Name of database.

        """

        if dbs:
            self.db = self.conn[dbs]
            self.db_name = dbs

        else:
            self.db = self.conn["test"]
            self.db_name = "test"

    def get_tbl_list(self, inc_sys=True):

        """Method:  get_tbl_list

        Description:  Returns a list of tables in the current database that is
            assigned to the database instance.

        Arguments:
            (input) inc_sys = True|False - Include system collections.
            (output) -> Returns a list of table names.

        """

        return self.db.collection_names(include_system_collections=inc_sys)

    def validate_tbl(self, tbl_name, scan=False):

        """Method:  validate_tbl

        Description:  Validates a table.

        Arguments:
            (input) tbl_name -> Table name.
            (input) scan -> True|False - Do full scan of table.
            (output) status -> True|False - Operation successful.
            (output) data -> Returns the results of the validate command.

        """

        status = True

        try:
            data = self.db.validate_collection(tbl_name, full=scan)

        except pymongo.errors.OperationFailure as msg:
            status = False
            data = msg

        return status, data

    def db_cmd(self, cmd, **kwargs):

        """Method:  db_cmd

        Description:  Executes a database command in the database.  Checks to
            see if additional options are to be included in the execution of
            the command.

        Arguments:
            (input) cmd -> Database command.
            (input) **kwargs:
                obj -> Name of object command will work against.
                    NOTE:  obj can be a database or collection.
            (output) Returns the output of the database command.

        """

        if "obj" in kwargs:
            return self.db.command(cmd, kwargs["obj"])

        return self.db.command(cmd)


class Coll(DB):

    """Class:  Coll

    Description:  Class which is a representation of a collection instance in a
        Mongo database server.  The basic methods and attributes include
        setting up a collection instance and connection.

    Methods:
        __init__
        connect
        coll_cnt
        coll_find
        coll_dst
        coll_find1
        ins_doc
        coll_options

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the DB class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                db -> Name of database.
                coll -> Name of collection.
                auth -> True|False - Authenication on.
                conf_file -> Location of mongo.conf file.
                use_uri -> True|False - Use uri to conenct to Mongo.
                use_arg -> True|False - Use arguments to connect to Mongo.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(Coll, self).__init__(
            name, user, japd, host=host, port=port,
            db=kwargs.get("db", "test"), auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            use_uri=kwargs.get("use_uri", False),
            use_arg=kwargs.get("use_arg", False),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.coll = None
        self.coll_db = kwargs.get("db", "test")
        self.coll_coll = kwargs.get("coll", None)

    def connect(self):

        """Method:  connect

        Description:  Connect to a Mongo database.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        status, errmsg = super(Coll, self).connect()

        if status:
            if self.coll_coll:
                self.coll = self.conn[self.coll_db][self.coll_coll]

            else:
                status = False
                errmsg = "Error:  Unable to connect, no collection passed."

        return status, errmsg

    def coll_cnt(self, qry=None):

        """Method:  coll_cnt

        Description:  Total count in a collection.

        Arguments:
            (input) qry -> Query criteria for count command.
            (output) -> Total number of documents in a collection.

        """

        if qry is None:
            qry = {}

        return self.coll.count(qry)

    def coll_find(self, qry=None):

        """Method:  coll_find

        Description:  Query of document using find command.

        Arguments:
            (input) qry -> Query criteria for find command.
            (output) -> Return of documents from collection as cursor.

        """

        if qry is None:
            qry = {}

        return self.coll.find(qry)

    def coll_dst(self, col=""):

        """Method:  coll_dst

        Description:  Query of document using distinct command.

        Arguments:
            (input) col -> Column distinct will be ran against.
            (output) -> Return of distinct values for col.

        """

        return self.coll.distinct(col)

    def coll_find1(self, qry=None):

        """Method:  coll_find1

        Description:  Query of document using findOne command.

        Arguments:
            (input) qry -> Query criteria for findOne command.
            (output) -> Return of document from collection as cursor.

        """

        if qry is None:
            qry = {}

        return self.coll.find_one(qry)

    def ins_doc(self, doc):

        """Method:  ins_doc

        Description:  Insert document into a collection.

        Arguments:
            (input) doc -> Document to be inserted into collection.

        """

        self.coll.insert_one(doc)

    def coll_options(self):

        """Method:  coll_options

        Description:  Return the collections option settings.

        Arguments:
            (output) -> Return options settings on the collection.

        """

        return self.coll.options()


class Rep(Server):

    """Class:  Rep

    Description:  Class which is a representation of a Mongo database server in
        replication.  A replication object is used as a proxy for
        operating within a Mongo database server.  The basic methods
        and attributes include general methods for replication.

    Methods:
        __init__
        fetch_nodes

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Rep class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authenication on.
                conf_file -> Location of mongo.conf file.
                use_uri -> True|False - Use uri to conenct to Mongo.
                use_arg -> True|False - Use arguments to connect to Mongo.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(Rep, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            use_uri=kwargs.get("use_uri", False),
            use_arg=kwargs.get("use_arg", False),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.repset = None
        self.ismaster = None
        self.isslave = None

    def fetch_nodes(self):

        """Method:  fetch_nodes

        Description:  Returns a set of all nodes in the replica set.
            NOTE:  Require time delay to allow for all nodes to be discover.

        Arguments:
            (output) -> List of all nodes in the replica set.

        """

        time.sleep(0.1)

        return self.conn.nodes


class MasterRep(Rep):

    """Class:  MasterRep

    Description:  Class which is a representation of a Master Replication Mongo
        database server.  A master replication server object is used as
        a proxy for operating within a replication Mongo server.

    Methods:
        __init__
        connect

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the MasterRep class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authenication on.
                conf_file -> Location of mongo.conf file.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(MasterRep, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.ismaster = None
        self.issecondary = None
        self.repset = None
        self.slaves = None

    def connect(self):

        """Method:  connect

        Description:  Connect to a Mongo database.

        Arguments:
            (output) status -> True|False - Connection success or not master.
            (output) errmsg -> Message status.

        """

        status, errmsg = super(MasterRep, self).connect()

        if status:
            data = fetch_ismaster(self)

            if data.get("ismaster"):
                self.ismaster = data.get("ismaster")
                self.issecondary = data.get("secondary")
                self.repset = data.get("setName")
                self.slaves = data.get("hosts", [])

            else:
                self.disconnect()
                status = False
                errmsg = "Error:  This is not a Master Replication server."

        return status, errmsg


class SlaveRep(Rep):

    """Class:  SlaveRep

    Description:  Class which is a representation of a Slave Replication Mongo
        database server.  A slave replication server object is used as a
        proxy for operating within a replication Mongo server.

    Methods:
        __init__
        connect

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the SlaveRep class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authenication on.
                conf_file -> Location of mongo.conf file.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(SlaveRep, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            auth_db=kwargs.get("auth_db", "admin"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.ismaster = None
        self.issecondary = None
        self.repset = None
        self.primary = None

    def connect(self):

        """Method:  connect

        Description:  Connect to a Mongo database.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        status, errmsg = super(SlaveRep, self).connect()

        if status:
            data = fetch_ismaster(self)

            if data.get("secondary"):
                self.ismaster = data.get("ismaster")
                self.issecondary = data.get("secondary")
                self.repset = data.get("setName")
                self.primary = data.get("primary")

            else:
                self.disconnect()
                status = False
                errmsg = "Error:  This is not a Slave Replication server."

        return status, errmsg


class RepSet(Rep):

    """Class:  RepSet

    Description:  Class which is a representation of a Mongo Replica set.  A
        replication set object is used as a proxy for operating within a
        replication Mongo database server.  The basic methods and
        attributes include connecting method.

    Methods:
        __init__
        connect

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the RepSet class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authenication on.
                repset -> Replication Set name.
                conf_file -> Location of mongo.conf file.
                repset_hosts -> Repset hosts:ports.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(RepSet, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.repset = kwargs.get("repset", None)
        self.repset_hosts = kwargs.get("repset_hosts", None)

    def connect(self, connections=None):

        """Method:  connect

        Description:  Sets up a connection to a Mongo replication set and sets
            basic server attributes.

        Arguments:
            (input) connections ->  String of server connections.
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        if not connections:

            if self.repset_hosts:
                connections = self.repset_hosts

            else:
                connections = self.host + ":" + str(self.port)

        if not self.conn:

            if self.auth:
                self.conn = pymongo.MongoClient(
                    connections, username=self.user, authSource=self.auth_db,
                    replicaSet=self.repset, **self.config)

            else:
                self.conn = pymongo.MongoClient(
                    connections, replicaSet=self.repset)

        status, errmsg = self.get_srv_attr()

        return status, errmsg


class RepSetColl(RepSet):

    """Class:  RepSetColl

    Description:  Class which is a representation of a collection instance in a
        Mongo database server.  The basic methods and attributes include
        setting up a collection instance and connection.

    Methods:
        __init__
        connect
        _db_auth
        ins_doc
        coll_cnt
        coll_del_many
        coll_find
        coll_dst
        coll_find1
        coll_options

    """

    def __init__(self, name, user, japd, host="localhost", port=27017,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the DB class.

        Arguments:
            (input) name -> Name of server.
            (input) user -> User's name.
            (input) japd -> User's pswd.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '27017' or port for Mongo.
            (input) kwargs:
                auth -> True|False - Authenication on.
                repset -> Replication Set name.
                conf_file -> Location of mongo.conf file.
                repset_hosts -> Repset hosts and ports.
                db -> Name of database.
                coll -> Name of collection.
                db_auth -> None or name of authentication database.
                auth_db -> Authentication database name.
                auth_mech -> Authentication mechanism for connecting.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL key pem file.
                ssl_client_cert -> SSL certificate pem file.
                ssl_client_phrase -> SSL client pass phrase to key file.

        """

        super(RepSetColl, self).__init__(
            name, user, japd, host=host, port=port,
            auth=kwargs.get("auth", True),
            conf_file=kwargs.get("conf_file", None),
            repset=kwargs.get("repset", None),
            repset_hosts=kwargs.get("repset_hosts", None),
            auth_db=kwargs.get("auth_db", "admin"),
            auth_mech=kwargs.get("auth_mech", "SCRAM-SHA-1"),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_client_phrase=kwargs.get("ssl_client_phrase", None))

        self.db = kwargs.get("db", "test")
        self.coll = kwargs.get("coll", None)
        self.db_auth = kwargs.get("db_auth", None)
        self.db_conn = None
        self.db_coll = None
        self.db_auth_conn = None

    def connect(self, connections=None):

        """Method:  connect

        Description:  Sets up a connection to a Mongo replication set and
            connects to a database and collection.

        Arguments:
            (input) connections ->  String of server connections.
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        if not connections:

            if self.repset_hosts:
                connections = self.repset_hosts

            else:
                connections = self.host + ":" + str(self.port)

        if not self.conn:

            if self.auth:
                self.conn = pymongo.MongoClient(
                    host=[connections], username=self.user,
                    authSource=self.auth_db, document_class=dict,
                    tz_aware=False, connect=True, replicaSet=self.repset,
                    **self.config)

                if self.conn:
                    self.db_coll = self.conn[self.db][self.coll]

            else:
                self.conn = pymongo.MongoClient(connections,
                                                replicaSet=self.repset)

        status, errmsg = self.get_srv_attr()

        return status, errmsg

    def _db_auth(self):

        """Method:  _db_auth

        Description:  Database authentication.  Private function for connect.

        Arguments:
            (output) status -> True|False - Connection successful.
            (output) errmsg -> Error message if connection failed.

        """

        status = True
        errmsg = None

        try:
            self.db_auth_conn = self.db_conn.authenticate(self.user, self.japd)
            self.db_coll = self.conn[self.db][self.coll]

        except pymongo.errors.ServerSelectionTimeoutError:
            self.disconnect()
            status = False
            errmsg = "Error:  Server not detected."

        except pymongo.errors.OperationFailure as msg:
            self.disconnect()
            status = False
            errmsg = "Error: Auth flag/login params is incorrect: %s" % msg

        return status, errmsg

    def ins_doc(self, doc):

        """Method:  ins_doc

        Description:  Insert document into a collection.

        Arguments:
            (input) doc -> Document to be inserted into collection.

        """

        self.db_coll.insert_one(doc)

    def coll_cnt(self, qry=None):

        """Method:  coll_cnt

        Description:  Total count in a collection.

        Arguments:
            (input) qry -> Query criteria for command.
            (output) -> Total number of documents in a collection.

        """

        if qry is None:
            qry = {}

        return self.db_coll.count(qry)

    def coll_del_many(self, qry=None, override=False):

        """Method:  coll_del_many

        Description:  Delete many records in a collection that match the search
            criteria.  Override allows for empty search criteria to
            truncate the collection.

        Arguments:
            (input) qry -> Query criteria for command.
            (input) override -> True|False - Allow for empty queries.

        """

        if qry:
            self.db_coll.delete_many(qry)

        # Allow for truncation.
        elif override:
            self.db_coll.delete_many({})

        # Assume must be a mistake.
        else:
            print("WARNING:  Require search criteria.")

    def coll_find(self, query=None):

        """Method:  coll_find

        Description:  Query of document using find command.

        Arguments:
            (input) query -> Query criteria for find command.
            (output) -> Return of documents from collection as cursor.

        """

        if query is None:
            query = {}

        return self.db_coll.find(query)

    def coll_dst(self, column=""):

        """Method:  coll_dst

        Description:  Query of document using distinct command.

        Arguments:
            (input) column -> Column distinct will be ran against.
            (output) -> Return of distinct values for col.

        """

        return self.db_coll.distinct(column)

    def coll_find1(self, query=None):

        """Method:  coll_find1

        Description:  Query of document using findOne command.

        Arguments:
            (input) query -> Query criteria for findOne command.
            (output) -> Return of document from collection as cursor.

        """

        if query is None:
            query = {}

        return self.db_coll.find_one(query)

    def coll_options(self):

        """Method:  coll_options

        Description:  Return the collections option settings.

        Arguments:
            (output) -> Return options settings on the collection.

        """

        return self.db_coll.options()
