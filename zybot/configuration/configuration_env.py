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
import os


class ConfigurationEnv(ConfigurationAbstract):
    """
    Implement ConfigurationAbstract. ConfigurationEnv permit to you to initialize the token with the env_name which is
    the environment variable to found in the environment. By default the value is TELEGRAM_TOKEN.
    """
    def __init__(self, env_name: str="TELEGRAM_TOKEN", **kwargs):
        """
        Initialize the configuration from the environment variable
        :param env_name: str is the environment variable to found
        :param kwargs:
        """
        super().__init__(env_name=env_name, **kwargs)

    def _init_token(self, env_name: str, **kwargs):
        token = os.getenv(env_name)
        if token is None:
            raise ValueError("The environment variable TELEGRAM_TOKEN is not created")
        self._token = token
