# coding: utf-8

"""
    UpGuard CyberRisk API

    Access information from the CyberRisk platform programmatically using this API.  You can find or generate an API key to access this API in your CyberRisk Account Settings. Please authorize all requests by setting the \"Authorization\" header to your api key.  The base url for all public endpoints is https://cyber-risk.upguard.com/api/public  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from upguard.api_client import ApiClient


class BulkApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_deregister_hostnames(self, **kwargs):  # noqa: E501
        """Deregister a list of hostnames  # noqa: E501

        Deregister a list of hostnames. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_deregister_hostnames(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkDeregisterHostnamesV1RequestBody bulk_deregister_hostnames_v1_request_body:
        :return: BulkDeregisterHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_deregister_hostnames_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bulk_deregister_hostnames_with_http_info(**kwargs)  # noqa: E501
            return data

    def bulk_deregister_hostnames_with_http_info(self, **kwargs):  # noqa: E501
        """Deregister a list of hostnames  # noqa: E501

        Deregister a list of hostnames. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_deregister_hostnames_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkDeregisterHostnamesV1RequestBody bulk_deregister_hostnames_v1_request_body:
        :return: BulkDeregisterHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bulk_deregister_hostnames_v1_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_deregister_hostnames" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bulk_deregister_hostnames_v1_request_body' in params:
            body_params = params['bulk_deregister_hostnames_v1_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkDeregisterHostnamesV1ResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_get_hostname_details(self, hostname, **kwargs):  # noqa: E501
        """Get the details for a hostname  # noqa: E501

        Get the details for a hostname. The provided hostname must be a fully qualified domain name or an IPv4 address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_get_hostname_details(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. (required)
        :param bool omit_scan_info: Omit the scan information, i.e. risks, score and last scanned at.
        :param bool omit_vendor: Omit the vendor information for a hostname in the response.
        :param bool omit_labels: Omit the labels for a hostname in the response.
        :return: BulkHostname
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_get_hostname_details_with_http_info(hostname, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_get_hostname_details_with_http_info(hostname, **kwargs)  # noqa: E501
            return data

    def bulk_get_hostname_details_with_http_info(self, hostname, **kwargs):  # noqa: E501
        """Get the details for a hostname  # noqa: E501

        Get the details for a hostname. The provided hostname must be a fully qualified domain name or an IPv4 address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_get_hostname_details_with_http_info(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. (required)
        :param bool omit_scan_info: Omit the scan information, i.e. risks, score and last scanned at.
        :param bool omit_vendor: Omit the vendor information for a hostname in the response.
        :param bool omit_labels: Omit the labels for a hostname in the response.
        :return: BulkHostname
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hostname', 'omit_scan_info', 'omit_vendor', 'omit_labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_get_hostname_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hostname' is set
        if self.api_client.client_side_validation and ('hostname' not in params or
                                                       params['hostname'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hostname` when calling `bulk_get_hostname_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hostname' in params:
            path_params['hostname'] = params['hostname']  # noqa: E501

        query_params = []
        if 'omit_scan_info' in params:
            query_params.append(('omit_scan_info', params['omit_scan_info']))  # noqa: E501
        if 'omit_vendor' in params:
            query_params.append(('omit_vendor', params['omit_vendor']))  # noqa: E501
        if 'omit_labels' in params:
            query_params.append(('omit_labels', params['omit_labels']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames/{hostname}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkHostname',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_get_hostnames_stats(self, **kwargs):  # noqa: E501
        """Get statistics around registered bulk hostnames  # noqa: E501

        Get statistics for the registered hostnames. This will return the number of registered hostnames, the number of remaining slots and the number of active and inactive hostnames  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_get_hostnames_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BulkGetHostnamesStatsV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_get_hostnames_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bulk_get_hostnames_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def bulk_get_hostnames_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get statistics around registered bulk hostnames  # noqa: E501

        Get statistics for the registered hostnames. This will return the number of registered hostnames, the number of remaining slots and the number of active and inactive hostnames  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_get_hostnames_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BulkGetHostnamesStatsV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_get_hostnames_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkGetHostnamesStatsV1ResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_hostname_put_labels(self, hostname, **kwargs):  # noqa: E501
        """Assign new labels to a hostname  # noqa: E501

        Assign labels to a hostname replacing the existing ones if any. To remove all labels use an empty array in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_hostname_put_labels(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. (required)
        :param list[str] labels: Labels list
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_hostname_put_labels_with_http_info(hostname, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_hostname_put_labels_with_http_info(hostname, **kwargs)  # noqa: E501
            return data

    def bulk_hostname_put_labels_with_http_info(self, hostname, **kwargs):  # noqa: E501
        """Assign new labels to a hostname  # noqa: E501

        Assign labels to a hostname replacing the existing ones if any. To remove all labels use an empty array in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_hostname_put_labels_with_http_info(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. (required)
        :param list[str] labels: Labels list
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hostname', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_hostname_put_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hostname' is set
        if self.api_client.client_side_validation and ('hostname' not in params or
                                                       params['hostname'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hostname` when calling `bulk_hostname_put_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hostname' in params:
            path_params['hostname'] = params['hostname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'labels' in params:
            body_params = params['labels']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames/{hostname}/labels', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_list_hostnames(self, **kwargs):  # noqa: E501
        """List hostnames and their risks  # noqa: E501

        Get the list of registered hostnames and their risks. You can use the omit_risks, omit_vendor, omit_score and omit_labels query parameter to turn off these information from the response and quickly get a list of registered hostnames.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_list_hostnames(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param bool sort_desc: Whether to sort the results in descending order.
        :param bool omit_scan_info: Omit the scan information, i.e. risks, score and last scanned at.
        :param bool omit_vendor: Omit the vendor information for a hostname in the response.
        :param bool omit_labels: Omit the labels for a hostname in the response.
        :param bool exclude_active: Exclude active hostnames from the results.
        :param bool exclude_inactive: Exclude inactive hostnames from the results.
        :param list[str] labels: Filter results to only hostnames that have all the provided labels.
        :return: BulkListHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_list_hostnames_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bulk_list_hostnames_with_http_info(**kwargs)  # noqa: E501
            return data

    def bulk_list_hostnames_with_http_info(self, **kwargs):  # noqa: E501
        """List hostnames and their risks  # noqa: E501

        Get the list of registered hostnames and their risks. You can use the omit_risks, omit_vendor, omit_score and omit_labels query parameter to turn off these information from the response and quickly get a list of registered hostnames.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_list_hostnames_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param bool sort_desc: Whether to sort the results in descending order.
        :param bool omit_scan_info: Omit the scan information, i.e. risks, score and last scanned at.
        :param bool omit_vendor: Omit the vendor information for a hostname in the response.
        :param bool omit_labels: Omit the labels for a hostname in the response.
        :param bool exclude_active: Exclude active hostnames from the results.
        :param bool exclude_inactive: Exclude inactive hostnames from the results.
        :param list[str] labels: Filter results to only hostnames that have all the provided labels.
        :return: BulkListHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_token', 'page_size', 'sort_desc', 'omit_scan_info', 'omit_vendor', 'omit_labels', 'exclude_active', 'exclude_inactive', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_list_hostnames" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] > 2000):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `bulk_list_hostnames`, must be a value less than or equal to `2000`")  # noqa: E501
        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] < 10):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `bulk_list_hostnames`, must be a value greater than or equal to `10`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_desc' in params:
            query_params.append(('sort_desc', params['sort_desc']))  # noqa: E501
        if 'omit_scan_info' in params:
            query_params.append(('omit_scan_info', params['omit_scan_info']))  # noqa: E501
        if 'omit_vendor' in params:
            query_params.append(('omit_vendor', params['omit_vendor']))  # noqa: E501
        if 'omit_labels' in params:
            query_params.append(('omit_labels', params['omit_labels']))  # noqa: E501
        if 'exclude_active' in params:
            query_params.append(('exclude_active', params['exclude_active']))  # noqa: E501
        if 'exclude_inactive' in params:
            query_params.append(('exclude_inactive', params['exclude_inactive']))  # noqa: E501
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
            collection_formats['labels'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkListHostnamesV1ResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_register_hostnames(self, **kwargs):  # noqa: E501
        """Register a list of hostnames to be scanned for risks  # noqa: E501

        Register a list of hostnames to be scanned for risks. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported. This will always replace the labels of currently registered hostnames and if the request has empty labels they will all be removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_register_hostnames(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkRegisterHostnamesV1RequestBody bulk_register_hostnames_v1_request_body:
        :return: BulkRegisterHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_register_hostnames_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bulk_register_hostnames_with_http_info(**kwargs)  # noqa: E501
            return data

    def bulk_register_hostnames_with_http_info(self, **kwargs):  # noqa: E501
        """Register a list of hostnames to be scanned for risks  # noqa: E501

        Register a list of hostnames to be scanned for risks. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported. This will always replace the labels of currently registered hostnames and if the request has empty labels they will all be removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_register_hostnames_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BulkRegisterHostnamesV1RequestBody bulk_register_hostnames_v1_request_body:
        :return: BulkRegisterHostnamesV1ResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bulk_register_hostnames_v1_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_register_hostnames" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bulk_register_hostnames_v1_request_body' in params:
            body_params = params['bulk_register_hostnames_v1_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key in header']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/hostnames', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkRegisterHostnamesV1ResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)