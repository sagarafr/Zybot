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
import configparser
from os import path


class ConfigurationIni(ConfigurationAbstract):
    """
    Implement ConfigurationAbstract. ConfigurationIni permit to you to initialize the token with a ini file.
    """
    def __init__(self, filename: str, **kwargs):
        """
        Initialize the Configuration from a filename at the ini format
        :param filename: str content the name of the filename
        :param kwargs:
        """
        self._config = configparser.ConfigParser()
        super().__init__(filename=filename, **kwargs)

    def _init_token(self, filename, **kwargs):
        if not path.isfile(filename):
            raise ValueError("Filename doesn't exist")
        try:
            self._config.read(filename)
        except FileNotFoundError as err:
            raise ValueError(err) from err
        if 'DEFAULT' not in self._config:
            raise ValueError("In the ini configuration file there are not a DEFAULT section")
        if 'token' not in self._config['DEFAULT']:
            raise ValueError("In the ini configuration file there are not a token option in the DEFAULT section")
        self._token = self._config['DEFAULT']['token']

    @property
    def config(self):
        """
        Get the config
        :return: configparser.ConfigParser
        """
        return self._config

    def get(self, option: str, session: str = "DEFAULT"):
        return self._config.get(session, option=option)
