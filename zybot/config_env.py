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
import os


class ConfigurationEnv(config.ConfigurationAbstract):
    """
    Implement ConfigurationAbstract. ConfigurationEnv permit to you to initialize the token and the admins list with
    the env_token and env_admin which is the environment variable to found in the environment.
    By default the env_token is TELEGRAM_TOKEN and the env_admin is TELEGRAM_ADMINS.
    """
    def __init__(self, env_token: str="TELEGRAM_TOKEN", env_admin: str="TELEGRAM_ADMINS", **kwargs):
        """
        Initialize the configuration from the environment variable
        :param env_name: str is the environment variable to found
        :param kwargs:
        """
        if os.getenv(env_token) is None:
            raise EnvironmentError("The environment variable TELEGRAM_TOKEN is not created")
        super().__init__(env_token=env_token, env_admin=env_admin, **kwargs)

    def _init_token(self, env_token: str, **kwargs):
        token = os.getenv(env_token)
        if token is None:
            raise EnvironmentError("The environment variable TELEGRAM_TOKEN is not created")
        self._token = token

    def _init_admin(self, env_admin: str, **kwargs):
        admins = os.getenv(env_admin)
        for admin in admins.split(os.pathsep):
            tmp = str(admin).strip()
            if tmp != '' and tmp.isdigit():
                self._admins.append(int(tmp))
