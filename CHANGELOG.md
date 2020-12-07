# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.1.0] - 2020-12-01
- Updated to use pymongo v3.8.0.
- Updated to be used in FIPS environment.
- Added authentication mechanism to connection methods.

### Changed
- mongo_class.Rep.\_\_init\_\_:  Added auth_mech argument to super class function call.
- mongo_class.Coll.\_\_init\_\_:  Added auth_mech argument to super class function call.
- mongo_class.DB.\_\_init\_\_:  Added auth_mech argument to super class function call.
- mongo_class.Server.\_\_init\_\_:  Added authMechanism to config attribute if not MONGODB-CR authentication mechanism.
- mongo_class.Server.\_\_init\_\_:  Added authentication mechanism attribute to class.
- Documentation updates.


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
- mongo_class.SlaveRep.connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.MasterRep.connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.Coll.connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.DB.db_connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.DB.connect:  Captured return status from connect, added check for return status and returned status.
- mongo_class.RepSet.connect:  Captured return status from get_srv_attr and returned status.
- mongo_class.Server.connect:  Captured return status from get_srv_attr and returned status.
- mongo_class.Server.get_srv_attr:  Removed sys.exit and replaced with status message return.
- mongo_class.RepSet.\_\_init\_\_:  Removed sys.exit on checking existence of repset attribute.
- mongo_class.RepSet.connect:  Changed uri connection to handle a null repset attribute setting.
- mongo_libs.crt_coll_inst:  Added in new class attributes to instance call.
- mongo_libs.create_slv_array:  Added in new class attributes to instance call.
- mongo_libs.create_instance:  Added in new class attributes to instance call.
- mongo_class.RepSetColl.\_\_init\_\_:  Passed new attributes to super command for the RepSet class.
- mongo_class.RepSet.connect:  Added capability to connect into Mongo using arguments.
- mongo_class.RepSet.\_\_init\_\_:  Passed new attributes to super command for the Rep class.
- mongo_class.SlaveRep.\_\_init\_\_:  Passed new attributes to super command for the Rep class.
- mongo_class.MasterRep.\_\_init\_\_:  Passed new attributes to super command for the Rep class.
- mongo_class.Rep.\_\_init\_\_:  Passed new attributes to super command for the Server class.
- mongo_class.Coll.\_\_init\_\_:  Passed new attributes to super command for the DB class.
- mongo_class.DB.\_\_init\_\_:  Passed new attributes to super command for the Server class.
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
- mongo_class.DB.db_connect:  Changed variable name to standard naming convention.
- mongo_class.Server.upd_srv_stat:  Changed variable name to standard naming convention.
- mongo_libs.ins_doc:  Changed variable name to standard naming convention.
- mongo_libs.crt_coll_inst:  Refactored function and remove else clause.
- mongo_libs.crt_base_cmd:  Refactored function to have only one return.
- mongo_class.Server.adm_cmd:  Refactored method and removed "if" statement.
- mongo_class.SlaveRep.connect:  Removed sys.exit and replaced with status message return.
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
- mongo_class.RepSetColl.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_class.RepSet.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_class.Coll.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_libs.crt_coll_inst:  Updated arguments to be passed as keyword arguments to mongo_class classes.
- mongo_class.DB.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_class.Rep.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_class.MasterRep.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_class.SlaveRep.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_libs.create_slv_array :  Updated arguments to be passed as keyword arguments to mongo_class SlaveRep class.
- mongo_libs.create_instance:  Added kwargs to argument list.
- mongo_libs.create_slv_array:  Added kwargs to argument list.
- mongo_class.Server.\_\_init\_\_:  Changed a number of arguments to be passed in as kwargs.
- mongo_libs.create_instance:  Updated arguments to be passed as keyword arguments to mongo_class classes.
- mongo_class.SlaveRep.\_\_init\_\_:  Removed connect() call from method.
- mongo_class.MasterRep.\_\_init\_\_:  Removed connect() call from method.
- mongo_class.DB.\_\_init\_\_:  Removed connect() call from method.
- mongo_class.Coll.\_\_init\_\_:  Removed connect() call from method.
- Documentation updates.

### Added
- mongo_class.SlaveRep.connect:  Connect method to a Mongo database for SlaveRep class.
- mongo_class.MasterRep.connect:  Connect method to a Mongo database for MasterRep class.
- mongo_class.Coll.connect:  Connect method to a Mongo database for Coll class.
- mongo_class.DB.connect:  Connect method to a Mongo database for DB class.

### Removed
- mongo_class.DB.isvalid_tbl:  Method has been replaced with validate_tbl method.
- mongo_libs.json_prt_ins_2_db:  Function is no longer required.
- mongo_libs.json_2_out:  Function is no longer required.


## [2.1.2] - 2019-07-22
### Change
- mongo_class.RepSetColl.connect:  Changed conn_list to connections for readability.
- mongo_class.RepSet.connect:  Changed conn_list to connections for readability.
- mongo_class.Server.disconnect:  Removed returning Null connection status.
- mongo_class.Server.upd_server_attr:  Refactored method and improved checking.

### Fixed
- mongo_libs.ins_doc:  Fixed problem with mutable default arguments issue.
- mongo_libs.create_slv_array:  Fixed problem with mutable default arguments issue.
- mongo_libs.create_cmd:  Fixed problem with mutable default arguments issue.
- mongo_class.RepSetColl.coll_del_many:  Replaced qry with an empty document ({}) to allow for collection truncation.
- mongo_class.Server.upd_srv_stat:  Fixed two vulnerabilities from Sonarqube findings.
- mongo_class.fetch_ismaster:  Fixed Sonarqube findings.
- mongo_class.fetch_db_info:  Fixed Sonarqube findings.
- mongo_class.fetch_cmd_line:  Fixed Sonarqube findings.
- mongo_libs.ins_doc:  Fixed Sonarqube findings.
- mongo_libs.crt_base_cmd:  Fixed Sonarqube findings.
- mongo_libs.create_slv_array:  Fixed Sonarqube findings.
- mongo_libs.create_instance:  Fixed Sonarqube findings.
- mongo_libs.create_cmd:  Fixed Sonarqube findings.

### Deprecated
- mongo_libs.json_prt_ins_2_db function.
- mongo_libs.json_2_out function.


## [2.1.1] - 2018-11-27
### Fixed
- mongo_class.Coll.coll_cnt:  Changed function parameter mutable argument default to immutable argument default.
- mongo_class.Coll.coll_find:  Changed function parameter mutable argument default to immutable argument default.
- mongo_class.Coll.coll_find1:  Changed function parameter mutable argument default to immutable argument default.
- mongo_class.RepSetColl.coll_cnt:  Changed function parameter mutable argument default to immutable argument default.


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
- mongo_class.SlaveRep.\_\_init\_\_:  Changed mongo_libs reference to new naming schema.
- mongo_class.MasterRep.\_\_init\_\_:  Changed mongo_libs reference to new naming schema.
- mongo_class.Server.upd_server_attr:  Changed mongo_libs reference to new naming schema.
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

