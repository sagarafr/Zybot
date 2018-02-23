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


import abc


class ConfigurationAbstract(object, metaclass=abc.ABCMeta):
    """
    ConfigurationAbstract is the abstraction of the configuration. The attribute token must be a string and the elements
    of the attribute _admins must be an integer
    """
    _token = None
    _admin_is_init = False
    _admins = []

    def __init__(self, **kwargs):
        """
        Initialize the ConfigurationAbstract
        :param kwargs:
        """
        if self._token is None:
            self._init_token(**kwargs)
        if not self._admin_is_init:
            self._admin_is_init = True
            self._init_admin(**kwargs)

    @property
    def token(self):
        """
        Return the token of your bot given by BotFather
        :return: str
        """
        return self._token

    @property
    def admins(self):
        return self._admins

    @abc.abstractmethod
    def _init_token(self, **kwargs):
        """
        Is a function that must be implemented to initialize the token value
        :param kwargs: All argument given to you to initialize
        :raise: NotImplementedError
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def _init_admin(self, **kwargs):
        """
        Is a function that muse be implemented to initialize the list of admin
        :param kwargs:
        :return:
        """
        raise NotImplemented()
