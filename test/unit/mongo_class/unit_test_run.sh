#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mongo_class"  
test/unit/mongo_class/fetch_cmd_line.py
test/unit/mongo_class/fetch_db_info.py
test/unit/mongo_class/fetch_ismaster.py
test/unit/mongo_class/Coll_coll_cnt.py
test/unit/mongo_class/Coll_coll_dst.py
test/unit/mongo_class/Coll_coll_find.py
test/unit/mongo_class/Coll_coll_find1.py
test/unit/mongo_class/Coll_coll_options.py
test/unit/mongo_class/Coll_connect.py
test/unit/mongo_class/Coll_init.py
test/unit/mongo_class/Coll_ins_doc.py
test/unit/mongo_class/DB_chg_db.py
test/unit/mongo_class/DB_connect.py
test/unit/mongo_class/DB_db_cmd.py
test/unit/mongo_class/DB_db_connect.py
test/unit/mongo_class/DB_get_tbl_list.py
test/unit/mongo_class/DB_init.py
test/unit/mongo_class/DB_validate_tbl.py
test/unit/mongo_class/MasterRep_connect.py
test/unit/mongo_class/MasterRep_init.py
test/unit/mongo_class/RepSetColl_coll_cnt.py
test/unit/mongo_class/RepSetColl_coll_del_many.py
test/unit/mongo_class/RepSetColl_connect.py
test/unit/mongo_class/RepSetColl_init.py
test/unit/mongo_class/RepSetColl_ins_doc.py
test/unit/mongo_class/RepSet_connect.py
test/unit/mongo_class/RepSet_init.py
test/unit/mongo_class/Rep_fetch_nodes.py
test/unit/mongo_class/Rep_init.py
test/unit/mongo_class/Server_connect.py
test/unit/mongo_class/Server_disconnect.py
test/unit/mongo_class/Server_fetch_adr.py
test/unit/mongo_class/Server_fetch_dbs.py
test/unit/mongo_class/Server_fetch_svr_info.py
test/unit/mongo_class/Server_get_server_attr.py
test/unit/mongo_class/Server_init.py
test/unit/mongo_class/Server_is_locked.py
test/unit/mongo_class/Server_is_primary.py
test/unit/mongo_class/Server_fetch_svr_info.py
test/unit/mongo_class/Server_lock_db.py
test/unit/mongo_class/Server_unlock_db.py
test/unit/mongo_class/Server_upd_server_attr.py
test/unit/mongo_class/Server_upd_srv_stat.py
test/unit/mongo_class/SlaveRep_connect.py
test/unit/mongo_class/SlaveRep_init.py

