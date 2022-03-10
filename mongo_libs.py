# Classification (U)

"""Program:  mongo_libs.py

    Description:  Library of function calls for a Mongo database system.

    Functions:
        add_ssl_cmd
        create_cmd
        create_instance
        create_slv_array
        crt_base_cmd
        crt_coll_inst
        disconnect
        ins_doc

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function

# Third party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import mongo_class
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "word"
KEY3 = "ssl_pem_"
KEY4 = "phrase"
HOST = "--host="


def add_ssl_cmd(mongo, cmd_list):

    """Function:  add_ssl_cmd

    Description:  Determine if SSL options are present and add to the command
        line.

    Arguments:
        (input) mongo -> Database instance
        (input) cmd_line -> Basic Mongo utility command line in list format.
        (output) cmd_line -> Basic Mongo utility command line in list format.
    """

    global KEY1
    global KEY2
    global KEY3
    global KEY4

    cmd_list = list(cmd_list)

    if mongo.config.get("ssl", False):
        cmd_list.append("--ssl")

        if mongo.config.get("ssl_ca_certs"):
            cmd_list.append("--sslCAFile=" + mongo.config.get("ssl_ca_certs"))

        if mongo.config.get("ssl_keyfile"):
            cmd_list.append(
                "--sslPEMKeyFile=" + mongo.config.get("ssl_keyfile"))

            if mongo.config.get(KEY3 + KEY1 + KEY4):
                cmd_list.append(
                    "--sslPEMKeyPass" + KEY2 + "="
                    + mongo.config.get(KEY3 + KEY1 + KEY4))

    return cmd_list


def create_cmd(mongo, args_array, prog_name, path_opt, **kwargs):

    """Function:  create_cmd

    Description:  Create a basic command line for a mongo utility program and
        then add required arguments and additional options if they are present.

    Arguments:
        (input) mongo -> Database instance.
        (input) args_array -> Array of command line options and values.
        (input) prog_name -> Name of utility program.
        (input) path_opt -> Option containing the path dir to program.
        (input) **kwargs:
            req_arg -> List of options to add to cmd line.
            opt_arg -> Dictionary of additional options to add.
            use_repset -> True|False - Use repset name connection.
                (i.e. repset_name/host1,host2,...)
            no_pass -> True|False - Turn off --password= option.
        (output) -> Mongo utility command line.

    """

    args_array = dict(args_array)
    cmd = crt_base_cmd(mongo, arg_parser.arg_set_path(args_array, path_opt)
                       + prog_name, **kwargs)

    # Process required arguments.
    for arg in list(kwargs.get("req_arg", [])):
        cmd = gen_libs.add_cmd(cmd, arg=arg)

    # Process optional arguments.
    return gen_libs.is_add_cmd(args_array, cmd,
                               dict(kwargs.get("opt_arg", {})))


def create_instance(cfg_file, dir_path, class_name):

    """Function:  create_instance

    Description:  Create a Mongo database instance for the class that is
        received on the argument line.  This function is used to create
        instances for the following classes:  Server, Rep, MasterRep, SlaveRep,
        RepSet, and DB.  Can create instances for the RepSetColl and Coll
        classes, but see Note section below for more details.

    Note 1:  If an instance is created for RepSetColl, then the db_auth and db
        attributes need to be manually set before calling the classes'
        connect method.

    Note 2:  If an instance is created for Coll, then the db and coll_coll
        attributes need to be manually set before calling the classes'
        connect method.

    Arguments:
        (input) cfg_file -> Configuration file name.
        (input) dir_path -> Directory path.
        (input) class_name -> Reference to a Class type.
        (output) -> Mongo class instance.

    """

    auth_db = "admin"
    auth_mech = "SCRAM-SHA-1"
    ssl_client_ca = None
    ssl_client_cert = None
    ssl_client_key = None
    ssl_client_phrase = None
    cfg = gen_libs.load_module(cfg_file, dir_path)

    if hasattr(cfg, "auth_db"):
        auth_db = cfg.auth_db

    if hasattr(cfg, "auth_mech"):
        auth_mech = cfg.auth_mech

    if hasattr(cfg, "ssl_client_ca"):
        ssl_client_ca = cfg.ssl_client_ca

    if hasattr(cfg, "ssl_client_cert"):
        ssl_client_cert = cfg.ssl_client_cert

    if hasattr(cfg, "ssl_client_key"):
        ssl_client_key = cfg.ssl_client_key

    if hasattr(cfg, "ssl_client_phrase"):
        ssl_client_phrase = cfg.ssl_client_phrase

    return class_name(
        cfg.name, cfg.user, cfg.japd, host=cfg.host, port=cfg.port,
        auth=cfg.auth, conf_file=cfg.conf_file, auth_db=auth_db,
        auth_mech=auth_mech, ssl_client_ca=ssl_client_ca,
        ssl_client_cert=ssl_client_cert, ssl_client_key=ssl_client_key,
        ssl_client_phrase=ssl_client_phrase)


def create_slv_array(cfg_array):

    """Function:  create_slv_array

    Description:  Create an array of slave instances from a configuration
        array.

    Arguments:
        (input) cfg_array -> List of configurations.
        (output) slaves -> List of slave instances.

    """

    cfg_array = list(cfg_array)
    slaves = []

    for slv in cfg_array:
        auth_db = slv.get("auth_db", "admin")
        auth_mech = slv.get("auth_mech", "SCRAM-SHA-1")

        slave_inst = mongo_class.SlaveRep(
            slv["name"], slv["user"], slv["japd"], host=slv["host"],
            port=int(slv["port"]), auth=slv["auth"],
            conf_file=slv["conf_file"], auth_db=auth_db, auth_mech=auth_mech)

        slaves.append(slave_inst)

    return slaves


def crt_base_cmd(mongo, prog_name, **kwargs):

    """Function:  crt_base_cmd

    Description:  Create a basic program command line setup.  Will determine
        which connection to setup based on authenication setting.  The
        basic setup will include program name, host, and port.

    Arguments:
        (input) mongo -> Database instance.
        (input) prog_name -> Name of binary program.
        (input) **kwargs:
            use_repset -> True|False - Use repset name connection.
                (i.e. repset_name/host1,host2,...)
            no_pass -> True|False - Turn off --password= option.
        (output) cmd_line -> Basic Mongo utility command line in list format.

    """

    global KEY1
    global KEY2
    global KEY3
    global KEY4
    global HOST

    cmd_list = []

    # Use repset name and hosts for connection
    if kwargs.get("use_repset", False) and mongo.repset \
            and mongo.repset_hosts:

        host_port = HOST + mongo.repset + "/" + mongo.repset_hosts

    # Use repset name for connection
    elif kwargs.get("use_repset", False) and mongo.repset:
        host_port = HOST + mongo.repset + "/" + mongo.host + ":" \
                    + str(mongo.port)

    # Assume just host and port
    else:
        host_port = HOST + mongo.host + ":" + str(mongo.port)

    # Determine the type of user parameters to add
    if mongo.auth and kwargs.get("no_pass", False):
        cmd_list = [prog_name, "--username=" + mongo.user, host_port]

    elif mongo.auth:
        cmd_list = [prog_name, "--username=" + mongo.user, host_port,
                    "--" + KEY1 + KEY2 + "=" + mongo.japd]

    else:
        cmd_list = [prog_name, host_port]

    if mongo.config.get("ssl", False):
        cmd_list = add_ssl_cmd(mongo, cmd_list)

    return cmd_list


def crt_coll_inst(cfg, dbs, tbl):

    """Function:  crt_coll_inst

    Description:  Creates a Mongo collection instance, it will either be a
        connection to a single Mongo database or to a Mongo replica set.
        This will be based on the type of configuration passed.

    Arguments:
        (input) cfg -> Mongo instance or mongo config module.
        (input) dbs -> Database name.
        (input) tbl ->  Collection name.

    """

    auth_db = cfg.auth_db if hasattr(cfg, "auth_db") else "admin"
    auth_mech = cfg.auth_mech if hasattr(cfg, "auth_mech") else "SCRAM-SHA-1"
    ssl_client_ca = cfg.ssl_client_ca if hasattr(
        cfg, "ssl_client_ca") else None
    ssl_client_cert = cfg.ssl_client_cert if hasattr(
        cfg, "ssl_client_cert") else None
    ssl_client_key = cfg.ssl_client_key if hasattr(
        cfg, "ssl_client_key") else None
    ssl_client_phrase = cfg.ssl_client_phrase if hasattr(
        cfg, "ssl_client_phrase") else None

    if hasattr(cfg, "repset_hosts") and cfg.repset_hosts:

        return mongo_class.RepSetColl(
            cfg.name, cfg.user, cfg.japd, host=cfg.host, port=cfg.port,
            auth=cfg.auth, repset=cfg.repset, repset_hosts=cfg.repset_hosts,
            db=dbs, coll=tbl, db_auth=cfg.db_auth, auth_db=auth_db,
            auth_mech=auth_mech, ssl_client_ca=ssl_client_ca,
            ssl_client_cert=ssl_client_cert, ssl_client_key=ssl_client_key,
            ssl_client_phrase=ssl_client_phrase)

    return mongo_class.Coll(
        cfg.name, cfg.user, cfg.japd, host=cfg.host, port=cfg.port,
        db=dbs, coll=tbl, auth=cfg.auth, conf_file=cfg.conf_file,
        auth_db=auth_db, auth_mech=auth_mech, ssl_client_ca=ssl_client_ca,
        ssl_client_cert=ssl_client_cert, ssl_client_key=ssl_client_key,
        ssl_client_phrase=ssl_client_phrase)


def disconnect(*args):

    """Function:  disconnect

    Description:  Disconnects a class database connection.  Will check to see
        if an argument is an array; if so will loop on the array to disconnect
        all connections.  Will require a disconnect method within the class.
        The disconnect method will be particular to that class.

    Arguments:
        (input) *arg -> One or more connection instances.

    """

    for server in args:

        if isinstance(server, list):
            for srv in server:
                srv.disconnect()

        else:
            server.disconnect()


def ins_doc(mongo_cfg, dbs, tbl, data, **kwargs):

    """Function:  ins_doc

    Description:  Create and connect to a collection instance, convert a
        document to JSON, and insert document into the database.

    Arguments:
        (input) mongo_cfg -> Mongo instance or mongo config module.
        (input) dbs -> Database name.
        (input) tbl ->  Collection name.
        (input) data -> Document to be inserted.
        (output) status -> True|False - Connection successful.
        (output) errmsg -> Error message if connection failed.

    """

    data = dict(data)
    coll = crt_coll_inst(mongo_cfg, dbs, tbl, **kwargs)
    status, errmsg = coll.connect()

    if status:
        coll.ins_doc(json.loads(json.dumps(data)))
        disconnect([coll])

    return status, errmsg
