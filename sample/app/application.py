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

from telegram import ext


class Application(object):
    _instance = None

    class __Application(object):
        def __init__(self, token: str):
            self._updater = ext.Updater(token=token)
            self._dispatcher = self._updater.dispatcher

        def add_command(self, function_name, callback, group=ext.dispatcher.DEFAULT_GROUP):
            self._dispatcher.add_handler(handler=ext.CommandHandler(function_name, callback), group=group)

        def add_message(self, callback, filters=ext.Filters.text, group=ext.dispatcher.DEFAULT_GROUP):
            self._dispatcher.add_handler(ext.MessageHandler(filters, callback), group=group)

        def run(self):
            self._updater.start_polling()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Application.__Application(**kwargs)
        return cls._instance
