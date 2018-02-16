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

import telegram.ext
from zybot.app import application
from zybot.configuration import configuration
from zybot.configuration import configuration_ini


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hello world")


def caps(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=str(update.message.text).upper())


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = [telegram.InlineQueryResultArticle(
        id=query.upper(),
        title="Caps",
        input_message_content=telegram.InputTextMessageContent(query.upper())
    )]
    bot.answer_inline_query(update.inline_query.id, results)


def unknown(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text="Sorry I don't understand your request")


if __name__ == '__main__':
    configuration.Configuration(ctor=configuration_ini.ConfigurationIni, filename="./config.ini")
    app = application.Application()
    app.add_command(function_name='start', callback=start)
    app.add_command(callback=inline_caps, type_handler=application.INLINE_HANDLER)
    app.add_message(echo)
    app.add_message(callback=unknown, filters=telegram.ext.Filters.command)
    print("run")
    app.run()
