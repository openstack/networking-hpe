# Copyright (c) 2015 Hewlett-Packard Enterprise Development, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""bm network provisioning
Revision ID: 9f1c0061fd83
Revises: start_networking_hpe
Create Date: 2015-07-06 00:25:06.980102
"""

# revision identifiers, used by Alembic.
revision = '9f1c0061fd83'
down_revision = 'start_networking_hpe'

from neutron.db import migration
from neutron.db.migration import cli


def upgrade():
    pass
