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

from sample.configuration import configuration
from sample.app import application


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hello world")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


if __name__ == '__main__':
    config = configuration.Configuration(filename="./config.ini")
    app = application.Application(token=config.token)
    app.add_command(function_name='start', callback=start)
    app.add_message(echo)
    app.run()
