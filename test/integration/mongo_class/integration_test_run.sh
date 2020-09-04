#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mongo_class"  
#test/integration/mongo_class/fetch_cmd_line.py
#test/integration/mongo_class/fetch_db_info.py
#test/integration/mongo_class/fetch_ismaster.py
test/integration/mongo_class/coll_coll_cnt.py
test/integration/mongo_class/coll_coll_dst.py
test/integration/mongo_class/coll_coll_find.py
test/integration/mongo_class/coll_coll_find1.py
test/integration/mongo_class/coll_coll_options.py
test/integration/mongo_class/coll_connect.py
test/integration/mongo_class/coll_init.py
test/integration/mongo_class/db_chg_db.py
test/integration/mongo_class/db_connect.py
test/integration/mongo_class/db_db_cmd.py
test/integration/mongo_class/db_db_connect.py
test/integration/mongo_class/db_get_tbl_list.py
test/integration/mongo_class/db_init.py
test/integration/mongo_class/db_validate_tbl.py
test/integration/mongo_class/masterrep_connect.py
test/integration/mongo_class/masterrep_init.py
#test/integration/mongo_class/repsetcoll_coll_cnt.py
#test/integration/mongo_class/repsetcoll_coll_del_many.py
#test/integration/mongo_class/repsetcoll_coll_dst.py
#test/integration/mongo_class/repsetcoll_coll_find.py
#test/integration/mongo_class/repsetcoll_coll_find1.py
#test/integration/mongo_class/repsetcoll_coll_options.py
#test/integration/mongo_class/repsetcoll_connect.py
#test/integration/mongo_class/repsetcoll_db_auth.py
#test/integration/mongo_class/repsetcoll_init.py
#test/integration/mongo_class/repsetcoll_ins_doc.py
#test/integration/mongo_class/repset_connect.py
#test/integration/mongo_class/repset_init.py
test/integration/mongo_class/rep_fetch_nodes.py
test/integration/mongo_class/rep_init.py
test/integration/mongo_class/server_adm_cmd.py
test/integration/mongo_class/server_connect.py
test/integration/mongo_class/server_disconnect.py
test/integration/mongo_class/server_fetch_adr.py
test/integration/mongo_class/server_fetch_dbs.py
test/integration/mongo_class/server_fetch_svr_info.py
test/integration/mongo_class/server_get_server_attr.py
test/integration/mongo_class/server_init.py
test/integration/mongo_class/server_is_locked.py
test/integration/mongo_class/server_is_primary.py
test/integration/mongo_class/server_upd_server_attr.py
test/integration/mongo_class/server_upd_srv_stat.py
#test/integration/mongo_class/slaverep_connect.py
test/integration/mongo_class/slaverep_init.py

