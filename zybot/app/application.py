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
import inspect

INLINE_HANDLER = "inline"
COMMAND_HANDLER = "command"
MESSAGE_HANDLER = "message"


class Application(object):
    _instance = None

    class __Application(object):
        def __init__(self):
            config = configuration.Configuration()
            self._updater = ext.Updater(token=config.token)
            self._dispatcher = self._updater.dispatcher
            self._help_command = {}

        def handler(self, type_handler=COMMAND_HANDLER, group=ext.dispatcher.DEFAULT_GROUP, filters=ext.Filters.text):
            def decorator(callback):
                if type_handler == COMMAND_HANDLER:
                    self._dispatcher.add_handler(handler=ext.CommandHandler(callback.__name__, callback), group=group)
                elif type_handler == INLINE_HANDLER:
                    self._dispatcher.add_handler(handler=ext.InlineQueryHandler(callback), group=group)
                elif type_handler == MESSAGE_HANDLER:
                    self._dispatcher.add_handler(handler=ext.MessageHandler(filters, callback), group=ext.dispatcher.DEFAULT_GROUP)
                if type_handler in [COMMAND_HANDLER, INLINE_HANDLER, MESSAGE_HANDLER]:
                    self._help_command[callback.__name__] = inspect.cleandoc(inspect.getdoc(callback))
            return decorator

        def run(self):
            self._dispatcher.add_handler(handler=ext.CommandHandler("help", self._help()), group=ext.dispatcher.DEFAULT_GROUP)
            self._updater.start_polling()
            self.stop()

        def _help(self):
            def _help_command(bot, update):
                _help_str = "\n".join(["{}: {}".format(key, value) for key, value in self._help_command.items()])
                bot.send_message(chat_id=update.message.chat_id, text=_help_str)
            return _help_command

        def stop(self):
            self._updater.idle()
            self._updater.stop()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Application.__Application()
        return cls._instance
