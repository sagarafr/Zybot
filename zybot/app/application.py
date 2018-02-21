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
from enum import Enum
import inspect


class HanderType(Enum):
    """
    HandlerType is the type of the functionality added to your bot.
    INLINE_HANDLER permit to you to create an inline command.
    COMMAND_HANDLER permit to you to create a basic command.
    MESSAGE_HANDLER permit to you to catch all message write in your channel.
    """
    INLINE_HANDLER = "inline"
    COMMAND_HANDLER = "command"
    MESSAGE_HANDLER = "message"


class Application(object):
    """
    Application is the central object. It's permit to you to add command, to run and to stop your bot. By default,
    the bot have the command help, which reference all your commands if there are documented in the docstring format.
    """
    _instance = None

    class __Application(object):
        def __init__(self):
            """
            Initialisation of the bot application. During the initialization, the construct will attempt to get and
            to connect to the Telegram API
            """
            config = configuration.Configuration()
            self._updater = ext.Updater(token=config.token)
            self._dispatcher = self._updater.dispatcher
            self._help_command = {}

        def handler(self, type_handler=HanderType.COMMAND_HANDLER, group=ext.dispatcher.DEFAULT_GROUP, filters=ext.Filters.text):
            """
            Decorator that add to the default dispatcher all kind of command
            :param type_handler: HandlerType is the type of your command
            :param group: group (:obj:`int`, optional): The group identifier. Default is 0.
            :param filters: Use for the MessageHandler
            :return: the function decorated
            """
            def decorator(callback):
                if type_handler.value == HanderType.COMMAND_HANDLER:
                    self._dispatcher.add_handler(handler=ext.CommandHandler(callback.__name__, callback), group=group)
                elif type_handler == HanderType.INLINE_HANDLER:
                    self._dispatcher.add_handler(handler=ext.InlineQueryHandler(callback), group=group)
                elif type_handler == HanderType.MESSAGE_HANDLER:
                    self._dispatcher.add_handler(handler=ext.MessageHandler(filters, callback), group=group)
                if isinstance(type_handler, HanderType):
                    self._help_command[callback.__name__] = inspect.cleandoc(inspect.getdoc(callback))
            return decorator

        def run(self):
            """
            Run your bot with all command added
            """
            self._dispatcher.add_handler(handler=ext.CommandHandler("help", self._help()), group=ext.dispatcher.DEFAULT_GROUP)
            self._updater.start_polling()
            self.stop()

        def _help(self):
            """
            Add the help command
            :return: the function decorated
            """
            def _help_command(bot, update):
                _help_str = "\n".join(["{}: {}".format(key, value) for key, value in self._help_command.items()])
                bot.send_message(chat_id=update.message.chat_id, text=_help_str)
            return _help_command

        def stop(self):
            """
            Stop your bot
            """
            self._updater.idle()
            self._updater.stop()

    def __new__(cls, *args, **kwargs):
        """
        Create an instance of __Application
        :param args: Not used
        :param kwargs: Not used
        :return: __Application instance
        """
        if cls._instance is None:
            cls._instance = Application.__Application()
        return cls._instance
