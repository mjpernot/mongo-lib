# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.5.3] - 2025-06-03
- Updated python-lib to v4.0.1

### Added
- mongo_class.Coll.coll_del_many: Delete records in a collection that match the search criteria.


## [4.5.2] - 2025-05-06
- Fixed a number of methods to work in Pymongo v4.X.

### Fixed
- mongo_class.Coll.coll_dst: Removed the default value for the col argument.
- mongo_class.DB.get_tbl_list: Removed "include_system_collections" and replaced with regex expression in filter argument.
- mongo_class.Server.is_locked: Replaced is_locked with admin.command("currentOp") call.
- mongo_class.Server.unlock_db: Replaced unlock() with admin.commandi"fsyncUnlock"() call.
- mongo_class.Server.lock_db: Replaced fsync() with admin.command("fsync") call.
- Renamed mongo.py to mongo_template.py due to conflict in testing.

## Changes
- mongo_class.Rep.\_\_init\_\_: Added direct_connect to initialization of the class.
- mongo_class.SlaveRep.\_\_init\_\_: Added direct_connect to initialization of the class.
- mongo_class.Server.unlock_db: Add check to only unlock if database is locked.
- Documentation changes.


## [4.5.1] - 2025-03-11
- Added support for Mongo 7.0
- Fixed problem with external binaries requiring to use SSL options to connect.

### Fixed
- mongo_libs.add_tls_cmd: Changed the TLS options to SSL options for outside binary commands.

### Changed
- mongo_class.Server.\_\_init\_\_: Removed check for "MONGODB-CR" in authorization mechanism.
- Documentation changes.


## [4.5.0] - 2025-02-07
- Added capability to connect directly to single server in replica set.

### Changed
- mongo_class.\_\_init\_\_: Added direct_connect attribute and set it in config attribute. 
- mongo_libs.create_instance: Added check for direct_connect configuration entry.

### Removed
- Mongo 3.4 support.


## [4.4.0] - 2024-12-20
- Removed support for Python 2.7.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Set pymongo==4.1.1 for Python 3.6.
- Update python-lib to v4.0.0

### Changed
- mongo_class.Server.lock_db: Refactored the method.
- mongo_class: Replaced dict() with {} and list() with [].
- mongo_libs: Replaced dict() with {} and list() with [].
- mongo_class: Converted strings to f-strings.
- Documentation changes.

### Deprecated
- Support for Mongo 3.4


## [4.3.4] - 2024-11-14

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [4.3.3] - 2024-10-25
- Updated chardet==4.0.0 for Python 3.
- Updated distro==1.9.0 for Python 3.
- Updated psutil==5.9.4 for Python 3.
- Updated python-lib to 3.0.6


## [4.3.2] - 2024-09-23
- Set pymongo to 4.1.1 for Python 3.6.
- Set simplejson to 3.13.2 for Python 3.

### Added
- mongo_libs.get_all_dbs_tbls: Return a dictionary of databases with table lists.
- mongo_libs.get_db_tbl: Determines which databases and tables will be checked.

### Changed
- Documentation changes.


## [4.3.1] - 2024-08-16
- Set simplejson to 3.13.2 for Python 2.
- Set pymongo to 4.6.3 for Python 3.
- Updated python-lib to 3.0.4

### Added
- mongo_libs.create_security_config:  Create security configuration object from a configuration file or mongo instance.
- mongo_libs.data_out: Outputs the data in a variety of formats and media.

### Changed
- mongo_libs.create_instance, mongo_libs.crt_coll_inst:  Replaced section of code with call to create_security_config.


## [4.3.0] - 2024-04-09
- Added TLS connection capability to the Mongo classes and libraries.
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- mongo_libs.crt_base_cmd: Added check for TLS settings.
- mongo_class.DB.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.Coll.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.Rep.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.SlaveRep.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.RepSet.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.RepSetColl.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_libs: create_instance, crt_coll_inst: Added TLS configuration entries and also passed in TLS and SSL via a pointer instead of individual parameters.
- mongo_class.Server.\_\_init\_\_: Added TLS attributes and type of connection attribute.
- mongo_class.Server.set_tls_config: Set the TLS attributes to the config setup.
- mongo_class.Server: \_\_init\_\_, set_pass_config, set_ssl_config: Removed global variables and replaced them with hardcoded values.
- mongo_libs: add_ssl_cmd, crt_base_cmd: Removed global variables and replaced them with hardcoded values.
- Documentation changes.

