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
from ..configuration import configuration
from ..command import command

INLINE_HANDLER = "inline"
COMMAND_HANDLER = "command"


class Application(object):
    _instance = None

    class __Application(object):
        def __init__(self):
            config = configuration.Configuration()
            cmd = command.Command()
            self._updater = ext.Updater(token=config.token)
            self._dispatcher = self._updater.dispatcher

        def add_command(self, callback, function_name="", type_handler=None, group=ext.dispatcher.DEFAULT_GROUP):
            if type_handler is not None:
                if type_handler == COMMAND_HANDLER:
                    self._dispatcher.add_handler(handler=ext.CommandHandler(function_name, callback), group=group)
                elif type_handler == INLINE_HANDLER:
                    self._dispatcher.add_handler(handler=ext.InlineQueryHandler(callback), group=group)
            else:
                self._dispatcher.add_handler(handler=ext.CommandHandler(function_name, callback), group=group)

        def add_message(self, callback, filters=ext.Filters.text, group=ext.dispatcher.DEFAULT_GROUP):
            self._dispatcher.add_handler(ext.MessageHandler(filters, callback), group=group)

        def run(self):
            self._updater.start_polling()
            self.stop()

        def stop(self):
            self._updater.idle()
            self._updater.stop()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Application.__Application()
        return cls._instance
