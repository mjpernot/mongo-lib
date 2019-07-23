#!/bin/bash
# Unit test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
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
 
