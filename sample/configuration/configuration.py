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
import os
from os import path


class Configuration(object):
    _instance = None

    class __ConfigurationSingleton(object):
        def __init__(self, filename: str = None, token: str = None):
            self._config = configparser.ConfigParser()
            self._token = token
            if filename is not None:
                self._config.read(filename)
                self._init_token()

        @property
        def token(self):
            return self._token

        def _init_token(self):
            if self._token is None:
                self._token = self.get("token")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            filename = None
            token = None

            if 'filename' in kwargs:
                if kwargs['filename'] is not None and not path.isfile(kwargs['filename']):
                    print(kwargs['filename'] + " in argument doesn't exist")
                else:
                    filename = kwargs['filename']
            if 'token' in kwargs and kwargs['token'] is not None and kwargs['token'] != '':
                token = kwargs['token']

            if filename is None:
                filename = os.getenv('TELEGRAM_CONFIG_FILE')
                if filename is not None and not path.isfile(filename):
                    print(filename + " doesn't exist")
                    filename = None
            if token is None:
                token = os.getenv('TELEGRAM_TOKEN')
                if token == '':
                    token = None

            if token is None and filename is None:
                raise ValueError('token and filename value are invalid')

            cls._instance = cls.__ConfigurationSingleton(filename=filename, token=token)

        return cls._instance

    def __getattr__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        return setattr(self, key, value)
