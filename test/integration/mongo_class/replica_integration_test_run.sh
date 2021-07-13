#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mongo_class"  
test/integration/mongo_class/fetch_ismaster.py
test/integration/mongo_class/masterrep_connect.py
test/integration/mongo_class/masterrep_init.py
test/integration/mongo_class/repsetcoll_coll_cnt.py
test/integration/mongo_class/repsetcoll_coll_dst.py
test/integration/mongo_class/repsetcoll_coll_find.py
test/integration/mongo_class/repsetcoll_coll_find1.py
test/integration/mongo_class/repsetcoll_coll_options.py
test/integration/mongo_class/repsetcoll_connect.py
test/integration/mongo_class/repsetcoll_init.py
test/integration/mongo_class/repset_connect.py
test/integration/mongo_class/repset_init.py
test/integration/mongo_class/rep_fetch_nodes.py
test/integration/mongo_class/rep_init.py
test/integration/mongo_class/slaverep_connect.py
test/integration/mongo_class/slaverep_init.py

