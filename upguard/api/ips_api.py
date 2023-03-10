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


class IpsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_custom_ips(self, ips, **kwargs):  # noqa: E501
        """Add custom ips  # noqa: E501

        Add a list of custom ips to your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_custom_ips(ips, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ips: The list of ips to add (required)
        :param list[str] labels: The labels to assign to the ips when added.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_custom_ips_with_http_info(ips, **kwargs)  # noqa: E501
        else:
            (data) = self.add_custom_ips_with_http_info(ips, **kwargs)  # noqa: E501
            return data

    def add_custom_ips_with_http_info(self, ips, **kwargs):  # noqa: E501
        """Add custom ips  # noqa: E501

        Add a list of custom ips to your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_custom_ips_with_http_info(ips, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ips: The list of ips to add (required)
        :param list[str] labels: The labels to assign to the ips when added.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ips', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_custom_ips" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ips' is set
        if self.api_client.client_side_validation and ('ips' not in params or
                                                       params['ips'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ips` when calling `add_custom_ips`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ips' in params:
            query_params.append(('ips', params['ips']))  # noqa: E501
            collection_formats['ips'] = 'multi'  # noqa: E501
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
            '/ips', 'PUT',
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

    def ip_details(self, ip, **kwargs):  # noqa: E501
        """Retrieve details for an IP address  # noqa: E501

        Returns the details of the IP address. It will return 422 when requesting details of an inactive IP address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ip_details(ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ip: The IP address to get details for (required)
        :return: GetIpDetailsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ip_details_with_http_info(ip, **kwargs)  # noqa: E501
        else:
            (data) = self.ip_details_with_http_info(ip, **kwargs)  # noqa: E501
            return data

    def ip_details_with_http_info(self, ip, **kwargs):  # noqa: E501
        """Retrieve details for an IP address  # noqa: E501

        Returns the details of the IP address. It will return 422 when requesting details of an inactive IP address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ip_details_with_http_info(ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ip: The IP address to get details for (required)
        :return: GetIpDetailsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ip_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in params or
                                                       params['ip'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ip` when calling `ip_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in params:
            query_params.append(('ip', params['ip']))  # noqa: E501

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
            '/ip', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetIpDetailsV1RespBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ip_update_labels(self, ip, labels, **kwargs):  # noqa: E501
        """Assign labels to an IP  # noqa: E501

        Assign labels to an IP. To remove all labels pass an empty list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ip_update_labels(ip, labels, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip: The IP to update labels for (required)
        :param list[str] labels: The labels to assign to the IP. You can pass an empty array to remove all labels. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ip_update_labels_with_http_info(ip, labels, **kwargs)  # noqa: E501
        else:
            (data) = self.ip_update_labels_with_http_info(ip, labels, **kwargs)  # noqa: E501
            return data

    def ip_update_labels_with_http_info(self, ip, labels, **kwargs):  # noqa: E501
        """Assign labels to an IP  # noqa: E501

        Assign labels to an IP. To remove all labels pass an empty list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ip_update_labels_with_http_info(ip, labels, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip: The IP to update labels for (required)
        :param list[str] labels: The labels to assign to the IP. You can pass an empty array to remove all labels. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ip_update_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip' is set
        if self.api_client.client_side_validation and ('ip' not in params or
                                                       params['ip'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ip` when calling `ip_update_labels`")  # noqa: E501
        # verify the required parameter 'labels' is set
        if self.api_client.client_side_validation and ('labels' not in params or
                                                       params['labels'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `labels` when calling `ip_update_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in params:
            query_params.append(('ip', params['ip']))  # noqa: E501
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
            '/ip/labels', 'PUT',
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

    def ips(self, **kwargs):  # noqa: E501
        """Get a list of ips  # noqa: E501

        Returns a list of ips for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ips(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the IPs by  If not specified will default to `ip` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetIPsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ips_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ips_with_http_info(**kwargs)  # noqa: E501
            return data

    def ips_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of ips  # noqa: E501

        Returns a list of ips for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ips_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the IPs by  If not specified will default to `ip` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetIPsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['labels', 'page_token', 'page_size', 'sort_by', 'sort_desc']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ips" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] > 2000):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `ips`, must be a value less than or equal to `2000`")  # noqa: E501
        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] < 10):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `ips`, must be a value greater than or equal to `10`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
            collection_formats['labels'] = 'multi'  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'sort_desc' in params:
            query_params.append(('sort_desc', params['sort_desc']))  # noqa: E501

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
            '/ips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetIPsV1RespBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ranges(self, **kwargs):  # noqa: E501
        """Get a list of ip ranges  # noqa: E501

        Returns a list of ip ranges for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ranges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the IP ranges by  If not specified will default to `num_ips` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetRangesV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ranges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ranges_with_http_info(**kwargs)  # noqa: E501
            return data

    def ranges_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of ip ranges  # noqa: E501

        Returns a list of ip ranges for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ranges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the IP ranges by  If not specified will default to `num_ips` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetRangesV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['labels', 'page_token', 'page_size', 'sort_by', 'sort_desc']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ranges" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] > 2000):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `ranges`, must be a value less than or equal to `2000`")  # noqa: E501
        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] < 10):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `ranges`, must be a value greater than or equal to `10`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
            collection_formats['labels'] = 'multi'  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'sort_desc' in params:
            query_params.append(('sort_desc', params['sort_desc']))  # noqa: E501

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
            '/ranges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRangesV1RespBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_custom_ips(self, **kwargs):  # noqa: E501
        """Remove custom ips  # noqa: E501

        Remove custom ips from your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_custom_ips(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ips: A comma separated list of ips to remove. Only ips or labels can be specified not both
        :param list[str] labels: A list of labels whose domains will be removed. All custom IPs with at least one of the provided labels will be removed. Only ips or labels can be specified not both
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_custom_ips_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_custom_ips_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_custom_ips_with_http_info(self, **kwargs):  # noqa: E501
        """Remove custom ips  # noqa: E501

        Remove custom ips from your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_custom_ips_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ips: A comma separated list of ips to remove. Only ips or labels can be specified not both
        :param list[str] labels: A list of labels whose domains will be removed. All custom IPs with at least one of the provided labels will be removed. Only ips or labels can be specified not both
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ips', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_custom_ips" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ips' in params:
            query_params.append(('ips', params['ips']))  # noqa: E501
            collection_formats['ips'] = 'multi'  # noqa: E501
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
            '/ips', 'DELETE',
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
