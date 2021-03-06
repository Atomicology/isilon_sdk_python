# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ClusterConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'devices': 'list[ClusterConfigDevice]',
            'encoding': 'str',
            'guid': 'str',
            'has_quorum': 'bool',
            'is_compliance': 'bool',
            'is_virtual': 'bool',
            'is_vonefs': 'bool',
            'join_mode': 'str',
            'local_devid': 'int',
            'local_lnn': 'int',
            'local_serial': 'str',
            'name': 'str',
            'onefs_version': 'ClusterConfigOnefsVersion',
            'timezone': 'ClusterConfigTimezone',
            'upgrade_type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'devices': 'devices',
            'encoding': 'encoding',
            'guid': 'guid',
            'has_quorum': 'has_quorum',
            'is_compliance': 'is_compliance',
            'is_virtual': 'is_virtual',
            'is_vonefs': 'is_vonefs',
            'join_mode': 'join_mode',
            'local_devid': 'local_devid',
            'local_lnn': 'local_lnn',
            'local_serial': 'local_serial',
            'name': 'name',
            'onefs_version': 'onefs_version',
            'timezone': 'timezone',
            'upgrade_type': 'upgrade_type'
        }

        self._description = None
        self._devices = None
        self._encoding = None
        self._guid = None
        self._has_quorum = None
        self._is_compliance = None
        self._is_virtual = None
        self._is_vonefs = None
        self._join_mode = None
        self._local_devid = None
        self._local_lnn = None
        self._local_serial = None
        self._name = None
        self._onefs_version = None
        self._timezone = None
        self._upgrade_type = None

    @property
    def description(self):
        """
        Gets the description of this ClusterConfig.
        Customer configurable description.

        :return: The description of this ClusterConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClusterConfig.
        Customer configurable description.

        :param description: The description of this ClusterConfig.
        :type: str
        """
        
        self._description = description

    @property
    def devices(self):
        """
        Gets the devices of this ClusterConfig.


        :return: The devices of this ClusterConfig.
        :rtype: list[ClusterConfigDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this ClusterConfig.


        :param devices: The devices of this ClusterConfig.
        :type: list[ClusterConfigDevice]
        """
        
        self._devices = devices

    @property
    def encoding(self):
        """
        Gets the encoding of this ClusterConfig.
        Default encoding.

        :return: The encoding of this ClusterConfig.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this ClusterConfig.
        Default encoding.

        :param encoding: The encoding of this ClusterConfig.
        :type: str
        """
        
        self._encoding = encoding

    @property
    def guid(self):
        """
        Gets the guid of this ClusterConfig.
        Cluster GUID.

        :return: The guid of this ClusterConfig.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this ClusterConfig.
        Cluster GUID.

        :param guid: The guid of this ClusterConfig.
        :type: str
        """
        
        self._guid = guid

    @property
    def has_quorum(self):
        """
        Gets the has_quorum of this ClusterConfig.
        If true, the local node is in a group with quorum: It is communicating, storing, and protecting data normally with other nodes in its group.  Under normal circumstances, every node in the cluster is part of one group.

        :return: The has_quorum of this ClusterConfig.
        :rtype: bool
        """
        return self._has_quorum

    @has_quorum.setter
    def has_quorum(self, has_quorum):
        """
        Sets the has_quorum of this ClusterConfig.
        If true, the local node is in a group with quorum: It is communicating, storing, and protecting data normally with other nodes in its group.  Under normal circumstances, every node in the cluster is part of one group.

        :param has_quorum: The has_quorum of this ClusterConfig.
        :type: bool
        """
        
        self._has_quorum = has_quorum

    @property
    def is_compliance(self):
        """
        Gets the is_compliance of this ClusterConfig.
        If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4.

        :return: The is_compliance of this ClusterConfig.
        :rtype: bool
        """
        return self._is_compliance

    @is_compliance.setter
    def is_compliance(self, is_compliance):
        """
        Sets the is_compliance of this ClusterConfig.
        If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4.

        :param is_compliance: The is_compliance of this ClusterConfig.
        :type: bool
        """
        
        self._is_compliance = is_compliance

    @property
    def is_virtual(self):
        """
        Gets the is_virtual of this ClusterConfig.
        true if the cluster is deployed on a desktop VMWorkstation

        :return: The is_virtual of this ClusterConfig.
        :rtype: bool
        """
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, is_virtual):
        """
        Sets the is_virtual of this ClusterConfig.
        true if the cluster is deployed on a desktop VMWorkstation

        :param is_virtual: The is_virtual of this ClusterConfig.
        :type: bool
        """
        
        self._is_virtual = is_virtual

    @property
    def is_vonefs(self):
        """
        Gets the is_vonefs of this ClusterConfig.
        true if this is a vOneFS cluster on an ESXi

        :return: The is_vonefs of this ClusterConfig.
        :rtype: bool
        """
        return self._is_vonefs

    @is_vonefs.setter
    def is_vonefs(self, is_vonefs):
        """
        Sets the is_vonefs of this ClusterConfig.
        true if this is a vOneFS cluster on an ESXi

        :param is_vonefs: The is_vonefs of this ClusterConfig.
        :type: bool
        """
        
        self._is_vonefs = is_vonefs

    @property
    def join_mode(self):
        """
        Gets the join_mode of this ClusterConfig.
        Node join mode: 'manual' or 'secure'.

        :return: The join_mode of this ClusterConfig.
        :rtype: str
        """
        return self._join_mode

    @join_mode.setter
    def join_mode(self, join_mode):
        """
        Sets the join_mode of this ClusterConfig.
        Node join mode: 'manual' or 'secure'.

        :param join_mode: The join_mode of this ClusterConfig.
        :type: str
        """
        
        self._join_mode = join_mode

    @property
    def local_devid(self):
        """
        Gets the local_devid of this ClusterConfig.
        Device ID of the queried node.

        :return: The local_devid of this ClusterConfig.
        :rtype: int
        """
        return self._local_devid

    @local_devid.setter
    def local_devid(self, local_devid):
        """
        Sets the local_devid of this ClusterConfig.
        Device ID of the queried node.

        :param local_devid: The local_devid of this ClusterConfig.
        :type: int
        """
        
        self._local_devid = local_devid

    @property
    def local_lnn(self):
        """
        Gets the local_lnn of this ClusterConfig.
        Device logical node number of the queried node.

        :return: The local_lnn of this ClusterConfig.
        :rtype: int
        """
        return self._local_lnn

    @local_lnn.setter
    def local_lnn(self, local_lnn):
        """
        Sets the local_lnn of this ClusterConfig.
        Device logical node number of the queried node.

        :param local_lnn: The local_lnn of this ClusterConfig.
        :type: int
        """
        
        self._local_lnn = local_lnn

    @property
    def local_serial(self):
        """
        Gets the local_serial of this ClusterConfig.
        Device serial number of the queried node.

        :return: The local_serial of this ClusterConfig.
        :rtype: str
        """
        return self._local_serial

    @local_serial.setter
    def local_serial(self, local_serial):
        """
        Sets the local_serial of this ClusterConfig.
        Device serial number of the queried node.

        :param local_serial: The local_serial of this ClusterConfig.
        :type: str
        """
        
        self._local_serial = local_serial

    @property
    def name(self):
        """
        Gets the name of this ClusterConfig.
        Cluster name.

        :return: The name of this ClusterConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClusterConfig.
        Cluster name.

        :param name: The name of this ClusterConfig.
        :type: str
        """
        
        self._name = name

    @property
    def onefs_version(self):
        """
        Gets the onefs_version of this ClusterConfig.
        

        :return: The onefs_version of this ClusterConfig.
        :rtype: ClusterConfigOnefsVersion
        """
        return self._onefs_version

    @onefs_version.setter
    def onefs_version(self, onefs_version):
        """
        Sets the onefs_version of this ClusterConfig.
        

        :param onefs_version: The onefs_version of this ClusterConfig.
        :type: ClusterConfigOnefsVersion
        """
        
        self._onefs_version = onefs_version

    @property
    def timezone(self):
        """
        Gets the timezone of this ClusterConfig.
        The cluster timezone settings.

        :return: The timezone of this ClusterConfig.
        :rtype: ClusterConfigTimezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ClusterConfig.
        The cluster timezone settings.

        :param timezone: The timezone of this ClusterConfig.
        :type: ClusterConfigTimezone
        """
        
        self._timezone = timezone

    @property
    def upgrade_type(self):
        """
        Gets the upgrade_type of this ClusterConfig.


        :return: The upgrade_type of this ClusterConfig.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """
        Sets the upgrade_type of this ClusterConfig.


        :param upgrade_type: The upgrade_type of this ClusterConfig.
        :type: str
        """
        allowed_values = ["rolling", "simultaneous", "assessment"]
        if upgrade_type is not None and upgrade_type not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._upgrade_type = upgrade_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

