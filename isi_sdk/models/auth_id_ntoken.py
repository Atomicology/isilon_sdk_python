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


class AuthIdNtoken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthIdNtoken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_id': 'list[GroupsGroupMember]',
            'gid': 'GroupsGroupMember',
            'group_sid': 'GroupsGroupMember',
            'ifs_restricted': 'bool',
            'local_address': 'str',
            'on_disk_group_id': 'GroupsGroupMember',
            'on_disk_user_id': 'GroupsGroupMember',
            'privilege': 'list[AuthIdNtokenPrivilegeItem]',
            'protocol': 'int',
            'remote_address': 'str',
            'uid': 'GroupsGroupMember',
            'user_sid': 'GroupsGroupMember',
            'zid': 'int',
            'zone_id': 'str'
        }

        self.attribute_map = {
            'additional_id': 'additional_id',
            'gid': 'gid',
            'group_sid': 'group_sid',
            'ifs_restricted': 'ifs_restricted',
            'local_address': 'local_address',
            'on_disk_group_id': 'on_disk_group_id',
            'on_disk_user_id': 'on_disk_user_id',
            'privilege': 'privilege',
            'protocol': 'protocol',
            'remote_address': 'remote_address',
            'uid': 'uid',
            'user_sid': 'user_sid',
            'zid': 'zid',
            'zone_id': 'zone_id'
        }

        self._additional_id = None
        self._gid = None
        self._group_sid = None
        self._ifs_restricted = None
        self._local_address = None
        self._on_disk_group_id = None
        self._on_disk_user_id = None
        self._privilege = None
        self._protocol = None
        self._remote_address = None
        self._uid = None
        self._user_sid = None
        self._zid = None
        self._zone_id = None

    @property
    def additional_id(self):
        """
        Gets the additional_id of this AuthIdNtoken.
        Specifies additional UIDs, GIDs, and SIDs.

        :return: The additional_id of this AuthIdNtoken.
        :rtype: list[GroupsGroupMember]
        """
        return self._additional_id

    @additional_id.setter
    def additional_id(self, additional_id):
        """
        Sets the additional_id of this AuthIdNtoken.
        Specifies additional UIDs, GIDs, and SIDs.

        :param additional_id: The additional_id of this AuthIdNtoken.
        :type: list[GroupsGroupMember]
        """
        self._additional_id = additional_id

    @property
    def gid(self):
        """
        Gets the gid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The gid of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param gid: The gid of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._gid = gid

    @property
    def group_sid(self):
        """
        Gets the group_sid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The group_sid of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._group_sid

    @group_sid.setter
    def group_sid(self, group_sid):
        """
        Sets the group_sid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param group_sid: The group_sid of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._group_sid = group_sid

    @property
    def ifs_restricted(self):
        """
        Gets the ifs_restricted of this AuthIdNtoken.
        Indicates if this user has restricted access to the /ifs file system.

        :return: The ifs_restricted of this AuthIdNtoken.
        :rtype: bool
        """
        return self._ifs_restricted

    @ifs_restricted.setter
    def ifs_restricted(self, ifs_restricted):
        """
        Sets the ifs_restricted of this AuthIdNtoken.
        Indicates if this user has restricted access to the /ifs file system.

        :param ifs_restricted: The ifs_restricted of this AuthIdNtoken.
        :type: bool
        """
        self._ifs_restricted = ifs_restricted

    @property
    def local_address(self):
        """
        Gets the local_address of this AuthIdNtoken.
        Specifies the IP address of the node that is serving the request.

        :return: The local_address of this AuthIdNtoken.
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """
        Sets the local_address of this AuthIdNtoken.
        Specifies the IP address of the node that is serving the request.

        :param local_address: The local_address of this AuthIdNtoken.
        :type: str
        """
        self._local_address = local_address

    @property
    def on_disk_group_id(self):
        """
        Gets the on_disk_group_id of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The on_disk_group_id of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._on_disk_group_id

    @on_disk_group_id.setter
    def on_disk_group_id(self, on_disk_group_id):
        """
        Sets the on_disk_group_id of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param on_disk_group_id: The on_disk_group_id of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._on_disk_group_id = on_disk_group_id

    @property
    def on_disk_user_id(self):
        """
        Gets the on_disk_user_id of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The on_disk_user_id of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._on_disk_user_id

    @on_disk_user_id.setter
    def on_disk_user_id(self, on_disk_user_id):
        """
        Sets the on_disk_user_id of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param on_disk_user_id: The on_disk_user_id of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._on_disk_user_id = on_disk_user_id

    @property
    def privilege(self):
        """
        Gets the privilege of this AuthIdNtoken.
        Specifies the privileges granted to the currently authenticated user.

        :return: The privilege of this AuthIdNtoken.
        :rtype: list[AuthIdNtokenPrivilegeItem]
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """
        Sets the privilege of this AuthIdNtoken.
        Specifies the privileges granted to the currently authenticated user.

        :param privilege: The privilege of this AuthIdNtoken.
        :type: list[AuthIdNtokenPrivilegeItem]
        """
        self._privilege = privilege

    @property
    def protocol(self):
        """
        Gets the protocol of this AuthIdNtoken.
        Specifies the protocol that is responsible for the creation of the token. The integer values for each protcol are as follows: NFS (1), SMB (2), NLM (3), FTP (4), HTTP (5), ISCSI (7), SMB2 (8), NFS4 (9), OneFS API (10), HDFS (15), console (16), and SSH (17).

        :return: The protocol of this AuthIdNtoken.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this AuthIdNtoken.
        Specifies the protocol that is responsible for the creation of the token. The integer values for each protcol are as follows: NFS (1), SMB (2), NLM (3), FTP (4), HTTP (5), ISCSI (7), SMB2 (8), NFS4 (9), OneFS API (10), HDFS (15), console (16), and SSH (17).

        :param protocol: The protocol of this AuthIdNtoken.
        :type: int
        """
        self._protocol = protocol

    @property
    def remote_address(self):
        """
        Gets the remote_address of this AuthIdNtoken.
        Specifies the IP address of the client requesting information.

        :return: The remote_address of this AuthIdNtoken.
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """
        Sets the remote_address of this AuthIdNtoken.
        Specifies the IP address of the client requesting information.

        :param remote_address: The remote_address of this AuthIdNtoken.
        :type: str
        """
        self._remote_address = remote_address

    @property
    def uid(self):
        """
        Gets the uid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The uid of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param uid: The uid of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._uid = uid

    @property
    def user_sid(self):
        """
        Gets the user_sid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The user_sid of this AuthIdNtoken.
        :rtype: GroupsGroupMember
        """
        return self._user_sid

    @user_sid.setter
    def user_sid(self, user_sid):
        """
        Sets the user_sid of this AuthIdNtoken.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param user_sid: The user_sid of this AuthIdNtoken.
        :type: GroupsGroupMember
        """
        self._user_sid = user_sid

    @property
    def zid(self):
        """
        Gets the zid of this AuthIdNtoken.
        Specifies the zone ID of the access zone that is serving the request.

        :return: The zid of this AuthIdNtoken.
        :rtype: int
        """
        return self._zid

    @zid.setter
    def zid(self, zid):
        """
        Sets the zid of this AuthIdNtoken.
        Specifies the zone ID of the access zone that is serving the request.

        :param zid: The zid of this AuthIdNtoken.
        :type: int
        """
        self._zid = zid

    @property
    def zone_id(self):
        """
        Gets the zone_id of this AuthIdNtoken.
        Specifies the name of the access zone that is serving the request.

        :return: The zone_id of this AuthIdNtoken.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this AuthIdNtoken.
        Specifies the name of the access zone that is serving the request.

        :param zone_id: The zone_id of this AuthIdNtoken.
        :type: str
        """
        self._zone_id = zone_id

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
