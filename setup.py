#!/usr/bin/env python
#  Licensed to the Apache Software Foundation (ASF) under one
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

from setuptools import setup

setup(
    name="Zybot",
    packages=["zybot"],
    version="0.0.0",
    license="ASP",
    author="Marian Gappa",
    maintainer_email="sagarafr@gmail.com",
    description="A minimalist package for building Telegram bot",
    url="https://github.com/sagarafr/Zybot",
    keywords=["telegram-bot", "bot"],
    classifiers=[],
    install_requires=[
        'python-telegram-bot',
    ],
    entry_points='''
    [console_scripts]
    teletrack=zybot.bot:main
    ''',
)
