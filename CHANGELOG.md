# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.1.1] - 2018-11-27
### Changed
- Documentation updates.


## [2.1.0] - 2018-09-12
### Added
- requirements-mongo-lib.txt:  Mongo support library install via pip.
- requirements-python-lib.txt:  General Python support library install via pip.
- requirements.txt:  System support library install via pip.

### Updated
- mongo_libs.create_instance:  Changed "gen_libs.Load_Module" to "gen_libs.load_module" call.
- mongo_libs.create_cmd:  Changed "arg_parser.Arg_Set_Path" to "arg_parser.arg_set_path" call.
- mongo_libs.create_cmd:  Changed "cmds_gen.Add_Cmd" to "cmds_gen.add_cmd" call.
- mongo_libs.create_cmd:  Changed "cmds_gen.Is_Add_Cmd" to "cmds_gen.is_add_cmd" call.
- mongo_libs.ins_doc:  Changed "cmds_gen.Disconnect" to "cmds_gen.disconnect" call.
- mongo_libs.py:  Changed "Ins_Doc" to "ins_doc" calls.
- mongo_libs.py:  Changed "gen_libs.Print_Data" to "gen_libs.print_data" calls.

### Removed
- mongo_libs.Crt_Base_Cmd: Function was previously deprecated.
- mongo_libs.Create_Cmd: Function was previously deprecated.
- mongo_libs.JSON_2_Out: Function was previously deprecated.
- mongo_libs.JSON_Prt_Ins_2_DB: Function was previously deprecated.
- mongo_libs.Create_Instance: Function was previously deprecated.
- mongo_libs.Crt_Coll_Inst: Function was previously deprecated.
- mongo_libs.Ins_Doc: Function was previously deprecated.
- mongo_libs.Fetch_Cmd_Line: Function was previously deprecated.
- mongo_libs.Fetch_Db_Info: Function was previously deprecated.
- mongo_libs.Fetch_isMaster: Function was previously deprecated.
- mongo_libs.Display_Data: Function was previously deprecated.
- mongo_libs.Create_Slv_Array: Function was previously deprecated.
- mongo_class.Rep_Set:  Class was previously deprecated.
- mongo_class.Rep_Set_Coll:  Class was previously deprecated.
- mongo_class.Slave_Rep:  Class was previously deprecated.
- mongo_class.Master_Rep:  Class was previously deprecated.
- requirements2.txt:  No longer required - contents moved to requirements.txt.


## [2.0.0] - 2018-03-08
Breaking Change

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

### Changed
- mongo_class.SlaveRep.__init__:  Changed mongo_libs reference to new naming schema.
- mongo_class.MasterRep.__init__:  Changed mongo_libs reference to new naming schema.
- mongo_class.Server.upd_server_attr:  Changed mongo_libs reference to new naming schema.
- mongo_libs.py: Changed mongo_class classes to new naming schema.
- mongo_libs.py: Changed svr_mongo references to mongo_class references.
- mongo_class.py:  Changed cmds_mongo references to mongo_libs references.
- mongo_libs.py:  Change to single-source version control.
- mongo_class.py:  Change to single-source version control.
- mongo_class.py:  Changed cmds_mongo to mongo_libs.
- mongo_libs.py:  Made program PEP-8 compliant.
- Merge version changed in mongo_libs.py into CHANGELOG.md file.
- setup.py:  Changed cmds_mongo to mongo_libs in py_modules option.
- Renamed cmds_mongo.py to mongo_libs.py - standardize the library naming convention.
- mongo_class.py:  Made program PEP-8 compliant.
- Merge version changed in mongo_class.py into CHANGELOG.md file.
- setup.py:  Changed svr_mongo to mongo_class in py_modules option.
- Renamed svr_mongo.py to mongo_class.py - standardize the class naming convention.

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
### Fixed
- setup.py:  Fixed py_modules option as it was not installing cmds_mongo.py program.


## [1.13.0] - 2018-02-28
### Added
- Moved svr_mongo.py from python_project to this project.
- Moved cmds_mongo.py from python_project to this project.
- version.py:  Added single-source version control module.
- __init__.py:  Stub header to allow class to be imported in sub-directory.
- setup.py:  Added setuptools module.
- requirements2.txt:  Add specific support libraries for the programs.
- README.md:  Added README file.


## [1.12.0] - 2017-08-14
### Changed
- cmds_mongo.py:  Add classification line for Sunspear use.
- cmds_mongo.py:  Convert comments/documentation to docstrings.
- cmds_mongo.py:  Change order of library sequence to be PEP-8 compliant.
- cmds_mongo.py:  Change versioning information to be PEP-440 compliant.
- cmds_mongo.py:  Change single quotes to double quotes to be PEP-8 compliant.
- cmds_mongo.py:  Convert program to use local libraries from ./lib directory.
- svr_mongo.py:  Add classification line for Sunspear use.
- svr_mongo.py:  Convert comments/documentation to docstrings.
- svr_mongo.py:  Change order of library sequence to be PEP-8 compliant.
- svr_mongo.py:  Change versioning information to be PEP-440 compliant.
- svr_mongo.py:  Change single quotes to double quotes to be PEP-8 compliant.


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
- svr_mongo.Rep_Set.__init__:  Added repset_hosts to initilization.
- svr_mongo.Rep_Set.connect:  Use repset_hosts if it is populated.

### Added
- cmds_mongo:  Crt_Base_Cmd function.
- cmds_mongo:  Create_Cmd function.
- Added arg_parser library.
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
- svr_mongo.Server.__init__:  Added attributes for the Servers memory and other status configuration settings.


## [1.5.0] - 2016-03-17
### Added
- cmds_mongo:  Ins_Doc function.
- Added new libraries for Ins_Doc function.
- svr_mongo.Coll:  ins_doc method - Insert document into collection.


## [1.4.0] - 2016-03-09
### Added
- svr_mongo.DB:  chg_db method - Change database instance to new db.
- svr_mongo.DB:  get_tbl_list method - Return list of tables in db.
- svr_mongo.DB:  isvalid_tbl method - Validates a table in a db.

### Fixed
- svr_mongo.DB.db_connect:  Corrected error in 'if' statement.


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
- svr_mongo.DB.__init__: Added attribute db_name.


## [1.0.0] - 2016-02-09
- svr_mongo.py:  Initial program creation.

