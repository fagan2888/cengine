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


class FunctionInDB(object):
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
        'function_type': 'str',
        'id': 'str',
        'user_id': 'str',
        'organization_id': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'function_type': 'function_type',
        'id': 'id',
        'user_id': 'user_id',
        'organization_id': 'organization_id',
        'created_at': 'created_at'
    }

    def __init__(self, name=None, function_type=None, id=None, user_id=None, organization_id=None, created_at=None):  # noqa: E501
        """FunctionInDB - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._function_type = None
        self._id = None
        self._user_id = None
        self._organization_id = None
        self._created_at = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if function_type is not None:
            self.function_type = function_type
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if organization_id is not None:
            self.organization_id = organization_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def name(self):
        """Gets the name of this FunctionInDB.  # noqa: E501


        :return: The name of this FunctionInDB.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FunctionInDB.


        :param name: The name of this FunctionInDB.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def function_type(self):
        """Gets the function_type of this FunctionInDB.  # noqa: E501


        :return: The function_type of this FunctionInDB.  # noqa: E501
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this FunctionInDB.


        :param function_type: The function_type of this FunctionInDB.  # noqa: E501
        :type: str
        """

        self._function_type = function_type

    @property
    def id(self):
        """Gets the id of this FunctionInDB.  # noqa: E501


        :return: The id of this FunctionInDB.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FunctionInDB.


        :param id: The id of this FunctionInDB.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this FunctionInDB.  # noqa: E501


        :return: The user_id of this FunctionInDB.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FunctionInDB.


        :param user_id: The user_id of this FunctionInDB.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def organization_id(self):
        """Gets the organization_id of this FunctionInDB.  # noqa: E501


        :return: The organization_id of this FunctionInDB.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this FunctionInDB.


        :param organization_id: The organization_id of this FunctionInDB.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this FunctionInDB.  # noqa: E501


        :return: The created_at of this FunctionInDB.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FunctionInDB.


        :param created_at: The created_at of this FunctionInDB.  # noqa: E501
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
        if issubclass(FunctionInDB, dict):
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
        if not isinstance(other, FunctionInDB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other