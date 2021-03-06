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


class CloudJobFiles(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudJobFiles - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file_matching_pattern': 'Empty',
            'names': 'list[CloudJobFilesName]',
            'total': 'int',
            'total_canceled': 'int',
            'total_failed': 'int',
            'total_pending': 'int',
            'total_processing': 'int',
            'total_succeeded': 'int'
        }

        self.attribute_map = {
            'file_matching_pattern': 'file_matching_pattern',
            'names': 'names',
            'total': 'total',
            'total_canceled': 'total_canceled',
            'total_failed': 'total_failed',
            'total_pending': 'total_pending',
            'total_processing': 'total_processing',
            'total_succeeded': 'total_succeeded'
        }

        self._file_matching_pattern = None
        self._names = None
        self._total = None
        self._total_canceled = None
        self._total_failed = None
        self._total_pending = None
        self._total_processing = None
        self._total_succeeded = None

    @property
    def file_matching_pattern(self):
        """
        Gets the file_matching_pattern of this CloudJobFiles.
        The file filtering logic to find files for this job

        :return: The file_matching_pattern of this CloudJobFiles.
        :rtype: Empty
        """
        return self._file_matching_pattern

    @file_matching_pattern.setter
    def file_matching_pattern(self, file_matching_pattern):
        """
        Sets the file_matching_pattern of this CloudJobFiles.
        The file filtering logic to find files for this job

        :param file_matching_pattern: The file_matching_pattern of this CloudJobFiles.
        :type: Empty
        """
        
        self._file_matching_pattern = file_matching_pattern

    @property
    def names(self):
        """
        Gets the names of this CloudJobFiles.
        A list of files to be addressed by this job.  (Note* these are only reported when audit_level is 'high'

        :return: The names of this CloudJobFiles.
        :rtype: list[CloudJobFilesName]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this CloudJobFiles.
        A list of files to be addressed by this job.  (Note* these are only reported when audit_level is 'high'

        :param names: The names of this CloudJobFiles.
        :type: list[CloudJobFilesName]
        """
        
        self._names = names

    @property
    def total(self):
        """
        Gets the total of this CloudJobFiles.
        The total number of files addressed by this job

        :return: The total of this CloudJobFiles.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this CloudJobFiles.
        The total number of files addressed by this job

        :param total: The total of this CloudJobFiles.
        :type: int
        """
        
        self._total = total

    @property
    def total_canceled(self):
        """
        Gets the total_canceled of this CloudJobFiles.
        The number of canceled files

        :return: The total_canceled of this CloudJobFiles.
        :rtype: int
        """
        return self._total_canceled

    @total_canceled.setter
    def total_canceled(self, total_canceled):
        """
        Sets the total_canceled of this CloudJobFiles.
        The number of canceled files

        :param total_canceled: The total_canceled of this CloudJobFiles.
        :type: int
        """
        
        self._total_canceled = total_canceled

    @property
    def total_failed(self):
        """
        Gets the total_failed of this CloudJobFiles.
        The number of files which failed

        :return: The total_failed of this CloudJobFiles.
        :rtype: int
        """
        return self._total_failed

    @total_failed.setter
    def total_failed(self, total_failed):
        """
        Sets the total_failed of this CloudJobFiles.
        The number of files which failed

        :param total_failed: The total_failed of this CloudJobFiles.
        :type: int
        """
        
        self._total_failed = total_failed

    @property
    def total_pending(self):
        """
        Gets the total_pending of this CloudJobFiles.
        The number of files pending action

        :return: The total_pending of this CloudJobFiles.
        :rtype: int
        """
        return self._total_pending

    @total_pending.setter
    def total_pending(self, total_pending):
        """
        Sets the total_pending of this CloudJobFiles.
        The number of files pending action

        :param total_pending: The total_pending of this CloudJobFiles.
        :type: int
        """
        
        self._total_pending = total_pending

    @property
    def total_processing(self):
        """
        Gets the total_processing of this CloudJobFiles.
        The number of files currently being processed

        :return: The total_processing of this CloudJobFiles.
        :rtype: int
        """
        return self._total_processing

    @total_processing.setter
    def total_processing(self, total_processing):
        """
        Sets the total_processing of this CloudJobFiles.
        The number of files currently being processed

        :param total_processing: The total_processing of this CloudJobFiles.
        :type: int
        """
        
        self._total_processing = total_processing

    @property
    def total_succeeded(self):
        """
        Gets the total_succeeded of this CloudJobFiles.
        The total number of files successfully completed

        :return: The total_succeeded of this CloudJobFiles.
        :rtype: int
        """
        return self._total_succeeded

    @total_succeeded.setter
    def total_succeeded(self, total_succeeded):
        """
        Sets the total_succeeded of this CloudJobFiles.
        The total number of files successfully completed

        :param total_succeeded: The total_succeeded of this CloudJobFiles.
        :type: int
        """
        
        self._total_succeeded = total_succeeded

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

