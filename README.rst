README
======

A basic Telegram starter to avoid some repetitions and rewrite on python using python-telegram-bot API

Usage
-----

A Simple Example
----------------

Add your token given by the Bot Father in the config.ini file

.. code-block:: python

from zybot.configuration import ConfigurationIni, Configuration
from zybot.app import Application


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hello world")


config = Configuration(ctor=ConfigurationIni, filename="./config.ini")
app = Application()
app.add_command(function_name='start', callback=start)

.. code-block:: none

 $ ZYBOT_APP="hello.py" python3 -m zybot zybot