### Added
- mongo_libs.add_tls_cmd: Add TLS options to the command line.
- mongo_class.Server.set_tls_config: Append TLS attributes to config.
- Added mongo.py - Template Mongo configuration file.


## [4.2.9] - 2024-02-21
- Updated python-lib to v3.0.3
- Updated module requirements for Python.

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set distro to 1.6.0 for Python 3.
- Set chardet to 3.0.4 for Python 2 and Python 3.
- Documentation changes.


## [4.2.8] - 2024-01-19
- Upgraded python-lib to v3.0.1
- Updated to work in RedHat 8 environment.


## [4.2.7] - 2023-10-11
- Upgraded python-lib to v2.10.1

### Fixed
- mongo_libs.create_cmd: Added args.arg_set_path to the join command to produce the correct path.


## [4.2.6] - 2023-10-04
- Fixed errors in unit testing.


## [4.2.5] - 2023-09-19
### Changed
- mongo_lib.create_cmd: Added ability to pass an args_array or an gen_class.ArgParser instance.


## [4.2.4] - 2023-06-06
### Fixed
- mongo_class.Server.upd_srv_stat: Using only self.host ip to determine if on a remote host.

### Changed
- Update documentation.


## [4.2.3] - 2023-01-26
### Fixed
- mongo_class.Server.upd_srv_stat: Added check for hostname in the system memory check.

### Changed
- mongo_class.RepSetColl:  Changed attribute db to db_name.
- mongo_class.DB: Changed attribute db to db_inst.


## [4.2.2] - 2022-10-07
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4

### Changed
- mongo_class.Coll.coll_cnt, mongo_class.RepSetColl.coll_cnt:  Replaced deprecated count() with count_documents().
- mongo_class.DB.get_tbl_list:  Replaced deprecated collection_names() with list_collection_names().
- mongo_class.Server.fetch_dbs:  Replaced deprecated database_names() with list_database_names().
- mongo_class.Server.upd_srv_stat: Converted divisor to a float to force float division and closed socket connection.

### Removed
- mongo_libs.create_slv_array


## [4.2.1] - 2022-03-08
- Upgraded python-lib to v2.8.6

### Changed
- mongo_libs.crt_coll_inst, mongo_libs.create_instance:  Refactored function.
- mongo_libs: Remove use_arg and use_uri from all Mongo library functions.
- mongo_class: Removed use_arg and use_uri attributes from all Mongo classes.
- mongo_class.Server.connect, mongo_class.RepSet.connect: Removed the uri connection capability.
- mongo_libs.create_cmd: Changed cmds_gen.add_cmd to gen_libs.add_cmd and cmds_gen.is_add_cmd to gen_libs.is_add_cmd.

### Deprecated
- mongo_libs.create_slv_array

### Removed
- mongo_class.RepSetColl.\_db_auth method


## [4.2.0] - 2021-06-22
- Added SSL connection capability to the Mongo classes.

### Fixed
- mongo_class.Coll.connect:  Added exception handler if no collection is passed to class.
- mongo_libs.create_instance:  Added auth_mech argument to instance call.

### Added
- mongo_libs.add_ssl_cmd:  Determine if SSL options are present and add to the command line.
- mongo_class.Server.set_ssl_config:  Append SSL attributes to config.
- mongo_class.Server.set_pass_config:  Set the passwd config attributes.

### Changed
- mongo_libs.crt_base_cmd:  Add check for SSL and append to command line if present.
- mongo_libs.crt_base_cmd:  Add check for no_pass option to determine usage of \-\-password= option and moved host, data, and data2 to Global variables.
- mongo_libs.create_instance:  Added checks for SSL arguments and pass to class instance calls.
- mongo_libs.create_slv_array:  Removed unused \*\*kwargs.
- mongo_libs.crt_coll_inst:  Added checks for SSL arguments and pass to class instance calls.
- mongo_class.RepSetColl.\_\_init\_\_, mongo_class.RepSet.\_\_init\_\_, mongo_class.SlaveRep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_, mongo_class.Rep.\_\_init\_\_, mongo_class.Coll.\_\_init\_\_, mongo_class.DB.\_\_init\_\_:  Added capability to allow SSL attributes to be set.
- mongo_class.Server.\_\_init\_\_:  Moved setting of config attribute to set_pass_config method and added call to set_pass_config.
- mongo_class.Server.\_\_init\_\_: Added SSL attributes and added call to set_ssl_config.
- Documentation updates.

