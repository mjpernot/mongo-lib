#!/bin/bash
# Unit test code coverage for SonarQube to cover all library modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_class test/unit/mongo_class/fetch_cmd_line.py
coverage run -a --source=mongo_class test/unit/mongo_class/fetch_db_info.py
coverage run -a --source=mongo_class test/unit/mongo_class/fetch_ismaster.py
coverage run -a --source=mongo_class test/unit/mongo_class/DB_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/MasterRep_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSetColl_coll_cnt.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSetColl_coll_del_many.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSetColl_connect.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSetColl_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSetColl_ins_doc.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSet_connect.py
coverage run -a --source=mongo_class test/unit/mongo_class/RepSet_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/Rep_fetch_nodes.py
coverage run -a --source=mongo_class test/unit/mongo_class/Rep_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_connect.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_disconnect.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_fetch_adr.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_fetch_dbs.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_fetch_svr_info.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_init.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_is_locked.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_is_primary.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_lock_db.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_unlock_db.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_upd_server_attr.py
coverage run -a --source=mongo_class test/unit/mongo_class/Server_upd_srv_stat.py
coverage run -a --source=mongo_class test/unit/mongo_class/SlaveRep_init.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/create_cmd.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/create_instance.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/create_slv_array.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/crt_base_cmd.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/crt_coll_inst.py
coverage run -a --source=mongo_libs test/unit/mongo_libs/ins_doc.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

