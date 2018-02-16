# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

from .abstract_configuration import ConfigurationAbstract


class Configuration(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            if 'ctor' not in kwargs:
                raise ValueError("Have not ctor variable")
            if not issubclass(kwargs['ctor'], ConfigurationAbstract):
                raise ValueError("Have not the right inheritance")
            ctor = kwargs['ctor']
            cls._instance = ctor(**kwargs)

        return cls._instance

    def __getattr__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        return setattr(self, key, value)
