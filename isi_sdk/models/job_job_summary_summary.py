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


class JobJobSummarySummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobJobSummarySummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cluster_is_degraded': 'bool',
            'connected': 'bool',
            'coordinator': 'int',
            'disconnected_nodes': 'list[int]',
            'down_or_read_only_nodes': 'bool',
            'next_jid': 'int',
            'run_degraded': 'bool',
            'stats_ready': 'bool'
        }

        self.attribute_map = {
            'cluster_is_degraded': 'cluster_is_degraded',
            'connected': 'connected',
            'coordinator': 'coordinator',
            'disconnected_nodes': 'disconnected_nodes',
            'down_or_read_only_nodes': 'down_or_read_only_nodes',
            'next_jid': 'next_jid',
            'run_degraded': 'run_degraded',
            'stats_ready': 'stats_ready'
        }

        self._cluster_is_degraded = None
        self._connected = None
        self._coordinator = None
        self._disconnected_nodes = None
        self._down_or_read_only_nodes = None
        self._next_jid = None
        self._run_degraded = None
        self._stats_ready = None

    @property
    def cluster_is_degraded(self):
        """
        Gets the cluster_is_degraded of this JobJobSummarySummary.
        Whether the cluster is in a degraded state.  Note this is from the perspective of the node handling the query, which might be different from another node.

        :return: The cluster_is_degraded of this JobJobSummarySummary.
        :rtype: bool
        """
        return self._cluster_is_degraded

    @cluster_is_degraded.setter
    def cluster_is_degraded(self, cluster_is_degraded):
        """
        Sets the cluster_is_degraded of this JobJobSummarySummary.
        Whether the cluster is in a degraded state.  Note this is from the perspective of the node handling the query, which might be different from another node.

        :param cluster_is_degraded: The cluster_is_degraded of this JobJobSummarySummary.
        :type: bool
        """
        self._cluster_is_degraded = cluster_is_degraded

    @property
    def connected(self):
        """
        Gets the connected of this JobJobSummarySummary.
        Whether isi_job_d instances on all up nodes in the cluster are connected to the coordinator.

        :return: The connected of this JobJobSummarySummary.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """
        Sets the connected of this JobJobSummarySummary.
        Whether isi_job_d instances on all up nodes in the cluster are connected to the coordinator.

        :param connected: The connected of this JobJobSummarySummary.
        :type: bool
        """
        self._connected = connected

    @property
    def coordinator(self):
        """
        Gets the coordinator of this JobJobSummarySummary.
        The devid of the job engine coordinator.

        :return: The coordinator of this JobJobSummarySummary.
        :rtype: int
        """
        return self._coordinator

    @coordinator.setter
    def coordinator(self, coordinator):
        """
        Sets the coordinator of this JobJobSummarySummary.
        The devid of the job engine coordinator.

        :param coordinator: The coordinator of this JobJobSummarySummary.
        :type: int
        """
        self._coordinator = coordinator

    @property
    def disconnected_nodes(self):
        """
        Gets the disconnected_nodes of this JobJobSummarySummary.
        If connected=false, this is the set of devids that are not connected to the coordinator.

        :return: The disconnected_nodes of this JobJobSummarySummary.
        :rtype: list[int]
        """
        return self._disconnected_nodes

    @disconnected_nodes.setter
    def disconnected_nodes(self, disconnected_nodes):
        """
        Sets the disconnected_nodes of this JobJobSummarySummary.
        If connected=false, this is the set of devids that are not connected to the coordinator.

        :param disconnected_nodes: The disconnected_nodes of this JobJobSummarySummary.
        :type: list[int]
        """
        self._disconnected_nodes = disconnected_nodes

    @property
    def down_or_read_only_nodes(self):
        """
        Gets the down_or_read_only_nodes of this JobJobSummarySummary.
        Whether the cluster has any down or read-only nodes.  These nodes are not considered in the connected property.

        :return: The down_or_read_only_nodes of this JobJobSummarySummary.
        :rtype: bool
        """
        return self._down_or_read_only_nodes

    @down_or_read_only_nodes.setter
    def down_or_read_only_nodes(self, down_or_read_only_nodes):
        """
        Sets the down_or_read_only_nodes of this JobJobSummarySummary.
        Whether the cluster has any down or read-only nodes.  These nodes are not considered in the connected property.

        :param down_or_read_only_nodes: The down_or_read_only_nodes of this JobJobSummarySummary.
        :type: bool
        """
        self._down_or_read_only_nodes = down_or_read_only_nodes

    @property
    def next_jid(self):
        """
        Gets the next_jid of this JobJobSummarySummary.
        The job ID to be assigned to the next job.

        :return: The next_jid of this JobJobSummarySummary.
        :rtype: int
        """
        return self._next_jid

    @next_jid.setter
    def next_jid(self, next_jid):
        """
        Sets the next_jid of this JobJobSummarySummary.
        The job ID to be assigned to the next job.

        :param next_jid: The next_jid of this JobJobSummarySummary.
        :type: int
        """
        self._next_jid = next_jid

    @property
    def run_degraded(self):
        """
        Gets the run_degraded of this JobJobSummarySummary.
        Whether the job engine would allow most jobs to run even when the cluster is in a degraded state.

        :return: The run_degraded of this JobJobSummarySummary.
        :rtype: bool
        """
        return self._run_degraded

    @run_degraded.setter
    def run_degraded(self, run_degraded):
        """
        Sets the run_degraded of this JobJobSummarySummary.
        Whether the job engine would allow most jobs to run even when the cluster is in a degraded state.

        :param run_degraded: The run_degraded of this JobJobSummarySummary.
        :type: bool
        """
        self._run_degraded = run_degraded

    @property
    def stats_ready(self):
        """
        Gets the stats_ready of this JobJobSummarySummary.
        Whether the coordinator has recently gathered statistics for all nodes in the cluster.

        :return: The stats_ready of this JobJobSummarySummary.
        :rtype: bool
        """
        return self._stats_ready

    @stats_ready.setter
    def stats_ready(self, stats_ready):
        """
        Sets the stats_ready of this JobJobSummarySummary.
        Whether the coordinator has recently gathered statistics for all nodes in the cluster.

        :param stats_ready: The stats_ready of this JobJobSummarySummary.
        :type: bool
        """
        self._stats_ready = stats_ready

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
