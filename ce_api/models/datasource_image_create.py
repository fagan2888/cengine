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


class DatasourceImageCreate(object):
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
        'client_storage_path': 'str',
        'service_account': 'object'
    }

    attribute_map = {
        'name': 'name',
        'client_storage_path': 'client_storage_path',
        'service_account': 'service_account'
    }

    def __init__(self, name=None, client_storage_path=None, service_account=None):  # noqa: E501
        """DatasourceImageCreate - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._client_storage_path = None
        self._service_account = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if client_storage_path is not None:
            self.client_storage_path = client_storage_path
        if service_account is not None:
            self.service_account = service_account

    @property
    def name(self):
        """Gets the name of this DatasourceImageCreate.  # noqa: E501


        :return: The name of this DatasourceImageCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasourceImageCreate.


        :param name: The name of this DatasourceImageCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def client_storage_path(self):
        """Gets the client_storage_path of this DatasourceImageCreate.  # noqa: E501


        :return: The client_storage_path of this DatasourceImageCreate.  # noqa: E501
        :rtype: str
        """
        return self._client_storage_path

    @client_storage_path.setter
    def client_storage_path(self, client_storage_path):
        """Sets the client_storage_path of this DatasourceImageCreate.


        :param client_storage_path: The client_storage_path of this DatasourceImageCreate.  # noqa: E501
        :type: str
        """

        self._client_storage_path = client_storage_path

    @property
    def service_account(self):
        """Gets the service_account of this DatasourceImageCreate.  # noqa: E501


        :return: The service_account of this DatasourceImageCreate.  # noqa: E501
        :rtype: object
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this DatasourceImageCreate.


        :param service_account: The service_account of this DatasourceImageCreate.  # noqa: E501
        :type: object
        """

        self._service_account = service_account

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
        if issubclass(DatasourceImageCreate, dict):
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
        if not isinstance(other, DatasourceImageCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
