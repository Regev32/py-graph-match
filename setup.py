#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    my_project_template My Project Template.
#    Copyright (c) 2021 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
#


"""The setup script."""

import sys
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy


def build_include_dirs():
    platform = sys.platform
    if platform == "darwin":  # MacOS
        return [numpy.get_include(), "/usr/local/opt/libomp/include"]
    return [numpy.get_include()]


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().split("\n")

with open("requirements-tests.txt") as requirements_file:
    test_requirements = requirements_file.read().split("\n")

setup(
    name="py-graph-match-temp",
    version="0.0.9",
    author="Pradeep Bashyal",
    author_email="pbashyal@nmdp.org",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Graph Match",
    install_requires=requirements,
    license="LGPL 3.0",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="Graph,HLA",
    packages=find_packages(
        include=["grma", "grma.donorsgraph", "grma.match", "grma.utilities"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nmdp-bioinformatics/",
    zip_safe=False,
    include_dirs=build_include_dirs(),
    ext_modules=cythonize(
        [
            Extension(
                "grma.utilities.cutils",
                ["grma/utilities/cutils.pyx"],
                define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
            ),
            Extension(
                "grma.match.lol_graph",
                ["grma/match/lol_graph.pyx"],
                define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
            ),
        ]
    ),
)
