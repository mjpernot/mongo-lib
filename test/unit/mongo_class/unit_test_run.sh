#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mongo_class"  
test/unit/mongo_class/fetch_cmd_line.py
test/unit/mongo_class/fetch_db_info.py
test/unit/mongo_class/fetch_ismaster.py
test/unit/mongo_class/coll_coll_cnt.py
test/unit/mongo_class/coll_coll_dst.py
test/unit/mongo_class/coll_coll_find.py
test/unit/mongo_class/coll_coll_find1.py
test/unit/mongo_class/coll_coll_options.py
test/unit/mongo_class/coll_connect.py
test/unit/mongo_class/coll_init.py
test/unit/mongo_class/coll_ins_doc.py
test/unit/mongo_class/db_chg_db.py
test/unit/mongo_class/db_connect.py
test/unit/mongo_class/db_db_cmd.py
test/unit/mongo_class/db_db_connect.py
test/unit/mongo_class/db_get_tbl_list.py
test/unit/mongo_class/db_init.py
test/unit/mongo_class/db_validate_tbl.py
test/unit/mongo_class/masterrep_connect.py
test/unit/mongo_class/masterrep_init.py
test/unit/mongo_class/repsetcoll_coll_cnt.py
test/unit/mongo_class/repsetcoll_coll_del_many.py
test/unit/mongo_class/repsetcoll_connect.py
test/unit/mongo_class/repsetcoll_db_auth.py
test/unit/mongo_class/repsetcoll_init.py
test/unit/mongo_class/repsetcoll_ins_doc.py
test/unit/mongo_class/repset_connect.py
test/unit/mongo_class/repset_init.py
test/unit/mongo_class/rep_fetch_nodes.py
test/unit/mongo_class/rep_init.py
test/unit/mongo_class/server_connect.py
test/unit/mongo_class/server_disconnect.py
test/unit/mongo_class/server_fetch_adr.py
test/unit/mongo_class/server_fetch_dbs.py
test/unit/mongo_class/server_fetch_svr_info.py
test/unit/mongo_class/server_get_server_attr.py
test/unit/mongo_class/server_init.py
test/unit/mongo_class/server_is_locked.py
test/unit/mongo_class/server_is_primary.py
test/unit/mongo_class/server_fetch_svr_info.py
test/unit/mongo_class/server_lock_db.py
test/unit/mongo_class/server_unlock_db.py
test/unit/mongo_class/server_upd_server_attr.py
test/unit/mongo_class/server_upd_srv_stat.py
test/unit/mongo_class/slaverep_connect.py
test/unit/mongo_class/slaverep_init.py

