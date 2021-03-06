# coding: utf-8

"""
    maiot Core Engine API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ce_api.api_client import ApiClient


class MetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get(self, pipeline_id, **kwargs):  # noqa: E501
        """Calculate Pipeline Metrics  # noqa: E501

        Calculate latest metrics of pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :return: RunMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get_with_http_info(pipeline_id, **kwargs)  # noqa: E501
        else:
            (data) = self.calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get_with_http_info(pipeline_id, **kwargs)  # noqa: E501
            return data

    def calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get_with_http_info(self, pipeline_id, **kwargs):  # noqa: E501
        """Calculate Pipeline Metrics  # noqa: E501

        Calculate latest metrics of pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get_with_http_info(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :return: RunMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pipeline_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if ('pipeline_id' not in params or
                params['pipeline_id'] is None):
            raise ValueError("Missing the required parameter `pipeline_id` when calling `calculate_pipeline_metrics_api_v1_metrics_pipeline_id_calculate_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in params:
            path_params['pipeline_id'] = params['pipeline_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/metrics/{pipeline_id}/calculate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunMetric',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component_metrics_api_v1_metrics_pipeline_id_component_type_get(self, pipeline_id, component_type, **kwargs):  # noqa: E501
        """Get Component Metrics  # noqa: E501

        Analyzes pipelines latest run. Choose from component list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_metrics_api_v1_metrics_pipeline_id_component_type_get(pipeline_id, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :param str component_type: (required)
        :return: ComponentMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_metrics_api_v1_metrics_pipeline_id_component_type_get_with_http_info(pipeline_id, component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_metrics_api_v1_metrics_pipeline_id_component_type_get_with_http_info(pipeline_id, component_type, **kwargs)  # noqa: E501
            return data

    def get_component_metrics_api_v1_metrics_pipeline_id_component_type_get_with_http_info(self, pipeline_id, component_type, **kwargs):  # noqa: E501
        """Get Component Metrics  # noqa: E501

        Analyzes pipelines latest run. Choose from component list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_metrics_api_v1_metrics_pipeline_id_component_type_get_with_http_info(pipeline_id, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :param str component_type: (required)
        :return: ComponentMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pipeline_id', 'component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_metrics_api_v1_metrics_pipeline_id_component_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if ('pipeline_id' not in params or
                params['pipeline_id'] is None):
            raise ValueError("Missing the required parameter `pipeline_id` when calling `get_component_metrics_api_v1_metrics_pipeline_id_component_type_get`")  # noqa: E501
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `get_component_metrics_api_v1_metrics_pipeline_id_component_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in params:
            path_params['pipeline_id'] = params['pipeline_id']  # noqa: E501
        if 'component_type' in params:
            path_params['component_type'] = params['component_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/metrics/{pipeline_id}/{component_type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComponentMetric',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pipeline_metrics_api_v1_metrics_pipeline_id_get(self, pipeline_id, **kwargs):  # noqa: E501
        """Get Pipeline Metrics  # noqa: E501

        Get latest metrics of pipeline. Does not calculate metrics, just returns the latest calculated one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_metrics_api_v1_metrics_pipeline_id_get(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :return: RunMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pipeline_metrics_api_v1_metrics_pipeline_id_get_with_http_info(pipeline_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pipeline_metrics_api_v1_metrics_pipeline_id_get_with_http_info(pipeline_id, **kwargs)  # noqa: E501
            return data

    def get_pipeline_metrics_api_v1_metrics_pipeline_id_get_with_http_info(self, pipeline_id, **kwargs):  # noqa: E501
        """Get Pipeline Metrics  # noqa: E501

        Get latest metrics of pipeline. Does not calculate metrics, just returns the latest calculated one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_metrics_api_v1_metrics_pipeline_id_get_with_http_info(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pipeline_id: (required)
        :return: RunMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pipeline_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pipeline_metrics_api_v1_metrics_pipeline_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if ('pipeline_id' not in params or
                params['pipeline_id'] is None):
            raise ValueError("Missing the required parameter `pipeline_id` when calling `get_pipeline_metrics_api_v1_metrics_pipeline_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in params:
            path_params['pipeline_id'] = params['pipeline_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/metrics/{pipeline_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunMetric',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
