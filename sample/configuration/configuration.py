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
    _instance = None

    class __ConfigurationSingleton(object):
        def __init__(self, filename: str = "config.ini"):
            self.filename = filename
            self._config = configparser.ConfigParser()
            self._config.read(self.filename)
            self._token = self._config["DEFAULT"]["token"]
            self._section = None

        @property
        def token(self):
            return self._token

        def __getattr__(self, item):
            if self._config.has_option(section="DEFAULT", option=item):
                return self._config["DEFAULT"][item]
            return None

        def get(self, option: str, session: str = "DEFAULT"):
            return self._config.get(session, option=option)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.__ConfigurationSingleton(**kwargs)
        else:
            if 'filename' in kwargs and cls._instance.filename != kwargs['filename']:
                cls._instance = cls.__ConfigurationSingleton(**kwargs)
        return cls._instance

    def __getattr__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        return setattr(self, key, value)
