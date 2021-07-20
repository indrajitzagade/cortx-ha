# Copyright (c) 2021 Seagate Technology LLC and/or its Affiliates
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along
# with this program. If not, see <https://www.gnu.org/licenses/>. For any questions
# about this software or licensing, please email opensource@seagate.com or
# cortx-questions@seagate.com.

ACTION_EVENT_VERSION = "2.0"
HA_MESSAGE_BUS_ADMIN = "ha_admin"
EVENT_MGR_PRODUCER_ID = "ha_event_manager_<component_id>"
EVENT_MGR_MESSAGE_TYPE = "ha_event_<component_id>"
EVENT_MGR_MESSAGE_TYPE_KEY = "message_type/<component_id>"
EVENT_MGR_PRODUCER_METHOD = "sync"
EVENT_COMPONENT_LIST = "events/<event_name>"