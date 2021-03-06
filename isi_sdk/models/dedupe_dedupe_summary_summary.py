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


class DedupeDedupeSummarySummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DedupeDedupeSummarySummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'block_size': 'float',
            'estimated_physical_blocks': 'float',
            'estimated_saved_blocks': 'float',
            'logical_blocks': 'float',
            'saved_logical_blocks': 'float',
            'total_blocks': 'float',
            'used_blocks': 'float'
        }

        self.attribute_map = {
            'block_size': 'block_size',
            'estimated_physical_blocks': 'estimated_physical_blocks',
            'estimated_saved_blocks': 'estimated_saved_blocks',
            'logical_blocks': 'logical_blocks',
            'saved_logical_blocks': 'saved_logical_blocks',
            'total_blocks': 'total_blocks',
            'used_blocks': 'used_blocks'
        }

        self._block_size = None
        self._estimated_physical_blocks = None
        self._estimated_saved_blocks = None
        self._logical_blocks = None
        self._saved_logical_blocks = None
        self._total_blocks = None
        self._used_blocks = None

    @property
    def block_size(self):
        """
        Gets the block_size of this DedupeDedupeSummarySummary.
        Size in bytes of a filesystem block.

        :return: The block_size of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """
        Sets the block_size of this DedupeDedupeSummarySummary.
        Size in bytes of a filesystem block.

        :param block_size: The block_size of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._block_size = block_size

    @property
    def estimated_physical_blocks(self):
        """
        Gets the estimated_physical_blocks of this DedupeDedupeSummarySummary.
        Estimated number of physical blocks deduped.

        :return: The estimated_physical_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._estimated_physical_blocks

    @estimated_physical_blocks.setter
    def estimated_physical_blocks(self, estimated_physical_blocks):
        """
        Sets the estimated_physical_blocks of this DedupeDedupeSummarySummary.
        Estimated number of physical blocks deduped.

        :param estimated_physical_blocks: The estimated_physical_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._estimated_physical_blocks = estimated_physical_blocks

    @property
    def estimated_saved_blocks(self):
        """
        Gets the estimated_saved_blocks of this DedupeDedupeSummarySummary.
        Estimated number of physical blocks saved by dedupe.

        :return: The estimated_saved_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._estimated_saved_blocks

    @estimated_saved_blocks.setter
    def estimated_saved_blocks(self, estimated_saved_blocks):
        """
        Sets the estimated_saved_blocks of this DedupeDedupeSummarySummary.
        Estimated number of physical blocks saved by dedupe.

        :param estimated_saved_blocks: The estimated_saved_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._estimated_saved_blocks = estimated_saved_blocks

    @property
    def logical_blocks(self):
        """
        Gets the logical_blocks of this DedupeDedupeSummarySummary.
        Number of logical blocks deduped.

        :return: The logical_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._logical_blocks

    @logical_blocks.setter
    def logical_blocks(self, logical_blocks):
        """
        Sets the logical_blocks of this DedupeDedupeSummarySummary.
        Number of logical blocks deduped.

        :param logical_blocks: The logical_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._logical_blocks = logical_blocks

    @property
    def saved_logical_blocks(self):
        """
        Gets the saved_logical_blocks of this DedupeDedupeSummarySummary.
        Number of logical blocks saved by dedupe.

        :return: The saved_logical_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._saved_logical_blocks

    @saved_logical_blocks.setter
    def saved_logical_blocks(self, saved_logical_blocks):
        """
        Sets the saved_logical_blocks of this DedupeDedupeSummarySummary.
        Number of logical blocks saved by dedupe.

        :param saved_logical_blocks: The saved_logical_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._saved_logical_blocks = saved_logical_blocks

    @property
    def total_blocks(self):
        """
        Gets the total_blocks of this DedupeDedupeSummarySummary.
        Total physical blocks in the cluster.

        :return: The total_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._total_blocks

    @total_blocks.setter
    def total_blocks(self, total_blocks):
        """
        Sets the total_blocks of this DedupeDedupeSummarySummary.
        Total physical blocks in the cluster.

        :param total_blocks: The total_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._total_blocks = total_blocks

    @property
    def used_blocks(self):
        """
        Gets the used_blocks of this DedupeDedupeSummarySummary.
        Total physical blocks used in the cluster.

        :return: The used_blocks of this DedupeDedupeSummarySummary.
        :rtype: float
        """
        return self._used_blocks

    @used_blocks.setter
    def used_blocks(self, used_blocks):
        """
        Sets the used_blocks of this DedupeDedupeSummarySummary.
        Total physical blocks used in the cluster.

        :param used_blocks: The used_blocks of this DedupeDedupeSummarySummary.
        :type: float
        """
        
        self._used_blocks = used_blocks

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