### Deprecated
- mongo_class.RepSetColl.\_\_init\_\_:  Removal of db_auth_conn attribute.
- mongo_class.RepSetColl.\_db_auth:  Removal private method, no longer required.
- mongo_class.Server.\_\_init\_\_:  Removal of use_uri and use_arg attributes.
- mongo_class.Server.connect:  Removal of URI connection method.
- mongo_class.RepSet.connect:  Removal of URI connection method.


## [4.1.0] - 2020-12-01
- Updated to use pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.
- Added authentication mechanism to connection methods.
- Replaced pymongo.MongoClient.authenticate as it is being deprecated from the library module.

### Added
- mongo_libs.disconnect:  Disconnects a class database connection.

### Changed
- mongo_libs.ins_doc:  Replaced cmds_gen.disconnect with internal call to disconnect function.
- mongo_class.RepSetColl.connect:  Refactored method to remove the use of pymongo.MongoClient.authenticate.
- mongo_libs.crt_coll_inst:  Add authentication mechanism to the Coll and RepSetColl class arguments.
- mongo_libs.create_slv_array:  Add authentication mechanism to the SlaveRep class arguments.
- mongo_class.RepSetColl.\_\_init\_\_, mongo_class.RepSet.\_\_init\_\_, mongo_class.SlaveRep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_, mongo_class.Rep.\_\_init\_\_, mongo_class.Coll.\_\_init\_\_, mongo_class.DB.\_\_init\_\_:  Added auth_mech argument to super class function call.
- mongo_class.Server.\_\_init\_\_:  Added authMechanism to config attribute if not MONGODB-CR authentication mechanism.
- mongo_class.Server.\_\_init\_\_:  Added authentication mechanism attribute to class.
- Documentation updates.

### Deprecated
- mongo_class.RepSetColl.\_db_auth:  Method is being replaced due to the deprecation of pymongo.MongoClient.authenticate.


## [4.0.0] - 2020-08-17
Breaking Change.

### Fixed
- mongo_class.RepSetColl.\_db_auth:  Changed db_auth to db_auth_conn to avoid overwrite of attribute.

### Added
- mongo_class.RepSetColl.coll_options:  Return the collections option settings.
- mongo_class.RepSetColl.coll_find1:  Query of document using findOne command.
- mongo_class.RepSetColl.coll_dst:  Query of document using distinct command.
- mongo_class.RepSetColl.coll_find:  Query of document using find command.
- mongo_class.RepSetColl.\_db_auth:  Database authentication, private function for connect method.

### Changed
- mongo_class.RepSetColl.\_\_init\_\_:  Added db_auth_conn attribute.
- mongo_class.RepSetColl.connect:  Added try/exception on authentication to database.
- mongo_libs.ins_doc:  Captured return status from connect, added check for return status and returned status.
- mongo_class.RepSetColl.connect:  Added get_srv_attr call and return status to calling function.
- mongo_class.SlaveRep.connect, mongo_class.MasterRep.connect, mongo_class.Coll.connect, mongo_class.DB.db_connect, mongo_class.DB.connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.RepSet.connect, mongo_class.Server.connect:  Captured return status from get_srv_attr and returned status.
- mongo_class.Server.get_srv_attr, mongo_class.RepSet.\_\_init\_\_:  Removed sys.exit and replaced with status message return.
- mongo_class.RepSet.connect:  Changed uri connection to handle a null repset attribute setting.
- mongo_libs.crt_coll_inst:  Added in new class attributes to instance call.
- mongo_libs.create_slv_array, mongo_libs.create_instance:  Added in new class attributes to instance call.
- mongo_class.RepSet.connect:  Added capability to connect into Mongo using arguments.
- mongo_class.RepSetColl.\_\_init\_\_:  Passed new attributes to super command for the RepSet class.
- mongo_class.RepSet.\_\_init\_\_, mongo_class.SlaveRep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_:  Passed new attributes to super command for the Rep class.
- mongo_class.Rep.\_\_init\_\_, mongo_class.DB.\_\_init\_\_:  Passed new attributes to super command for the Server class.
- mongo_class.Coll.\_\_init\_\_:  Passed new attributes to super command for the DB class.
- mongo_class.Server.connect:  Added capability to connect into Mongo using arguments.
- mongo_class.Server.\_\_init\_\_:  Added a number of new attributes to handle connecting into Mongo using arguments.
- Documentation updates.

### Removed
- mongo_class:  Removed sys module.


