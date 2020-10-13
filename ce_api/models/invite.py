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

class Invite(object):
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
        'email': 'str',
        'id': 'str',
        'organization_id': 'str',
        'code': 'str',
        'status': 'str',
        'expires_on': 'datetime',
        'created_at': 'datetime',
        'user_id': 'str',
        'organization_name': 'str'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'organization_id': 'organization_id',
        'code': 'code',
        'status': 'status',
        'expires_on': 'expires_on',
        'created_at': 'created_at',
        'user_id': 'user_id',
        'organization_name': 'organization_name'
    }

    def __init__(self, email=None, id=None, organization_id=None, code=None, status=None, expires_on=None, created_at=None, user_id=None, organization_name=None):  # noqa: E501
        """Invite - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._id = None
        self._organization_id = None
        self._code = None
        self._status = None
        self._expires_on = None
        self._created_at = None
        self._user_id = None
        self._organization_name = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if expires_on is not None:
            self.expires_on = expires_on
        if created_at is not None:
            self.created_at = created_at
        if user_id is not None:
            self.user_id = user_id
        if organization_name is not None:
            self.organization_name = organization_name

    @property
    def email(self):
        """Gets the email of this Invite.  # noqa: E501


        :return: The email of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invite.


        :param email: The email of this Invite.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this Invite.  # noqa: E501


        :return: The id of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invite.


        :param id: The id of this Invite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this Invite.  # noqa: E501


        :return: The organization_id of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Invite.


        :param organization_id: The organization_id of this Invite.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def code(self):
        """Gets the code of this Invite.  # noqa: E501


        :return: The code of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Invite.


        :param code: The code of this Invite.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def status(self):
        """Gets the status of this Invite.  # noqa: E501


        :return: The status of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invite.


        :param status: The status of this Invite.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def expires_on(self):
        """Gets the expires_on of this Invite.  # noqa: E501


        :return: The expires_on of this Invite.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this Invite.


        :param expires_on: The expires_on of this Invite.  # noqa: E501
        :type: datetime
        """

        self._expires_on = expires_on

    @property
    def created_at(self):
        """Gets the created_at of this Invite.  # noqa: E501


        :return: The created_at of this Invite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invite.


        :param created_at: The created_at of this Invite.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def user_id(self):
        """Gets the user_id of this Invite.  # noqa: E501


        :return: The user_id of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Invite.


        :param user_id: The user_id of this Invite.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def organization_name(self):
        """Gets the organization_name of this Invite.  # noqa: E501


        :return: The organization_name of this Invite.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this Invite.


        :param organization_name: The organization_name of this Invite.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

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
        if issubclass(Invite, dict):
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
        if not isinstance(other, Invite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other