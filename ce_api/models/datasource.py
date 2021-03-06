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

class Datasource(object):
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
        'args': 'object',
        'type': 'str',
        'source': 'str',
        'provider_id': 'str',
        'id': 'str',
        'created_at': 'datetime',
        'organization_id': 'str',
        'origin_pipeline_id': 'str',
        'metadatastore_id': 'str',
        'datasource_commits': 'list[DatasourceCommitInDB]'
    }

    attribute_map = {
        'name': 'name',
        'args': 'args',
        'type': 'type',
        'source': 'source',
        'provider_id': 'provider_id',
        'id': 'id',
        'created_at': 'created_at',
        'organization_id': 'organization_id',
        'origin_pipeline_id': 'origin_pipeline_id',
        'metadatastore_id': 'metadatastore_id',
        'datasource_commits': 'datasource_commits'
    }

    def __init__(self, name=None, args=None, type=None, source=None, provider_id=None, id=None, created_at=None, organization_id=None, origin_pipeline_id=None, metadatastore_id=None, datasource_commits=None):  # noqa: E501
        """Datasource - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._args = None
        self._type = None
        self._source = None
        self._provider_id = None
        self._id = None
        self._created_at = None
        self._organization_id = None
        self._origin_pipeline_id = None
        self._metadatastore_id = None
        self._datasource_commits = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if args is not None:
            self.args = args
        if type is not None:
            self.type = type
        if source is not None:
            self.source = source
        if provider_id is not None:
            self.provider_id = provider_id
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if organization_id is not None:
            self.organization_id = organization_id
        if origin_pipeline_id is not None:
            self.origin_pipeline_id = origin_pipeline_id
        if metadatastore_id is not None:
            self.metadatastore_id = metadatastore_id
        if datasource_commits is not None:
            self.datasource_commits = datasource_commits

    @property
    def name(self):
        """Gets the name of this Datasource.  # noqa: E501


        :return: The name of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datasource.


        :param name: The name of this Datasource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def args(self):
        """Gets the args of this Datasource.  # noqa: E501


        :return: The args of this Datasource.  # noqa: E501
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Datasource.


        :param args: The args of this Datasource.  # noqa: E501
        :type: object
        """

        self._args = args

    @property
    def type(self):
        """Gets the type of this Datasource.  # noqa: E501


        :return: The type of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datasource.


        :param type: The type of this Datasource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def source(self):
        """Gets the source of this Datasource.  # noqa: E501


        :return: The source of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Datasource.


        :param source: The source of this Datasource.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def provider_id(self):
        """Gets the provider_id of this Datasource.  # noqa: E501


        :return: The provider_id of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Datasource.


        :param provider_id: The provider_id of this Datasource.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def id(self):
        """Gets the id of this Datasource.  # noqa: E501


        :return: The id of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datasource.


        :param id: The id of this Datasource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Datasource.  # noqa: E501


        :return: The created_at of this Datasource.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datasource.


        :param created_at: The created_at of this Datasource.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def organization_id(self):
        """Gets the organization_id of this Datasource.  # noqa: E501


        :return: The organization_id of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Datasource.


        :param organization_id: The organization_id of this Datasource.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def origin_pipeline_id(self):
        """Gets the origin_pipeline_id of this Datasource.  # noqa: E501


        :return: The origin_pipeline_id of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._origin_pipeline_id

    @origin_pipeline_id.setter
    def origin_pipeline_id(self, origin_pipeline_id):
        """Sets the origin_pipeline_id of this Datasource.


        :param origin_pipeline_id: The origin_pipeline_id of this Datasource.  # noqa: E501
        :type: str
        """

        self._origin_pipeline_id = origin_pipeline_id

    @property
    def metadatastore_id(self):
        """Gets the metadatastore_id of this Datasource.  # noqa: E501


        :return: The metadatastore_id of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._metadatastore_id

    @metadatastore_id.setter
    def metadatastore_id(self, metadatastore_id):
        """Sets the metadatastore_id of this Datasource.


        :param metadatastore_id: The metadatastore_id of this Datasource.  # noqa: E501
        :type: str
        """

        self._metadatastore_id = metadatastore_id

    @property
    def datasource_commits(self):
        """Gets the datasource_commits of this Datasource.  # noqa: E501


        :return: The datasource_commits of this Datasource.  # noqa: E501
        :rtype: list[DatasourceCommitInDB]
        """
        return self._datasource_commits

    @datasource_commits.setter
    def datasource_commits(self, datasource_commits):
        """Sets the datasource_commits of this Datasource.


        :param datasource_commits: The datasource_commits of this Datasource.  # noqa: E501
        :type: list[DatasourceCommitInDB]
        """

        self._datasource_commits = datasource_commits

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
        if issubclass(Datasource, dict):
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
        if not isinstance(other, Datasource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
