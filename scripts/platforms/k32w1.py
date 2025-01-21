#!/usr/bin/env python3
#
#    Copyright 2024-2025 NXP
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
import os

from .utils.platform import COMMON_SDK
from .utils.platform import Platform
from .utils.tools import BlHost

# This assumes that the matter-vscode-for-mcux repo is cloned in Matter root path.
nbu_path = os.path.abspath(os.path.join(COMMON_SDK, "middleware/wireless/ieee-802.15.4/bin/k32w1_mcxw71/k32w1_mcxw71_nbu_ble_15_4_dyn_matter.sb3"))

class K32W1(Platform):

    def __init__(self, board=None):
        super().__init__()

        self.tool = BlHost()
        self.tool.add_action(["receive-sb-file", nbu_path])
        self.tool.add_action(["flash-erase-region", "0xf4000", "8192"])
        self.tool.add_action(["write-memory", "0xf4000", self.get_binary("example-factory-data.bin"), "8192"])
        self.tool.add_action(["reset"])

    def pre_message(self):
        print("Please place the board in ISP mode:")
        print(" - place jumper on JP25 pins 2-3")
        print(" - press and hold SW4, press and release Reset, then release SW4")
