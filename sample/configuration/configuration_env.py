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

from .abstract_configuration import *
import os


class ConfigurationEnv(ConfigurationAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_token(self, **kwargs):
        token = os.getenv('TELEGRAM_TOKEN')
        if token is None:
            raise ValueError("The environment variable TELEGRAM_TOKEN is not created")
        self._token = token
