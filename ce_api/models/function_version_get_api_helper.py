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


class FunctionVersionGetAPIHelper(object):
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
        'function_id': 'str',
        'udf_path': 'str',
        'message': 'str',
        'user_id': 'str',
        'id': 'str',
        'storage_path': 'str',
        'created_at': 'datetime',
        'file_contents': 'str'
    }

    attribute_map = {
        'function_id': 'function_id',
        'udf_path': 'udf_path',
        'message': 'message',
        'user_id': 'user_id',
        'id': 'id',
        'storage_path': 'storage_path',
        'created_at': 'created_at',
        'file_contents': 'file_contents'
    }

    def __init__(self, function_id=None, udf_path=None, message=None, user_id=None, id=None, storage_path=None, created_at=None, file_contents=None):  # noqa: E501
        """FunctionVersionGetAPIHelper - a model defined in Swagger"""  # noqa: E501
        self._function_id = None
        self._udf_path = None
        self._message = None
        self._user_id = None
        self._id = None
        self._storage_path = None
        self._created_at = None
        self._file_contents = None
        self.discriminator = None
        if function_id is not None:
            self.function_id = function_id
        if udf_path is not None:
            self.udf_path = udf_path
        if message is not None:
            self.message = message
        if user_id is not None:
            self.user_id = user_id
        if id is not None:
            self.id = id
        if storage_path is not None:
            self.storage_path = storage_path
        if created_at is not None:
            self.created_at = created_at
        if file_contents is not None:
            self.file_contents = file_contents

    @property
    def function_id(self):
        """Gets the function_id of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The function_id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """Sets the function_id of this FunctionVersionGetAPIHelper.


        :param function_id: The function_id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._function_id = function_id

    @property
    def udf_path(self):
        """Gets the udf_path of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The udf_path of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._udf_path

    @udf_path.setter
    def udf_path(self, udf_path):
        """Sets the udf_path of this FunctionVersionGetAPIHelper.


        :param udf_path: The udf_path of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._udf_path = udf_path

    @property
    def message(self):
        """Gets the message of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The message of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FunctionVersionGetAPIHelper.


        :param message: The message of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def user_id(self):
        """Gets the user_id of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The user_id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FunctionVersionGetAPIHelper.


        :param user_id: The user_id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FunctionVersionGetAPIHelper.


        :param id: The id of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def storage_path(self):
        """Gets the storage_path of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The storage_path of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this FunctionVersionGetAPIHelper.


        :param storage_path: The storage_path of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._storage_path = storage_path

    @property
    def created_at(self):
        """Gets the created_at of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The created_at of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FunctionVersionGetAPIHelper.


        :param created_at: The created_at of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def file_contents(self):
        """Gets the file_contents of this FunctionVersionGetAPIHelper.  # noqa: E501


        :return: The file_contents of this FunctionVersionGetAPIHelper.  # noqa: E501
        :rtype: str
        """
        return self._file_contents

    @file_contents.setter
    def file_contents(self, file_contents):
        """Sets the file_contents of this FunctionVersionGetAPIHelper.


        :param file_contents: The file_contents of this FunctionVersionGetAPIHelper.  # noqa: E501
        :type: str
        """

        self._file_contents = file_contents

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
        if issubclass(FunctionVersionGetAPIHelper, dict):
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
        if not isinstance(other, FunctionVersionGetAPIHelper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
