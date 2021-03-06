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

class Backend(object):
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
        'args': 'object',
        'provider_id': 'str',
        'backend_class': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'user_id': 'str',
        'organization_id': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'args': 'args',
        'provider_id': 'provider_id',
        'backend_class': 'backend_class',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'user_id': 'user_id',
        'organization_id': 'organization_id',
        'created_at': 'created_at'
    }

    def __init__(self, args=None, provider_id=None, backend_class=None, type=None, name=None, id=None, user_id=None, organization_id=None, created_at=None):  # noqa: E501
        """Backend - a model defined in Swagger"""  # noqa: E501
        self._args = None
        self._provider_id = None
        self._backend_class = None
        self._type = None
        self._name = None
        self._id = None
        self._user_id = None
        self._organization_id = None
        self._created_at = None
        self.discriminator = None
        if args is not None:
            self.args = args
        if provider_id is not None:
            self.provider_id = provider_id
        if backend_class is not None:
            self.backend_class = backend_class
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if organization_id is not None:
            self.organization_id = organization_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def args(self):
        """Gets the args of this Backend.  # noqa: E501


        :return: The args of this Backend.  # noqa: E501
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Backend.


        :param args: The args of this Backend.  # noqa: E501
        :type: object
        """

        self._args = args

    @property
    def provider_id(self):
        """Gets the provider_id of this Backend.  # noqa: E501


        :return: The provider_id of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Backend.


        :param provider_id: The provider_id of this Backend.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def backend_class(self):
        """Gets the backend_class of this Backend.  # noqa: E501


        :return: The backend_class of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._backend_class

    @backend_class.setter
    def backend_class(self, backend_class):
        """Sets the backend_class of this Backend.


        :param backend_class: The backend_class of this Backend.  # noqa: E501
        :type: str
        """

        self._backend_class = backend_class

    @property
    def type(self):
        """Gets the type of this Backend.  # noqa: E501


        :return: The type of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Backend.


        :param type: The type of this Backend.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Backend.  # noqa: E501


        :return: The name of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Backend.


        :param name: The name of this Backend.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this Backend.  # noqa: E501


        :return: The id of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Backend.


        :param id: The id of this Backend.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this Backend.  # noqa: E501


        :return: The user_id of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Backend.


        :param user_id: The user_id of this Backend.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def organization_id(self):
        """Gets the organization_id of this Backend.  # noqa: E501


        :return: The organization_id of this Backend.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Backend.


        :param organization_id: The organization_id of this Backend.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this Backend.  # noqa: E501


        :return: The created_at of this Backend.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Backend.


        :param created_at: The created_at of this Backend.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(Backend, dict):
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
        if not isinstance(other, Backend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
