#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
#coverage run -a --source=mongo_class test/integration/mongo_class/fetch_cmd_line.py
#coverage run -a --source=mongo_class test/integration/mongo_class/fetch_db_info.py
#coverage run -a --source=mongo_class test/integration/mongo_class/fetch_ismaster.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_coll_cnt.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_coll_dst.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_coll_find.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_coll_find1.py
#coverage run -a --source=mongo_class test/integration/mongo_class/coll_coll_options.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/coll_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_chg_db.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_db_cmd.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_db_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_get_tbl_list.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/db_validate_tbl.py
#coverage run -a --source=mongo_class test/integration/mongo_class/masterrep_connect.py
#coverage run -a --source=mongo_class test/integration/mongo_class/masterrep_init.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_cnt.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_del_many.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_dst.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_find.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_find1.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_options.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_connect.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_db_auth.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_init.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_ins_doc.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repset_connect.py
#coverage run -a --source=mongo_class test/integration/mongo_class/repset_init.py
#coverage run -a --source=mongo_class test/integration/mongo_class/rep_fetch_nodes.py
#coverage run -a --source=mongo_class test/integration/mongo_class/rep_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_adm_cmd.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_disconnect.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_fetch_adr.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_fetch_dbs.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_fetch_svr_info.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_get_server_attr.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_is_locked.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_is_primary.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_upd_server_attr.py
coverage run -a --source=mongo_class test/integration/mongo_class/server_upd_srv_stat.py
#coverage run -a --source=mongo_class test/integration/mongo_class/slaverep_connect.py
#coverage run -a --source=mongo_class test/integration/mongo_class/slaverep_init.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
