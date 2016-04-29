# coding: utf-8

"""
Copyright 2015 SmartBear Software

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


class JobType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobType - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'policy': 'str',
            'priority': 'int',
            'schedule': 'str'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'policy': 'policy',
            'priority': 'priority',
            'schedule': 'schedule'
        }

        self._enabled = None
        self._policy = None
        self._priority = None
        self._schedule = None

    @property
    def enabled(self):
        """
        Gets the enabled of this JobType.
        Whether the job type is enabled and able to run.

        :return: The enabled of this JobType.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this JobType.
        Whether the job type is enabled and able to run.

        :param enabled: The enabled of this JobType.
        :type: bool
        """
        self._enabled = enabled

    @property
    def policy(self):
        """
        Gets the policy of this JobType.
        Default impact policy of this job type.

        :return: The policy of this JobType.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this JobType.
        Default impact policy of this job type.

        :param policy: The policy of this JobType.
        :type: str
        """
        self._policy = policy

    @property
    def priority(self):
        """
        Gets the priority of this JobType.
        Default priority of this job type; lower numbers preempt higher numbers.

        :return: The priority of this JobType.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this JobType.
        Default priority of this job type; lower numbers preempt higher numbers.

        :param priority: The priority of this JobType.
        :type: int
        """
        self._priority = priority

    @property
    def schedule(self):
        """
        Gets the schedule of this JobType.
        The schedule on which this job type is queued, if any.

        :return: The schedule of this JobType.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this JobType.
        The schedule on which this job type is queued, if any.

        :param schedule: The schedule of this JobType.
        :type: str
        """
        self._schedule = schedule

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
