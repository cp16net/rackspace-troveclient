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


setuptools.setup(
    name='rackspace-troveclient',
    version='1.0',
    author='Rackspace',
    author_email='cp16net@gmail.com',
    description='Metapackage to install python-troveclient and Rackspace '
                'extensions',
    license='Apache License, Version 2.0',
    url='https://github.com/cp16net/rackspace-troveclient',
    install_requires=['python-troveclient'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points={
        "openstack.client.auth_url": [
            "rackspace_us = rackspace_auth_openstack.plugin:auth_url_us",
            "rackspace_uk = rackspace_auth_openstack.plugin:auth_url_uk",
            "rackspace = rackspace_auth_openstack.plugin:auth_url_us"
        ],
        "openstack.client.authenticate": [
            "rackspace_us = rackspace_auth_openstack.plugin:authenticate_us",
            "rackspace_uk = rackspace_auth_openstack.plugin:authenticate_uk",
            "rackspace = rackspace_auth_openstack.plugin:authenticate_us"
        ],
        "openstack.client.auth_plugin": [
            "rackspace = rackspace_auth_openstack.plugin:RackspaceAuthPlugin"
        ]
    }
)
