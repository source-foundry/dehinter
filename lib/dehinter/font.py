# Copyright 2019 Source Foundry Authors and Contributors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def is_truetype_font(filepath):
    """Confirms has the TrueType file signature of either:
         1) b'\x00\x01\x00\x00'
         2) b'\x74\x72\x75\x65' == 'true'"""
    with open(filepath, 'rb') as f:
        file_signature = f.read(4)

        return file_signature in (b'\x00\x01\x00\x00', b'\x74\x72\x75\x65')
