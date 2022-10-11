#!/bin/bash
# Integration testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Integration test: mongo_libs"
/usr/bin/python3 ./test/integration/mongo_libs/add_ssl_cmd.py
/usr/bin/python3 ./test/integration/mongo_libs/create_cmd.py
/usr/bin/python3 ./test/integration/mongo_libs/create_instance.py
/usr/bin/python3 ./test/integration/mongo_libs/crt_base_cmd.py
/usr/bin/python3 ./test/integration/mongo_libs/crt_coll_inst.py
/usr/bin/python3 ./test/integration/mongo_libs/disconnect.py

