#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_class test/integration/mongo_class/fetch_ismaster.py
coverage run -a --source=mongo_class test/integration/mongo_class/masterrep_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/masterrep_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_cnt.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_dst.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_find.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_find1.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_coll_options.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/repsetcoll_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/repset_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/repset_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/rep_fetch_nodes.py
coverage run -a --source=mongo_class test/integration/mongo_class/rep_init.py
coverage run -a --source=mongo_class test/integration/mongo_class/slaverep_connect.py
coverage run -a --source=mongo_class test/integration/mongo_class/slaverep_init.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
