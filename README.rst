README
======

A basic Telegram starter to avoid some repetitions and rewrite on python using python-telegram-bot API

Usage
-----

A Simple Example
----------------

Add your token given by the Bot Father in the config.ini file

.. code-block:: python

    from zybot import (config_ini, config)
    from zybot import app

    configuration = config.Configuration(ctor=config_ini.ConfigurationIni, filename="./config.ini")
    application = app.Application()


    @application.command()
    def start(bot, update):
        """
        Say to you 'hello world'
        """
        bot.send_message(chat_id=update.message.chat_id, text="hello world")

    @application.command()
    @application.restricted
    def protected(bot, update):
        """
        Say to you 'hello admin'
        """
        bot.send_message(chat_id=update.message.chat_id, text="hello admin")

.. code-block:: ini

    [DEFAULT]
    token = token_given_by_the_bot_father
    # separator ,
    admin = id_given_by_user_info_bot

.. code-block:: none

    $ ZYBOT_APP="hello.py" python3 -m zybot zybot
