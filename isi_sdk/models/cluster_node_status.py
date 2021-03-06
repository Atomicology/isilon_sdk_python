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


class ClusterNodeStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterNodeStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'batterystatus': 'NodeStatusNodeBatterystatus',
            'capacity': 'list[NodeStatusNodeCapacityItem]',
            'cpu': 'NodeStatusNodeCpu',
            'nvram': 'NodeStatusNodeNvram',
            'powersupplies': 'NodeStatusNodePowersupplies',
            'release': 'str',
            'uptime': 'int',
            'version': 'str'
        }

        self.attribute_map = {
            'batterystatus': 'batterystatus',
            'capacity': 'capacity',
            'cpu': 'cpu',
            'nvram': 'nvram',
            'powersupplies': 'powersupplies',
            'release': 'release',
            'uptime': 'uptime',
            'version': 'version'
        }

        self._batterystatus = None
        self._capacity = None
        self._cpu = None
        self._nvram = None
        self._powersupplies = None
        self._release = None
        self._uptime = None
        self._version = None

    @property
    def batterystatus(self):
        """
        Gets the batterystatus of this ClusterNodeStatus.
        Battery status information.

        :return: The batterystatus of this ClusterNodeStatus.
        :rtype: NodeStatusNodeBatterystatus
        """
        return self._batterystatus

    @batterystatus.setter
    def batterystatus(self, batterystatus):
        """
        Sets the batterystatus of this ClusterNodeStatus.
        Battery status information.

        :param batterystatus: The batterystatus of this ClusterNodeStatus.
        :type: NodeStatusNodeBatterystatus
        """
        
        self._batterystatus = batterystatus

    @property
    def capacity(self):
        """
        Gets the capacity of this ClusterNodeStatus.
        Storage capacity of this node.

        :return: The capacity of this ClusterNodeStatus.
        :rtype: list[NodeStatusNodeCapacityItem]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ClusterNodeStatus.
        Storage capacity of this node.

        :param capacity: The capacity of this ClusterNodeStatus.
        :type: list[NodeStatusNodeCapacityItem]
        """
        
        self._capacity = capacity

    @property
    def cpu(self):
        """
        Gets the cpu of this ClusterNodeStatus.
        CPU status information for this node.

        :return: The cpu of this ClusterNodeStatus.
        :rtype: NodeStatusNodeCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this ClusterNodeStatus.
        CPU status information for this node.

        :param cpu: The cpu of this ClusterNodeStatus.
        :type: NodeStatusNodeCpu
        """
        
        self._cpu = cpu

    @property
    def nvram(self):
        """
        Gets the nvram of this ClusterNodeStatus.
        Node NVRAM information.

        :return: The nvram of this ClusterNodeStatus.
        :rtype: NodeStatusNodeNvram
        """
        return self._nvram

    @nvram.setter
    def nvram(self, nvram):
        """
        Sets the nvram of this ClusterNodeStatus.
        Node NVRAM information.

        :param nvram: The nvram of this ClusterNodeStatus.
        :type: NodeStatusNodeNvram
        """
        
        self._nvram = nvram

    @property
    def powersupplies(self):
        """
        Gets the powersupplies of this ClusterNodeStatus.
        Information about this node's power supplies.

        :return: The powersupplies of this ClusterNodeStatus.
        :rtype: NodeStatusNodePowersupplies
        """
        return self._powersupplies

    @powersupplies.setter
    def powersupplies(self, powersupplies):
        """
        Sets the powersupplies of this ClusterNodeStatus.
        Information about this node's power supplies.

        :param powersupplies: The powersupplies of this ClusterNodeStatus.
        :type: NodeStatusNodePowersupplies
        """
        
        self._powersupplies = powersupplies

    @property
    def release(self):
        """
        Gets the release of this ClusterNodeStatus.
        OneFS release.

        :return: The release of this ClusterNodeStatus.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """
        Sets the release of this ClusterNodeStatus.
        OneFS release.

        :param release: The release of this ClusterNodeStatus.
        :type: str
        """
        
        self._release = release

    @property
    def uptime(self):
        """
        Gets the uptime of this ClusterNodeStatus.
        Seconds this node has been online.

        :return: The uptime of this ClusterNodeStatus.
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """
        Sets the uptime of this ClusterNodeStatus.
        Seconds this node has been online.

        :param uptime: The uptime of this ClusterNodeStatus.
        :type: int
        """
        
        self._uptime = uptime

    @property
    def version(self):
        """
        Gets the version of this ClusterNodeStatus.
        OneFS version.

        :return: The version of this ClusterNodeStatus.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ClusterNodeStatus.
        OneFS version.

        :param version: The version of this ClusterNodeStatus.
        :type: str
        """
        
        self._version = version

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