## [3.1.0] - 2020-07-09
### Fixed
- mongo_class.RepSetColl.\_\_init\_\_:  Initialized db_conn and db_coll attributes.

### Changed
- Changed order of import of modules.
- mongo_class.DB.db_cmd:  Refactored function and remove else clause.
- mongo_class.DB.chg_db:  Changed variable name to standard naming convention.
- mongo_class.DB.db_connect, mongo_class.Server.upd_srv_stat, mongo_libs.ins_doc:  Changed variable name to standard naming convention.
- mongo_libs.crt_coll_inst:  Refactored function and remove else clause.
- mongo_libs.crt_base_cmd:  Refactored function to have only one return.
- mongo_class.Server.adm_cmd:  Refactored method and removed "if" statement.
- mongo_class.SlaveRep.connect, mongo_class.MasterRep.connect:  Removed sys.exit and replaced with status message return.
- mongo_class.MasterRep.connect:  Removed sys.exit and replaced with status message return.


## [3.0.1] - 2019-12-04
### Fixed
- mongo_libs.create_cmd:  Fixed incorrect typing of keyword argument.


## [3.0.0] - 2019-10-08
Breaking Change

### Fixed
- mongo_class.DB.validate_collection:  Add exception handler to deal with trying to validate views.

### Changed
- mongo_class.RepSetColl.\_\_init\_\_:  Changed check of repset attribute until after it is set.
- mongo_libs.crt_coll_inst:  Updated arguments to be passed as keyword arguments to mongo_class classes.
- mongo_class.RepSetColl.\_\_init\_\_, mongo_class.RepSet.\_\_init\_\_, mongo_class.RepSet.\_\_init\_\_, mongo_class.Coll.\_\_init\_\_, mongo_class.DB.\_\_init\_\_, mongo_class.Rep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_, mongo_class.SlaveRep.\_\_init\_\_, mongo_class.Server.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_libs.create_slv_array :  Updated arguments to be passed as keyword arguments to mongo_class SlaveRep class.
- mongo_libs.create_instance, mongo_libs.create_slv_array:  Added kwargs to argument list.
- mongo_libs.create_instance:  Updated arguments to be passed as keyword arguments to mongo_class classes.
- mongo_class.SlaveRep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_:  Removed connect() call from method.
- mongo_class.DB.\_\_init\_\_, mongo_class.Coll.\_\_init\_\_:  Removed connect() call from method.
- Documentation updates.

### Added
- mongo_class.SlaveRep.connect:  Connect method to a Mongo database for SlaveRep class.
- mongo_class.MasterRep.connect:  Connect method to a Mongo database for MasterRep class.
- mongo_class.Coll.connect:  Connect method to a Mongo database for Coll class.
- mongo_class.DB.connect:  Connect method to a Mongo database for DB class.

### Removed
- mongo_class.DB.isvalid_tbl
- mongo_libs.json_prt_ins_2_db
- mongo_libs.json_2_out


## [2.1.2] - 2019-07-22
### Change
- mongo_class.RepSetColl.connect, mongo_class.RepSet.connect:  Changed conn_list to connections for readability.
- mongo_class.Server.disconnect:  Removed returning Null connection status.
- mongo_class.Server.upd_server_attr:  Refactored method and improved checking.

### Fixed
- mongo_libs.ins_doc, mongo_libs.create_slv_array, mongo_libs.create_cmd:  Fixed problem with mutable default arguments issue.
- mongo_class.RepSetColl.coll_del_many:  Replaced qry with an empty document ({}) to allow for collection truncation.
- mongo_class.Server.upd_srv_stat, mongo_class.fetch_ismaster, mongo_class.fetch_db_info, mongo_class.fetch_cmd_line,mongo_libs.ins_doc, mongo_libs.crt_base_cmd, mongo_libs.create_slv_array, mongo_libs.create_instance, mongo_libs.create_cmd:  Fixed Sonarqube findings.

### Deprecated
- mongo_libs.json_prt_ins_2_db function.
- mongo_libs.json_2_out function.


## [2.1.1] - 2018-11-27
### Fixed
- mongo_class.Coll.coll_cnt, mongo_class.Coll.coll_find, mongo_class.Coll.coll_find1, mongo_class.RepSetColl.coll_cnt:  Changed function parameter mutable argument default to immutable argument default.


