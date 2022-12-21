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


class DomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_custom_domains(self, hostnames, **kwargs):  # noqa: E501
        """Add custom domains  # noqa: E501

        Add a list of custom domains to your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_custom_domains(hostnames, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] hostnames: A comma separated list of hostnames to add (required)
        :param list[str] labels: The labels to add to the hostnames
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_custom_domains_with_http_info(hostnames, **kwargs)  # noqa: E501
        else:
            (data) = self.add_custom_domains_with_http_info(hostnames, **kwargs)  # noqa: E501
            return data

    def add_custom_domains_with_http_info(self, hostnames, **kwargs):  # noqa: E501
        """Add custom domains  # noqa: E501

        Add a list of custom domains to your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_custom_domains_with_http_info(hostnames, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] hostnames: A comma separated list of hostnames to add (required)
        :param list[str] labels: The labels to add to the hostnames
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hostnames', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_custom_domains" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hostnames' is set
        if self.api_client.client_side_validation and ('hostnames' not in params or
                                                       params['hostnames'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hostnames` when calling `add_custom_domains`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hostnames' in params:
            query_params.append(('hostnames', params['hostnames']))  # noqa: E501
            collection_formats['hostnames'] = 'multi'  # noqa: E501
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
            '/domains', 'PUT',
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

    def domain_details(self, hostname, **kwargs):  # noqa: E501
        """Retrieve details for a domain  # noqa: E501

        Returns the details for a domain. It will return 422 when requesting details of an inactive domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_details(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname for which to return the details, e.g. \"upguard.com\" (required)
        :return: GetDomainDetailsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_details_with_http_info(hostname, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_details_with_http_info(hostname, **kwargs)  # noqa: E501
            return data

    def domain_details_with_http_info(self, hostname, **kwargs):  # noqa: E501
        """Retrieve details for a domain  # noqa: E501

        Returns the details for a domain. It will return 422 when requesting details of an inactive domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_details_with_http_info(hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname for which to return the details, e.g. \"upguard.com\" (required)
        :return: GetDomainDetailsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hostname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hostname' is set
        if self.api_client.client_side_validation and ('hostname' not in params or
                                                       params['hostname'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hostname` when calling `domain_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hostname' in params:
            query_params.append(('hostname', params['hostname']))  # noqa: E501

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
            '/domain', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDomainDetailsV1RespBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_update_labels(self, hostname, labels, **kwargs):  # noqa: E501
        """Assign labels to a domain  # noqa: E501

        Assign labels to a domain. To remove all labels pass an empty list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_update_labels(hostname, labels, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to update labels for (required)
        :param list[str] labels: The labels to assign to the domain. You can pass an empty array to remove all labels. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_update_labels_with_http_info(hostname, labels, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_update_labels_with_http_info(hostname, labels, **kwargs)  # noqa: E501
            return data

    def domain_update_labels_with_http_info(self, hostname, labels, **kwargs):  # noqa: E501
        """Assign labels to a domain  # noqa: E501

        Assign labels to a domain. To remove all labels pass an empty list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_update_labels_with_http_info(hostname, labels, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hostname: The hostname to update labels for (required)
        :param list[str] labels: The labels to assign to the domain. You can pass an empty array to remove all labels. (required)
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
                    " to method domain_update_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hostname' is set
        if self.api_client.client_side_validation and ('hostname' not in params or
                                                       params['hostname'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hostname` when calling `domain_update_labels`")  # noqa: E501
        # verify the required parameter 'labels' is set
        if self.api_client.client_side_validation and ('labels' not in params or
                                                       params['labels'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `labels` when calling `domain_update_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hostname' in params:
            query_params.append(('hostname', params['hostname']))  # noqa: E501
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
            '/domain/labels', 'PUT',
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

    def domains(self, **kwargs):  # noqa: E501
        """Get a list of domains  # noqa: E501

        Returns a list of domains for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool active: Retrieve active domains
        :param bool inactive: Retrieve inactive domains
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the domains by  If not specified will default to `domain` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetDomainsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def domains_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of domains  # noqa: E501

        Returns a list of domains for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool active: Retrieve active domains
        :param bool inactive: Retrieve inactive domains
        :param list[str] labels: Filter result by the provided labels
        :param str page_token: The `page_token` from a previous request, use this to get the next page of results.
        :param int page_size: The number of results to return per page.
        :param str sort_by: The value to sort the domains by  If not specified will default to `domain` and set `sort_desc` to `true`
        :param bool sort_desc: Whether or not to sort the results in descending order
        :return: GetDomainsV1RespBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['active', 'inactive', 'labels', 'page_token', 'page_size', 'sort_by', 'sort_desc']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] > 2000):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `domains`, must be a value less than or equal to `2000`")  # noqa: E501
        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] < 10):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `domains`, must be a value greater than or equal to `10`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501
        if 'inactive' in params:
            query_params.append(('inactive', params['inactive']))  # noqa: E501
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
            '/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDomainsV1RespBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_custom_domains(self, **kwargs):  # noqa: E501
        """Remove custom domains  # noqa: E501

        Remove custom domains from your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_custom_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] hostnames: A comma separated list of hostnames to remove. Only hostnames or labels can be specified not both
        :param list[str] labels: A list of labels whose hostnames will be removed. All custom domains with at least one of the provided labels will be removed. Only hostnames or labels can be specified not both
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_custom_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_custom_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_custom_domains_with_http_info(self, **kwargs):  # noqa: E501
        """Remove custom domains  # noqa: E501

        Remove custom domains from your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_custom_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] hostnames: A comma separated list of hostnames to remove. Only hostnames or labels can be specified not both
        :param list[str] labels: A list of labels whose hostnames will be removed. All custom domains with at least one of the provided labels will be removed. Only hostnames or labels can be specified not both
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hostnames', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_custom_domains" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hostnames' in params:
            query_params.append(('hostnames', params['hostnames']))  # noqa: E501
            collection_formats['hostnames'] = 'multi'  # noqa: E501
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
            '/domains', 'DELETE',
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
