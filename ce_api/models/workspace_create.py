# coding: utf-8

"""
    maiot Core Engine API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkspaceCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'organization_id': 'str',
        'user_ids': 'list[str]',
        'provider_id': 'str',
        'metadatastore_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'organization_id': 'organization_id',
        'user_ids': 'user_ids',
        'provider_id': 'provider_id',
        'metadatastore_id': 'metadatastore_id'
    }

    def __init__(self, name=None, organization_id=None, user_ids=None, provider_id=None, metadatastore_id=None):  # noqa: E501
        """WorkspaceCreate - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._organization_id = None
        self._user_ids = None
        self._provider_id = None
        self._metadatastore_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if user_ids is not None:
            self.user_ids = user_ids
        if provider_id is not None:
            self.provider_id = provider_id
        if metadatastore_id is not None:
            self.metadatastore_id = metadatastore_id

    @property
    def name(self):
        """Gets the name of this WorkspaceCreate.  # noqa: E501


        :return: The name of this WorkspaceCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceCreate.


        :param name: The name of this WorkspaceCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this WorkspaceCreate.  # noqa: E501


        :return: The organization_id of this WorkspaceCreate.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this WorkspaceCreate.


        :param organization_id: The organization_id of this WorkspaceCreate.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def user_ids(self):
        """Gets the user_ids of this WorkspaceCreate.  # noqa: E501


        :return: The user_ids of this WorkspaceCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this WorkspaceCreate.


        :param user_ids: The user_ids of this WorkspaceCreate.  # noqa: E501
        :type: list[str]
        """

        self._user_ids = user_ids

    @property
    def provider_id(self):
        """Gets the provider_id of this WorkspaceCreate.  # noqa: E501


        :return: The provider_id of this WorkspaceCreate.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this WorkspaceCreate.


        :param provider_id: The provider_id of this WorkspaceCreate.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def metadatastore_id(self):
        """Gets the metadatastore_id of this WorkspaceCreate.  # noqa: E501


        :return: The metadatastore_id of this WorkspaceCreate.  # noqa: E501
        :rtype: str
        """
        return self._metadatastore_id

    @metadatastore_id.setter
    def metadatastore_id(self, metadatastore_id):
        """Sets the metadatastore_id of this WorkspaceCreate.


        :param metadatastore_id: The metadatastore_id of this WorkspaceCreate.  # noqa: E501
        :type: str
        """

        self._metadatastore_id = metadatastore_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WorkspaceCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other