## [2.1.0] - 2018-09-12
### Updated
- mongo_libs.create_instance:  Changed "gen_libs.Load_Module" to "gen_libs.load_module" call.
- mongo_libs.create_cmd:  Changed "arg_parser.Arg_Set_Path" to "arg_parser.arg_set_path" call.
- mongo_libs.create_cmd:  Changed "cmds_gen.Add_Cmd" to "cmds_gen.add_cmd" call.
- mongo_libs.create_cmd:  Changed "cmds_gen.Is_Add_Cmd" to "cmds_gen.is_add_cmd" call.
- mongo_libs.ins_doc:  Changed "cmds_gen.Disconnect" to "cmds_gen.disconnect" call.
- mongo_libs.py:  Changed "Ins_Doc" to "ins_doc" calls.
- mongo_libs.py:  Changed "gen_libs.Print_Data" to "gen_libs.print_data" calls.

### Removed
- mongo_libs.Crt_Base_Cmd
- mongo_libs.Create_Cmd
- mongo_libs.JSON_2_Out
- mongo_libs.JSON_Prt_Ins_2_DB
- mongo_libs.Create_Instance
- mongo_libs.Crt_Coll_Inst
- mongo_libs.Ins_Doc
- mongo_libs.Fetch_Cmd_Line
- mongo_libs.Fetch_Db_Info
- mongo_libs.Fetch_isMaster
- mongo_libs.Display_Data
- mongo_libs.Create_Slv_Array
- mongo_class.Rep_Set
- mongo_class.Rep_Set_Coll
- mongo_class.Slave_Rep
- mongo_class.Master_Rep


## [2.0.0] - 2018-03-08
Breaking Change

### Changed
- Renamed cmds_mongo.py to mongo_libs.py.
- Renamed svr_mongo.py to mongo_class.py.
- mongo_class.SlaveRep.\_\_init\_\_, mongo_class.MasterRep.\_\_init\_\_, mongo_class.Server.upd_server_attr:  Changed mongo_libs reference to new naming schema.
- mongo_libs.py: Changed mongo_class classes to new naming schema.
- mongo_libs.py: Changed svr_mongo references to mongo_class references.
- mongo_class.py:  Changed cmds_mongo references to mongo_libs references.
- mongo_libs.py:  Change to single-source version control.
- mongo_class.py:  Change to single-source version control.
- mongo_class.py:  Changed cmds_mongo to mongo_libs.

### Added
- mongo_libs.crt_coll_inst function:  Replaces mongo_libs.Crt_Coll_Inst.
- mongo_libs.ins_doc function:  Replaces mongo_libs.Ins_Doc.
- mongo_libs.json_prt_ins_2_db function:  Replaces mongo_libs.JSON_Prt_Ins_2_DB.
- mongo_libs.json_2_out function:  Replaces mongo_libs.JSON_2_Out.
- mongo_libs.crt_base_cmd function:  Replaces mongo_libs.Crt_Base_Cmd.
- mongo_libs.create_cmd function:  Replaces mongo_libs.Create_Cmd.
- mongo_libs.create_instance function:  Replaces mongo_libs.Create_Instance.
- mongo_class.fetch_cmd_line function:  Replaces mongo_libs.Fetch_Cmd_Line.
- mongo_class.fetch_db_info function:  Replaces mongo_libs.Fetch_Db_Info.
- mongo_class.fetch_ismaster function:  Replaces mongo_libs.Fetch_isMaster.
- mongo_libs.create_slv_array function:  Replaces mongo_libs.Create_Slv_Array.
- mongo_class.MasterRep class:  Replaces mongo_class.Master_Rep.
- mongo_class.SlaveRep class:  Replaces mongo_class.Slave_Rep.
- mongo_class.RepSet class:  Replaces mongo_class.Rep_Set.
- mongo_class.RepSetColl class:  Replaces mongo_class.Rep_Set_Coll.

