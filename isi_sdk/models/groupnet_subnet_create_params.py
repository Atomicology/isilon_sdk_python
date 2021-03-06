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


class GroupnetSubnetCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GroupnetSubnetCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'dsr_addrs': 'list[str]',
            'gateway': 'str',
            'gateway_priority': 'int',
            'mtu': 'int',
            'name': 'str',
            'prefixlen': 'int',
            'sc_service_addr': 'str',
            'vlan_enabled': 'bool',
            'vlan_id': 'int',
            'addr_family': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'dsr_addrs': 'dsr_addrs',
            'gateway': 'gateway',
            'gateway_priority': 'gateway_priority',
            'mtu': 'mtu',
            'name': 'name',
            'prefixlen': 'prefixlen',
            'sc_service_addr': 'sc_service_addr',
            'vlan_enabled': 'vlan_enabled',
            'vlan_id': 'vlan_id',
            'addr_family': 'addr_family'
        }

        self._description = None
        self._dsr_addrs = None
        self._gateway = None
        self._gateway_priority = None
        self._mtu = None
        self._name = None
        self._prefixlen = None
        self._sc_service_addr = None
        self._vlan_enabled = None
        self._vlan_id = None
        self._addr_family = None

    @property
    def description(self):
        """
        Gets the description of this GroupnetSubnetCreateParams.
        A description of the subnet.

        :return: The description of this GroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupnetSubnetCreateParams.
        A description of the subnet.

        :param description: The description of this GroupnetSubnetCreateParams.
        :type: str
        """
        
        if description is not None and len(description) > 128: 
            raise ValueError("Invalid value for `description`, length must be less than `128`")

        self._description = description

    @property
    def dsr_addrs(self):
        """
        Gets the dsr_addrs of this GroupnetSubnetCreateParams.
        List of Direct Server Return addresses.

        :return: The dsr_addrs of this GroupnetSubnetCreateParams.
        :rtype: list[str]
        """
        return self._dsr_addrs

    @dsr_addrs.setter
    def dsr_addrs(self, dsr_addrs):
        """
        Sets the dsr_addrs of this GroupnetSubnetCreateParams.
        List of Direct Server Return addresses.

        :param dsr_addrs: The dsr_addrs of this GroupnetSubnetCreateParams.
        :type: list[str]
        """
        
        self._dsr_addrs = dsr_addrs

    @property
    def gateway(self):
        """
        Gets the gateway of this GroupnetSubnetCreateParams.
        Gateway IP address.

        :return: The gateway of this GroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this GroupnetSubnetCreateParams.
        Gateway IP address.

        :param gateway: The gateway of this GroupnetSubnetCreateParams.
        :type: str
        """
        
        self._gateway = gateway

    @property
    def gateway_priority(self):
        """
        Gets the gateway_priority of this GroupnetSubnetCreateParams.
        Gateway priority.

        :return: The gateway_priority of this GroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._gateway_priority

    @gateway_priority.setter
    def gateway_priority(self, gateway_priority):
        """
        Sets the gateway_priority of this GroupnetSubnetCreateParams.
        Gateway priority.

        :param gateway_priority: The gateway_priority of this GroupnetSubnetCreateParams.
        :type: int
        """
        
        if gateway_priority is not None  and gateway_priority > 2.147483647E9:
            raise ValueError("Invalid value for `gateway_priority`, must be a value less than or equal to `2.147483647E9`")
        if gateway_priority is not None and gateway_priority < 1.0:
            raise ValueError("Invalid value for `gateway_priority`, must be a value greater than or equal to `1.0`")

        self._gateway_priority = gateway_priority

    @property
    def mtu(self):
        """
        Gets the mtu of this GroupnetSubnetCreateParams.
        MTU of the subnet.

        :return: The mtu of this GroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """
        Sets the mtu of this GroupnetSubnetCreateParams.
        MTU of the subnet.

        :param mtu: The mtu of this GroupnetSubnetCreateParams.
        :type: int
        """
        
        if mtu is not None  and mtu > 9000.0:
            raise ValueError("Invalid value for `mtu`, must be a value less than or equal to `9000.0`")
        if mtu is not None and mtu < 576.0:
            raise ValueError("Invalid value for `mtu`, must be a value greater than or equal to `576.0`")

        self._mtu = mtu

    @property
    def name(self):
        """
        Gets the name of this GroupnetSubnetCreateParams.
        The name of the subnet.

        :return: The name of this GroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupnetSubnetCreateParams.
        The name of the subnet.

        :param name: The name of this GroupnetSubnetCreateParams.
        :type: str
        """
        
        if name is not None and len(name) > 32: 
            raise ValueError("Invalid value for `name`, length must be less than `32`")

        self._name = name

    @property
    def prefixlen(self):
        """
        Gets the prefixlen of this GroupnetSubnetCreateParams.
        Subnet Prefix Length.

        :return: The prefixlen of this GroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """
        Sets the prefixlen of this GroupnetSubnetCreateParams.
        Subnet Prefix Length.

        :param prefixlen: The prefixlen of this GroupnetSubnetCreateParams.
        :type: int
        """
        
        if prefixlen is not None  and prefixlen > 128.0:
            raise ValueError("Invalid value for `prefixlen`, must be a value less than or equal to `128.0`")
        if prefixlen is not None and prefixlen < 1.0:
            raise ValueError("Invalid value for `prefixlen`, must be a value greater than or equal to `1.0`")

        self._prefixlen = prefixlen

    @property
    def sc_service_addr(self):
        """
        Gets the sc_service_addr of this GroupnetSubnetCreateParams.
        The address that SmartConnect listens for DNS requests.

        :return: The sc_service_addr of this GroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._sc_service_addr

    @sc_service_addr.setter
    def sc_service_addr(self, sc_service_addr):
        """
        Sets the sc_service_addr of this GroupnetSubnetCreateParams.
        The address that SmartConnect listens for DNS requests.

        :param sc_service_addr: The sc_service_addr of this GroupnetSubnetCreateParams.
        :type: str
        """
        
        self._sc_service_addr = sc_service_addr

    @property
    def vlan_enabled(self):
        """
        Gets the vlan_enabled of this GroupnetSubnetCreateParams.
        VLAN tagging enabled or disabled.

        :return: The vlan_enabled of this GroupnetSubnetCreateParams.
        :rtype: bool
        """
        return self._vlan_enabled

    @vlan_enabled.setter
    def vlan_enabled(self, vlan_enabled):
        """
        Sets the vlan_enabled of this GroupnetSubnetCreateParams.
        VLAN tagging enabled or disabled.

        :param vlan_enabled: The vlan_enabled of this GroupnetSubnetCreateParams.
        :type: bool
        """
        
        self._vlan_enabled = vlan_enabled

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this GroupnetSubnetCreateParams.
        VLAN ID for all interfaces in the subnet.

        :return: The vlan_id of this GroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this GroupnetSubnetCreateParams.
        VLAN ID for all interfaces in the subnet.

        :param vlan_id: The vlan_id of this GroupnetSubnetCreateParams.
        :type: int
        """
        
        if vlan_id is not None  and vlan_id > 4094.0:
            raise ValueError("Invalid value for `vlan_id`, must be a value less than or equal to `4094.0`")
        if vlan_id is not None and vlan_id < 2.0:
            raise ValueError("Invalid value for `vlan_id`, must be a value greater than or equal to `2.0`")

        self._vlan_id = vlan_id

    @property
    def addr_family(self):
        """
        Gets the addr_family of this GroupnetSubnetCreateParams.
        IP address format.

        :return: The addr_family of this GroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._addr_family

    @addr_family.setter
    def addr_family(self, addr_family):
        """
        Sets the addr_family of this GroupnetSubnetCreateParams.
        IP address format.

        :param addr_family: The addr_family of this GroupnetSubnetCreateParams.
        :type: str
        """
        allowed_values = ["ipv4", "ipv6"]
        if addr_family not in allowed_values:
            raise ValueError(
                "Invalid value for `addr_family`, must be one of {0}"
                .format(allowed_values)
            )

        self._addr_family = addr_family

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

