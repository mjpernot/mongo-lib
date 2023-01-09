#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.
# Note:  Those test files commented out require a Mongo replica set, see replica_integration_test_run.sh.

echo "Unit test: mongo_class"  
/usr/bin/python ./test/integration/mongo_class/fetch_cmd_line.py
/usr/bin/python ./test/integration/mongo_class/fetch_db_info.py
/usr/bin/python ./test/integration/mongo_class/fetch_ismaster.py
/usr/bin/python ./test/integration/mongo_class/coll_coll_cnt.py
/usr/bin/python ./test/integration/mongo_class/coll_coll_dst.py
/usr/bin/python ./test/integration/mongo_class/coll_coll_find.py
/usr/bin/python ./test/integration/mongo_class/coll_coll_find1.py
/usr/bin/python ./test/integration/mongo_class/coll_coll_options.py
/usr/bin/python ./test/integration/mongo_class/coll_connect.py
/usr/bin/python ./test/integration/mongo_class/coll_init.py
/usr/bin/python ./test/integration/mongo_class/db_chg_db.py
/usr/bin/python ./test/integration/mongo_class/db_connect.py
/usr/bin/python ./test/integration/mongo_class/db_db_cmd.py
/usr/bin/python ./test/integration/mongo_class/db_db_connect.py
/usr/bin/python ./test/integration/mongo_class/db_get_tbl_list.py
/usr/bin/python ./test/integration/mongo_class/db_init.py
/usr/bin/python ./test/integration/mongo_class/db_validate_tbl.py
#test/integration/mongo_class/masterrep_connect.py
/usr/bin/python ./test/integration/mongo_class/masterrep_init.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_coll_cnt.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_coll_dst.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_coll_find.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_coll_find1.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_coll_options.py
#test/integration/mongo_class/repsetcoll_connect.py
/usr/bin/python ./test/integration/mongo_class/repsetcoll_init.py
#test/integration/mongo_class/repset_connect.py
/usr/bin/python ./test/integration/mongo_class/repset_init.py
/usr/bin/python ./test/integration/mongo_class/rep_fetch_nodes.py
/usr/bin/python ./test/integration/mongo_class/rep_init.py
/usr/bin/python ./test/integration/mongo_class/server_adm_cmd.py
/usr/bin/python ./test/integration/mongo_class/server_connect.py
/usr/bin/python ./test/integration/mongo_class/server_disconnect.py
/usr/bin/python ./test/integration/mongo_class/server_fetch_adr.py
/usr/bin/python ./test/integration/mongo_class/server_fetch_dbs.py
/usr/bin/python ./test/integration/mongo_class/server_fetch_svr_info.py
/usr/bin/python ./test/integration/mongo_class/server_get_server_attr.py
/usr/bin/python ./test/integration/mongo_class/server_init.py
/usr/bin/python ./test/integration/mongo_class/server_is_locked.py
/usr/bin/python ./test/integration/mongo_class/server_is_primary.py
/usr/bin/python ./test/integration/mongo_class/server_upd_server_attr.py
/usr/bin/python ./test/integration/mongo_class/server_upd_srv_stat.py
#test/integration/mongo_class/slaverep_connect.py
/usr/bin/python ./test/integration/mongo_class/slaverep_init.py

