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


class OrganizationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_invite_api_v1_organizations_invite_post(self, body, **kwargs):  # noqa: E501
        """Create Invite  # noqa: E501

        Invites user with specified email to organization via email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invite_api_v1_organizations_invite_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InviteCreate body: (required)
        :return: Invite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_invite_api_v1_organizations_invite_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_invite_api_v1_organizations_invite_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_invite_api_v1_organizations_invite_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Invite  # noqa: E501

        Invites user with specified email to organization via email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invite_api_v1_organizations_invite_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InviteCreate body: (required)
        :return: Invite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invite_api_v1_organizations_invite_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_invite_api_v1_organizations_invite_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/invite', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Invite',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_organization_api_v1_organizations_post(self, body, **kwargs):  # noqa: E501
        """Create Organization  # noqa: E501

        Create new organization. Only for admins. Users create orgs via sign up.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_organization_api_v1_organizations_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrgIn body: (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_organization_api_v1_organizations_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_organization_api_v1_organizations_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_organization_api_v1_organizations_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Organization  # noqa: E501

        Create new organization. Only for admins. Users create orgs via sign up.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_organization_api_v1_organizations_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrgIn body: (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization_api_v1_organizations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_organization_api_v1_organizations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_invite_api_v1_organizations_invite_invite_id_delete(self, invite_id, **kwargs):  # noqa: E501
        """Delete Invite  # noqa: E501

        Deletes the invite specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_invite_api_v1_organizations_invite_invite_id_delete(invite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invite_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_invite_api_v1_organizations_invite_invite_id_delete_with_http_info(invite_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_invite_api_v1_organizations_invite_invite_id_delete_with_http_info(invite_id, **kwargs)  # noqa: E501
            return data

    def delete_invite_api_v1_organizations_invite_invite_id_delete_with_http_info(self, invite_id, **kwargs):  # noqa: E501
        """Delete Invite  # noqa: E501

        Deletes the invite specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_invite_api_v1_organizations_invite_invite_id_delete_with_http_info(invite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invite_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invite_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_invite_api_v1_organizations_invite_invite_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invite_id' is set
        if ('invite_id' not in params or
                params['invite_id'] is None):
            raise ValueError("Missing the required parameter `invite_id` when calling `delete_invite_api_v1_organizations_invite_invite_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invite_id' in params:
            path_params['invite_id'] = params['invite_id']  # noqa: E501

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
            '/api/v1/organizations/invite/{invite_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invite_by_code_api_v1_organizations_invite_code_get(self, code, **kwargs):  # noqa: E501
        """Get Invite By Code  # noqa: E501

        Gets specific invite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invite_by_code_api_v1_organizations_invite_code_get(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: Invite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invite_by_code_api_v1_organizations_invite_code_get_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_invite_by_code_api_v1_organizations_invite_code_get_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def get_invite_by_code_api_v1_organizations_invite_code_get_with_http_info(self, code, **kwargs):  # noqa: E501
        """Get Invite By Code  # noqa: E501

        Gets specific invite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invite_by_code_api_v1_organizations_invite_code_get_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: Invite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invite_by_code_api_v1_organizations_invite_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_invite_by_code_api_v1_organizations_invite_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/invite/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Invite',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invites_api_v1_organizations_invite_get(self, **kwargs):  # noqa: E501
        """Get Invites  # noqa: E501

        Gets all invites of this users organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invites_api_v1_organizations_invite_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status:
        :return: list[Invite]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invites_api_v1_organizations_invite_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_invites_api_v1_organizations_invite_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_invites_api_v1_organizations_invite_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Invites  # noqa: E501

        Gets all invites of this users organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invites_api_v1_organizations_invite_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status:
        :return: list[Invite]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invites_api_v1_organizations_invite_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

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
            '/api/v1/organizations/invite', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Invite]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_loggedin_organization_api_v1_organizations_get(self, **kwargs):  # noqa: E501
        """Get Loggedin Organization  # noqa: E501

        Gets the logged in users organization details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loggedin_organization_api_v1_organizations_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_loggedin_organization_api_v1_organizations_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_loggedin_organization_api_v1_organizations_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_loggedin_organization_api_v1_organizations_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Loggedin Organization  # noqa: E501

        Gets the logged in users organization details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loggedin_organization_api_v1_organizations_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Organization
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
                    " to method get_loggedin_organization_api_v1_organizations_get" % key
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

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_org_creator_api_v1_organizations_creator_get(self, **kwargs):  # noqa: E501
        """Get Org Creator  # noqa: E501

        Gets all invites of this users organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_creator_api_v1_organizations_creator_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_org_creator_api_v1_organizations_creator_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_org_creator_api_v1_organizations_creator_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_org_creator_api_v1_organizations_creator_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Org Creator  # noqa: E501

        Gets all invites of this users organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_creator_api_v1_organizations_creator_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: User
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
                    " to method get_org_creator_api_v1_organizations_creator_get" % key
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

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/creator', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_org_users_api_v1_organizations_users_get(self, **kwargs):  # noqa: E501
        """Get Org Users  # noqa: E501

        Gets a list of all users in an organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_users_api_v1_organizations_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserInOrganization]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_org_users_api_v1_organizations_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_org_users_api_v1_organizations_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_org_users_api_v1_organizations_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Org Users  # noqa: E501

        Gets a list of all users in an organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_users_api_v1_organizations_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserInOrganization]
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
                    " to method get_org_users_api_v1_organizations_users_get" % key
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

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserInOrganization]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_roles_in_org_api_v1_organizations_roles_get(self, **kwargs):  # noqa: E501
        """Get Roles In Org  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_in_org_api_v1_organizations_roles_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_roles_in_org_api_v1_organizations_roles_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_in_org_api_v1_organizations_roles_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_roles_in_org_api_v1_organizations_roles_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Roles In Org  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_in_org_api_v1_organizations_roles_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
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
                    " to method get_roles_in_org_api_v1_organizations_roles_get" % key
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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/organizations/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)