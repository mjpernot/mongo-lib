#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mongo_class"  
test/unit/mongo_libs/create_cmd.py
test/unit/mongo_libs/create_instance.py
test/unit/mongo_libs/create_slv_array.py
test/unit/mongo_libs/crt_base_cmd.py
test/unit/mongo_libs/crt_coll_inst.py
test/unit/mongo_libs/disconnect.py
test/unit/mongo_libs/ins_doc.py

