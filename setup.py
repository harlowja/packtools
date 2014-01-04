#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright (C) 2013 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from setuptools import setup


def _path(fn):
    return os.path.join(os.path.dirname(__file__), fn)


setup(name='packtools',
      version='0.0.1',
      description='Packaging toolbelt',
      author="OpenStack Foundation",
      author_email='openstack-dev@lists.openstack.org',
      url='https://github.com/harlowja/packtools/',
      scripts=[
          _path(os.path.join('scripts', 'multipip')),
          _path(os.path.join('scripts', 'pip-download')),
          _path(os.path.join('scripts', 'py2rpm')),
          _path(os.path.join('scripts', 'specprint')),
          _path(os.path.join('scripts', 'yyoom')),
      ],
      install_requires=[
          'argparse',
          'pip>=1.3',
          'six>=1.4.1',
      ],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
      ],
      keywords="packaging rpm pip yum specfile",
     )
