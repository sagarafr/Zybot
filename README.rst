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
    from zybot.app import application

    config = Configuration(ctor=ConfigurationIni, filename="./config.ini")
    app = application.Application()


    @app.handler()
    def start(bot, update):
        """
        Say to you 'hello world'
        """
        bot.send_message(chat_id=update.message.chat_id, text="hello world")

.. code-block:: none

    $ ZYBOT_APP="hello.py" python3 -m zybot zybot
