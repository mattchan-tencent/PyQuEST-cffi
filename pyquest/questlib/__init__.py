# Copyright 2019 HQS Quantum Simulations GmbH
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Requires LD_LIBRARY_PATH=path/to/this/dir to run
import os
lib_path = os.path.dirname(os.path.realpath(__file__))
os.environ['LD_LIBRARY_PATH'] = lib_path
from pyquest.questlib._abstract import _PYQUEST, tquestenv, tqureg
from ._quest import lib as quest
from ._quest import ffi as ffi_quest