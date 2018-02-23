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
from functools import wraps


class Application(object):
    """
    Application is the central object. It's permit to you to add command, to run and to stop your bot. By default,
    the bot have the command help, which reference all your commands if there are documented in the docstring format,
    and the unknown message if the command doesn't exist.
    """
    _instance = None

    class __Application(object):
        def __init__(self):
            """
            Initialisation of the bot application. During the initialization, the construct will attempt to get and
            to connect to the Telegram API
            """
            self._config = configuration.Configuration()
            self._updater = ext.Updater(token=self._config.token)
            self._dispatcher = self._updater.dispatcher
            self._help_command = {}
            self._admin_command = {}
            self._help_cmd_str = ""
            self._help_admin_cmd_str = ""

        def command(self, cmd_name: str="", group: int=ext.dispatcher.DEFAULT_GROUP, filters: ext.Filters=None,
                    allow_edited: bool=False, pass_args: bool=False, pass_update_queue: bool=False,
                    pass_job_queue: bool=False, pass_user_data: bool=False, pass_chat_data: bool=False):
            """
            Create an CommandHandler and add it to the main dispatcher
            :param cmd_name:
            :param group:
            :param filters:
            :param allow_edited:
            :param pass_args:
            :param pass_update_queue:
            :param pass_job_queue:
            :param pass_user_data:
            :param pass_chat_data:
            :return:
            """
            def decorator(callback):
                name = cmd_name
                if name == "":
                    name = callback.__name__
                self._dispatcher.add_handler(handler=ext.CommandHandler(command=name, callback=callback,
                                                                        filters=filters, allow_edited=allow_edited,
                                                                        pass_args=pass_args,
                                                                        pass_update_queue=pass_update_queue,
                                                                        pass_job_queue=pass_job_queue,
                                                                        pass_user_data=pass_user_data,
                                                                        pass_chat_data=pass_chat_data), group=group)

                if callback.__name__ in self._admin_command.keys():
                    del self._admin_command[callback.__name__]
                    self._admin_command[callback] = name
                else:
                    self._help_command[callback] = name
            return decorator

        def restricted(self, callback):
            """
            Restrict the usage of callback
            :param callback:
            :return:
            """

            self._admin_command[callback.__name__] = None

            @wraps(callback)
            def wrapped(bot, update, *args, **kwargs):

                user_id = update.effective_user.id
                # TODO see to use bot.get_chat_administrators function
                if user_id not in self._config.admins:
                    self._unknown_command(bot, update)
                    print("Unauthorized access denied for {}.".format(user_id))
                    return
                return callback(bot, update, *args, **kwargs)
            return wrapped

        def inline(self, group: int=ext.dispatcher.DEFAULT_GROUP, pass_update_queue: bool=False,
                   pass_job_queue: bool=False, pattern=None, pass_groups: bool=False, pass_groupdict: bool=False,
                   pass_user_data: bool=False, pass_chat_data: bool=False):
            """
            Create an InlineQueryHandler and add it to the main dispatcher
            :param group:
            :param pass_update_queue:
            :param pass_job_queue:
            :param pattern:
            :param pass_groups:
            :param pass_groupdict:
            :param pass_user_data:
            :param pass_chat_data:
            :return:
            """
            def decorator(callback):
                self._dispatcher.add_handler(handler=ext.InlineQueryHandler(callback=callback,
                                                                            pass_update_queue=pass_update_queue,
                                                                            pass_job_queue=pass_job_queue,
                                                                            pattern=pattern, pass_groups=pass_groups,
                                                                            pass_groupdict=pass_groupdict,
                                                                            pass_user_data=pass_user_data,
                                                                            pass_chat_data=pass_chat_data), group=group)
            return decorator

        def message(self, filters: ext.Filters=ext.Filters.text, group: int=ext.dispatcher.DEFAULT_GROUP,
                    allow_edited: bool=False, pass_update_queue: bool=False, pass_job_queue: bool=False,
                    pass_user_data: bool=False, pass_chat_data: bool=False, message_updates: bool=True,
                    channel_post_updates: bool=True, edited_updates: bool=False):
            """
            Create a MessageHandler and add it to the main dispatcher
            :param filters:
            :param group:
            :param allow_edited:
            :param pass_update_queue:
            :param pass_job_queue:
            :param pass_user_data:
            :param pass_chat_data:
            :param message_updates:
            :param channel_post_updates:
            :param edited_updates:
            :return:
            """
            def decorator(callback):
                self._dispatcher.add_handler(handler=ext.MessageHandler(filters=filters, callback=callback,
                                                                        allow_edited=allow_edited,
                                                                        pass_update_queue=pass_update_queue,
                                                                        pass_job_queue=pass_job_queue,
                                                                        pass_user_data=pass_user_data,
                                                                        pass_chat_data=pass_chat_data,
                                                                        message_updates=message_updates,
                                                                        channel_post_updates=channel_post_updates,
                                                                        edited_updates=edited_updates), group=group)
            return decorator

        def run(self):
            """
            Run your bot with all command added
            """
            self._generate_help()
            self._dispatcher.add_handler(handler=ext.CommandHandler("help", self._help()),
                                         group=ext.dispatcher.DEFAULT_GROUP)
            self._dispatcher.add_handler(handler=ext.MessageHandler(ext.Filters.command, self._unknown_command),
                                         group=ext.dispatcher.DEFAULT_GROUP)
            self._updater.start_polling()
            self.stop()

        @staticmethod
        def _unknown_command(bot, update):
            bot.send_message(chat_id=update.message.chat_id, text="Sorry I don't understant your request")

        def _generate_help(self):
            self._help_cmd_str = "\n".join(["{}: {}".format(cmd, inspect.cleandoc(inspect.getdoc(callback)))
                                            for callback, cmd in self._help_command.items()])
            self._help_admin_cmd_str = "\n".join(["{}: {}".format(cmd, inspect.cleandoc(inspect.getdoc(callback)))
                                                  for callback, cmd in self._admin_command.items()])

        def _help(self):
            """
            Add the help command
            :return: the function decorated
            """
            def _help_command(bot, update):
                help_str = self._help_cmd_str

                # TODO see to use bot.get_chat_administrators function
                if update.effective_user.id in self._config.admins:
                    help_str += "\n" + self._help_admin_cmd_str
                bot.send_message(chat_id=update.message.chat_id, text=help_str)
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