### Deprecated
- mongo_libs.Crt_Coll_Inst function:  Replaced by mongo_libs.crt_coll_inst.
- mongo_libs.Ins_Doc function:  Replaced by mongo_libs.ins_doc.
- mongo_libs.JSON_Prt_Ins_2_DB function:  Replaced by mongo_libs.json_prt_ins_2_db.
- mongo_libs.JSON_2_Out function:  Replaced by mongo_libs.json_2_out.
- mongo_libs.Crt_Base_Cmd function:  Replaced by mongo_libs.crt_base_cmd.
- mongo_libs.Create_Cmd function:  Replaced by mongo_libs.create_cmd.
- mongo_libs.Create_Instance function:  Replaced by mongo_libs.create_instance.
- mongo_libs.Fetch_Cmd_Line function:  Replaced by mongo_class.fetch_cmd_line.
- mongo_libs.Fetch_Db_Info function:  Replaced by mongo_class.fetch_db_info.
- mongo_libs.Fetch_isMaster function:  Replaced by mongo_class.fetch_ismaster.
- mongo_libs.Create_Slv_Array function:  Replaced by mongo_libs.create_slv_array.
- mongo_libs.Display_Data function:  Replaced by gen_libs.Display_Data.
- mongo_class.Master_Rep class:  Replaced by mongo_class.MasterRep.
- mongo_class.Slave_Rep class:  Replaced by mongo_class.SlaveRep.
- mongo_class.Rep_Set class:  Replaced by mongo_class.RepSet.
- mongo_class.Rep_Set_Coll class:  Replaced by mongo_class.RepSetColl.


## [1.13.1] - 2018-03-05
### Updated
- Documentation update.


## [1.13.0] - 2018-02-28
### Updated
- cmds_mongo.py:  Added single-source version control.
- svr_mongo.py:  Added single-source version control.


## [1.12.0] - 2017-08-14
### Changed
- cmds_mongo.py:  Change single quotes to double quotes.
- cmds_mongo.py:  Convert program to use local libraries from ./lib directory.
- svr_mongo.py:  Change single quotes to double quotes.


## [1.11.0] - 2017-05-12
### Added
- svr_mongo.Coll:  Added coll_options method.


## [1.10.0] - 2017-04-17
### Added
- cmds_mongo.py:  Crt_Coll_Inst function.
- svr_mongo.Rep_Set_Coll:  Added ins_doc method.

### Changed
- cmds_mongo.Ins_Doc:  Replaced class instance call with a function which will determine if connection is a single or replica set connection.


## [1.9.0] - 2017-04-12
### Added
- svr_mongo.DB:  Added validate_tbl method to insert document into database in a replica set connection.

### Changed
- svr_mongo.DB:  Replaced isvalid_tbl method with validate_tbl to more accurately reflect the functions definition.

### Deprecated
- svr_mongo.DB:  isvalid_tbl method


## [1.8.0] - 2016-12-06
### Changed
- svr_mongo.Rep_Set.\_\_init\_\_:  Added repset_hosts to initilization.
- svr_mongo.Rep_Set.connect:  Use repset_hosts if it is populated.

### Added
- cmds_mongo:  Crt_Base_Cmd function.
- cmds_mongo:  Create_Cmd function.
- svr_mongo:  Rep_Set_Coll class - Connecting to a collection within a replication set.


## [1.7.0] - 2016-04-28
### Added
- cmds_mongo:  JSON_2_Out function.

### Changed
- svr_mongo.Server.adm_cmd:  Added "if" statement to deal with named argument.
- svr_mongo.Server.adm_cmd:  Removed the self.connect command as this no longer required.


## [1.6.0] - 2016-04-19
### Added
- cmds_mongo:  JSON_Prt_Ins_2_DB function.
- svr_mongo.Server:  upd_srv_stat method.
- svr_mongo:  Added psutil and socket modules.

### Changed
- svr_mongo.Server.\_\_init\_\_:  Added attributes for the Servers memory and other status configuration settings.


## [1.5.0] - 2016-03-17
### Added
- cmds_mongo:  Ins_Doc function.
- svr_mongo.Coll:  ins_doc method - Insert document into collection.


## [1.4.0] - 2016-03-09
### Added
- svr_mongo.DB:  chg_db method - Change database instance to new db.
- svr_mongo.DB:  get_tbl_list method - Return list of tables in db.
- svr_mongo.DB:  isvalid_tbl method - Validates a table in a db.

### Fixed
- svr_mongo.DB.db_connect:  Corrected error in "if" statement.


## [1.3.0] - 2016-03-04
### Changed
- svr_mongo.RepSet.connect:  Changed conn_list to a string type.


## [1.2.0] - 2016-02-29
### Added
- cmds_mongo.py:  Initial program creation.

### Changed
- svr_mongo.Server.upd_server_attr: Corrected parsing error.


## [1.1.0] - 2016-02-19
### Added
- svr_mongo:  Coll class

### Changed
- svr_mongo.DB.\_\_init\_\_: Added attribute db_name.


## [1.0.0] - 2016-02-09
- svr_mongo.py:  Initial program creation.

