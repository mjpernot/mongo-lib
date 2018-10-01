# Classification (U)

###############################################################################
#
# Program:      setup.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               None
#
###############################################################################

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

###############################################################################
# Libraries and Global Variables

# Standard
import os
import setuptools

# Third-party

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="Mongo_Lib",
    description="Mongodb class and libraries for connecting to MongoDB.",
    author="Mark Pernot",
    author_email="Mark.J.Pernot@coe.ic.gov",
    url="https://sc.appdev.proj.coe.ic.gov/JAC-DSXD/mongo-lib",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    py_modules=[
        "mongo_class",
        "mongo_libs",
        "__init__",
        "version"],

    classifiers=[
        # Common Values:
        #  2 - Pre-Alpha
        #  3 - Alpha
        #  4 - Beta
        #  5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Database",
        "Topic :: Database :: MongoDB :: 3.4.2"])
