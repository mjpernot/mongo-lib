# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md", "r", encoding="UTF-8")) as f_hdlr:
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
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Linux",
        "Operating System :: Linux :: Redhat",
        "Operating System :: Linux :: Redhat :: 8",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: Linux :: RedHat :: 9",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Linux :: Fedora",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database",
        "Topic :: Database :: Mongodb :: 3.4",
        "Topic :: Database :: Mongodb :: 4.2"])
