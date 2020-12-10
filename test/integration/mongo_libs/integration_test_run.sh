#!/bin/bash
# Integration testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Integration test: mongo_libs"  
test/integration/mongo_libs/create_cmd.py
test/integration/mongo_libs/create_instance.py
test/integration/mongo_libs/crt_base_cmd.py
test/integration/mongo_libs/crt_coll_inst.py
test/integration/mongo_libs/disconnect.py

