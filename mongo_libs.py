# Classification (U)

"""Program:  mongo_libs.py

    Description:  Library of function calls for a Mongo database system.

    Functions:
        create_cmd
        create_instance
        create_slv_array
        crt_base_cmd
        crt_coll_inst
        ins_doc
        json_2_out
        json_prt_ins_2_db

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
import lib.cmds_gen as cmds_gen
import mongo_class
import version

__version__ = version.__version__


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
        (output) -> Mongo utility command line.

    """

    cmd = crt_base_cmd(mongo, arg_parser.arg_set_path(args_array, path_opt)
                       + prog_name, **kwargs)

    # Process required arguments.
    for arg in kwargs.get("req_arg", []):
        cmd = cmds_gen.add_cmd(cmd, arg=arg)

    # Add optional arguments.
    return cmds_gen.is_add_cmd(args_array, cmd, kwargs.get("opt_arg", []))


def create_instance(cfg_file, dir_path, CLASS):

    """Function:  create_instance

    Description:  Create a Mongo database instance for the class that is
        received on the argument line.  This function is only used to create
        one of the following classes:  Server, Rep, Master_Rep, or
        Slave_Rep.  No other classes are allowed att.

    Arguments:
        (input) cfg_file -> Configuration file name.
        (input) dir_path -> Directory path.
        (input) CLASS -> Reference to a Class type.
        (output) -> Class type instance.

    """

    cfg = gen_libs.load_module(cfg_file, dir_path)

    return CLASS(cfg.name, cfg.user, cfg.passwd, cfg.host, cfg.port, cfg.auth,
                 cfg.conf_file)


def create_slv_array(cfg_array):

    """Function:  create_slv_array

    Description:  Create an array of slave instances from a configuration
        array.

    Arguments:
        (input) cfg_array -> Array of configurations.
        (output) SLV_ARRAY -> Array of slave instances.

    """

    SLV_ARRAY = []

    for slv in cfg_array:
        SLV = mongo_class.SlaveRep(slv["name"], slv["user"], slv["passwd"],
                                   slv["host"], int(slv["port"]), slv["auth"],
                                   slv["conf_file"])
        SLV_ARRAY.append(SLV)

    return SLV_ARRAY


def crt_base_cmd(MONGO, prog_name, **kwargs):

    """Function:  crt_base_cmd

    Description:  Create a basic program command line setup.  Will determine
        which connection to setup based on authenication setting.  The
        basic setup will include program name, host, and port.

    Arguments:
        (input) MONGO -> Database/Replication server instance.
        (input) prog_name -> Name of binary program.
        (input) **kwargs:
            use_repset -> True|False - Use repset name connection.
                (i.e. repset_name/host1,host2,...)
        (output) -> List of basic Mongo utility command line.

    """

    # Use repset name and hosts for connection, if set.
    if kwargs.get("use_repset", False) and MONGO.repset \
            and MONGO.repset_hosts:

        host_port = "--host=" + MONGO.repset + "/" + MONGO.repset_hosts

    # Use repset name for connection, if set.
    elif kwargs.get("use_repset", False) and MONGO.repset:
        host_port = "--host=" + MONGO.repset + "/" + MONGO.host + ":" \
                    + str(MONGO.port)

    # Assume just host and port.
    else:
        host_port = "--host=" + MONGO.host + ":" + str(MONGO.port)

    if MONGO.auth:
        return [prog_name, "--username=" + MONGO.user, host_port,
                "--password=" + MONGO.passwd]

    else:
        return [prog_name, host_port]


def crt_coll_inst(cfg, db, tbl, **kwargs):

    """Function:  crt_coll_inst

    Description:  Creates a Mongo collection instance, it will either be a
        connection to a single Mongo database or to a Mongo replica set.
        This will be based on the type of configuration passed.

    Arguments:
        (input) cfg_file -> Configuration file name.
        (input) db -> Database name.
        (input) tbl ->  Collection name.

    """

    if hasattr(cfg, "repset_hosts") and cfg.repset_hosts:

        return mongo_class.RepSetColl(cfg.name, cfg.user, cfg.passwd, cfg.host,
                                      cfg.port, cfg.auth, repset=cfg.repset,
                                      repset_hosts=cfg.repset_hosts, db=db,
                                      coll=tbl, db_auth=cfg.db_auth)

    else:
        return mongo_class.Coll(cfg.name, cfg.user, cfg.passwd, cfg.host,
                                cfg.port, db, tbl, cfg.auth, cfg.conf_file)


def ins_doc(mongo_cfg, db, tbl, data, **kwargs):

    """Function:  ins_doc

    Description:  Create and connect to a collection instance, convert a
        document to JSON, and insert document into the database.

    Arguments:
        (input) mongo_cfg -> Mongo database configuration.
        (input) db -> Database name.
        (input) tbl ->  Collection name.
        (input) data -> Document to be inserted.

    """

    COLL = crt_coll_inst(mongo_cfg, db, tbl, **kwargs)
    COLL.connect()
    COLL.ins_doc(json.loads(json.dumps(data)))
    cmds_gen.disconnect([COLL])


def json_2_out(data, **kwargs):

    """Function:  json_2_out

    Description:  If Mongo instance is present, insert data into database, else
        send data to standard out or file.

    Arguments:
        (input) data -> Data in dictionary format.
        (input) **kwargs:
            class_cfg -> Mongo server configuration.
            db_tbl database:table_name -> Mongo database and table name.
            ofile -> file name - Name of output file.

    """

    mongo_cfg = kwargs.get("class_cfg", False)
    db_tbl = kwargs.get("db_tbl", False)

    if mongo_cfg and db_tbl:
        db, tbl = db_tbl.split(":")
        ins_doc(mongo_cfg, db, tbl, data, **kwargs)

    else:
        # Convert dictionary to JSON and send to output.
        #   NOTE: Only the last line of the output will be saved to file.
        gen_libs.print_data(json.dumps(data, indent=4), **kwargs)


def json_prt_ins_2_db(data, **kwargs):

    """Function:  json_prt_ins_2_db

    Description:  Convert dictionary to JSON format and print it.  If Mongo
        instance is present, insert the data into database.

    Arguments:
        (input) data -> Data in dictionary format.
        (input) **kwargs:
            class_cfg -> Mongo server configuration.
            db_tbl database:table_name -> Mongo database and table name.
            ofile -> file name - Name of output file.

    """

    gen_libs.print_data(json.dumps(data, indent=4), **kwargs)

    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)

    if mongo_cfg and db_tbl:
        db, tbl = db_tbl.split(":")
        ins_doc(mongo_cfg, db, tbl, data, **kwargs)
