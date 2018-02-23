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

import os
from .app import application
from os import path


def main():
    app = os.getenv("ZYBOT_APP")
    if app is None:
        raise EnvironmentError("Fail to get ZYBOT_APP environment variable")
    if path.isfile(app):
        raise FileNotFoundError("Fail to get [{}] filename in the ZYBOT_APP environment variable".format(app))
    with open(app) as fd:
        exec(fd.read())
        app = application.Application()
        print("run")
        app.run()


if __name__ == '__main__':
    main()
