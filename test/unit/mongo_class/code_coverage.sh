#!/bin/bash
# Unit test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_classtest/unit/mongo_class/MasterRep_init.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSetColl_coll_cnt.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSetColl_coll_del_many.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSetColl_connect.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSetColl_init.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSetColl_ins_doc.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSet_connect.py
coverage run -a --source=mongo_classtest/unit/mongo_class/RepSet_init.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Rep_fetch_nodes.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Rep_init.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_connect.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_disconnect.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_fetch_adr.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_init.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_is_locked.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_is_primary.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_upd_server_attr.py
coverage run -a --source=mongo_classtest/unit/mongo_class/Server_upd_srv_stat.py
coverage run -a --source=mongo_classtest/unit/mongo_class/SlaveRep_init.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
