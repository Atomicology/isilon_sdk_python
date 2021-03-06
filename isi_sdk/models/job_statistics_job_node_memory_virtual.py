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


class JobStatisticsJobNodeMemoryVirtual(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobStatisticsJobNodeMemoryVirtual - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'average': 'float',
            'current': 'float',
            'maximum': 'float',
            'minimum': 'float'
        }

        self.attribute_map = {
            'average': 'average',
            'current': 'current',
            'maximum': 'maximum',
            'minimum': 'minimum'
        }

        self._average = None
        self._current = None
        self._maximum = None
        self._minimum = None

    @property
    def average(self):
        """
        Gets the average of this JobStatisticsJobNodeMemoryVirtual.
        The average virtual memory utilization of the job on this node, in KB.

        :return: The average of this JobStatisticsJobNodeMemoryVirtual.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """
        Sets the average of this JobStatisticsJobNodeMemoryVirtual.
        The average virtual memory utilization of the job on this node, in KB.

        :param average: The average of this JobStatisticsJobNodeMemoryVirtual.
        :type: float
        """
        
        self._average = average

    @property
    def current(self):
        """
        Gets the current of this JobStatisticsJobNodeMemoryVirtual.
        The current virtual memory utilization of the job on this node, in KB.

        :return: The current of this JobStatisticsJobNodeMemoryVirtual.
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this JobStatisticsJobNodeMemoryVirtual.
        The current virtual memory utilization of the job on this node, in KB.

        :param current: The current of this JobStatisticsJobNodeMemoryVirtual.
        :type: float
        """
        
        self._current = current

    @property
    def maximum(self):
        """
        Gets the maximum of this JobStatisticsJobNodeMemoryVirtual.
        The maximum virtual memory utilization of the job on this node, in KB.

        :return: The maximum of this JobStatisticsJobNodeMemoryVirtual.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Sets the maximum of this JobStatisticsJobNodeMemoryVirtual.
        The maximum virtual memory utilization of the job on this node, in KB.

        :param maximum: The maximum of this JobStatisticsJobNodeMemoryVirtual.
        :type: float
        """
        
        self._maximum = maximum

    @property
    def minimum(self):
        """
        Gets the minimum of this JobStatisticsJobNodeMemoryVirtual.
        The minimum virtual memory utilization of the job on this node, in KB.

        :return: The minimum of this JobStatisticsJobNodeMemoryVirtual.
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this JobStatisticsJobNodeMemoryVirtual.
        The minimum virtual memory utilization of the job on this node, in KB.

        :param minimum: The minimum of this JobStatisticsJobNodeMemoryVirtual.
        :type: float
        """
        
        self._minimum = minimum

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

