#!/usr/bin/env python3
#
#    Copyright 2025 NXP
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
nbu_path = os.path.abspath(os.path.join(COMMON_SDK, "middleware/wireless/ieee-802.15.4/bin/mcxw72/mcxw72_nbu_ble_15_4_dyn.bin"))

class MCXW72(Platform):

    def __init__(self, board=None):
        super().__init__()

        factory_data_len = str(os.path.getsize(self.get_binary("example-factory-data.bin")))

        self.tool = BlHost()
        self.tool.add_action(["write-memory", "0x48800000", nbu_path])
        self.tool.add_action(["flash-erase-region", "0x2002680", factory_data_len])
        self.tool.add_action(["write-memory", "0x2002680", self.get_binary("example-factory-data.bin"), factory_data_len])
        self.tool.add_action(["reset"])

    def pre_message(self):
        print("Please place the board in ISP mode:")
        print(" - press and hold SW4 (BOOT_CONFIG)")
        print(" - press and release SW1 (RST)")
        print(" - release SW4")
