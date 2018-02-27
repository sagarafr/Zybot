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
from . import app
from os import path


def main():
    app_file = os.getenv("ZYBOT_APP")
    if app_file is None:
        raise EnvironmentError("Fail to get ZYBOT_APP environment variable")
    if not path.isfile(app_file):
        raise FileNotFoundError("Fail to get [{}] filename in the ZYBOT_APP environment variable".format(app_file))
    with open(app_file) as fd:
        exec(fd.read())
        application = app.Application()
        print("run")
        application.run()


if __name__ == '__main__':
    main()
