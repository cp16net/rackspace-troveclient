#   Copyright 2014 Rackspace
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import setuptools


# troveclient_extensions = [
#     'rackspace-auth-openstack',                         # RAX-KSKEY
# ]


setuptools.setup(
    name='rackspace-troveclient',
    version='1.0',
    author='Rackspace',
    author_email='cp16net@gmail.com',
    description='Metapackage to install python-troveclient and Rackspace '
                'extensions',
    license='Apache License, Version 2.0',
    url='https://github.com/cp16net/rackspace-troveclient',
    install_requires=['python-troveclient'],  # + troveclient_extensions,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
