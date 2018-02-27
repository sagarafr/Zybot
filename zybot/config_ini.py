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

from . import config
import configparser
from os import path


class ConfigurationIni(config.ConfigurationAbstract):
    """
    Implement ConfigurationAbstract. ConfigurationIni permit to you to initialize the token and the admin with a file
    with the ini format. The key for the token is token. The key for the admin is admin, with ',' for separator
    """
    def __init__(self, filename: str, **kwargs):
        """
        Initialize the Configuration from a filename at the ini format
        :param filename: str content the name of the filename
        :param kwargs:
        """
        self._config = configparser.ConfigParser()
        if not path.isfile(filename):
            raise FileNotFoundError("Fail to found the filename [{}] given in argument".format(filename))
        self._config.read(filename)
        super().__init__(**kwargs)

    def _get_element(self, option: str, session: str="DEFAULT"):
        if session not in self._config:
            raise KeyError("Fail to found the [{}] section in the configuration".format(session))
        if option not in self._config[session]:
            raise KeyError("Fail to found the [{}] option at the [{}] "
                           "section in the configuration".format(session, option))
        return self._config[session][option]

    def _init_token(self, **kwargs):
        self._token = self._get_element(option='token')

    def _init_admin(self, **kwargs):
        for admin in self._get_element(option='admin').split(','):
            tmp = str(admin).strip()
            if tmp != '' and tmp.isdigit():
                self._admins.append(int(tmp))

    @property
    def config(self):
        """
        Get the config
        :return: configparser.ConfigParser
        """
        return self._config

    def get(self, option: str, session: str = "DEFAULT"):
        """
        Get in the configuration the option at the session asked. If it does'nt exist then return None
        :param option:
        :param session:
        :return:
        """
        try:
            return self._get_element(option=option, session=session)
        except KeyError:
            return None
