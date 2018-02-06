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

import configparser


class Configuration(object):
    instance = None

    class __ConfigurationSingleton(object):
        def __init__(self, filename: str = "config.ini"):
            self.filename = filename
            self._config = configparser.ConfigParser()
            self._token = None
            self._init_config()

        def _init_config(self):
            self._config.read(self.filename)
            if "DEFAULT" not in self._config or "token" not in self._config["DEFAULT"]:
                raise NameError
            self._token = self._config["DEFAULT"]["token"]

        @property
        def token(self):
            return self._token

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = cls.__ConfigurationSingleton(**kwargs)
        else:
            if 'filename' in kwargs and cls.instance.filename != kwargs['filename']:
                cls.instance = cls.__ConfigurationSingleton(**kwargs)
        return cls.instance

    def __getattr__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        return setattr(self, key, value)
