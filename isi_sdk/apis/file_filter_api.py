# coding: utf-8

"""
FileFilterApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FileFilterApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_file_filter_settings(self, **kwargs):
        """
        
        View File Filtering settings of an access zone

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_filter_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FileFilterSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_filter_settings" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/platform/3/file-filter/settings'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='FileFilterSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_file_filter_settings(self, file_filter_settings, **kwargs):
        """
        
        Modify one or more File Filtering settings for an access zone

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_file_filter_settings(file_filter_settings, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FileFilterSettings file_filter_settings:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_filter_settings']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_file_filter_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'file_filter_settings' is set
        if ('file_filter_settings' not in params) or (params['file_filter_settings'] is None):
            raise ValueError("Missing the required parameter `file_filter_settings` when calling `update_file_filter_settings`")

        resource_path = '/platform/3/file-filter/settings'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'file_filter_settings' in params:
            body_params = params['file_filter_settings']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response