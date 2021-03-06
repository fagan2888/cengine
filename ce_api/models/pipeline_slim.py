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

class PipelineSlim(object):
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
        'id': 'str',
        'name': 'str',
        'workspace_id': 'str',
        'created_at': 'datetime',
        'organization_id': 'str',
        'user_id': 'str',
        'pipeline_runs': 'list[PipelineRunSlim]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'created_at': 'created_at',
        'organization_id': 'organization_id',
        'user_id': 'user_id',
        'pipeline_runs': 'pipeline_runs'
    }

    def __init__(self, id=None, name=None, workspace_id=None, created_at=None, organization_id=None, user_id=None, pipeline_runs=None):  # noqa: E501
        """PipelineSlim - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._workspace_id = None
        self._created_at = None
        self._organization_id = None
        self._user_id = None
        self._pipeline_runs = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if created_at is not None:
            self.created_at = created_at
        if organization_id is not None:
            self.organization_id = organization_id
        if user_id is not None:
            self.user_id = user_id
        if pipeline_runs is not None:
            self.pipeline_runs = pipeline_runs

    @property
    def id(self):
        """Gets the id of this PipelineSlim.  # noqa: E501


        :return: The id of this PipelineSlim.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineSlim.


        :param id: The id of this PipelineSlim.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PipelineSlim.  # noqa: E501


        :return: The name of this PipelineSlim.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineSlim.


        :param name: The name of this PipelineSlim.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this PipelineSlim.  # noqa: E501


        :return: The workspace_id of this PipelineSlim.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this PipelineSlim.


        :param workspace_id: The workspace_id of this PipelineSlim.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def created_at(self):
        """Gets the created_at of this PipelineSlim.  # noqa: E501


        :return: The created_at of this PipelineSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PipelineSlim.


        :param created_at: The created_at of this PipelineSlim.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def organization_id(self):
        """Gets the organization_id of this PipelineSlim.  # noqa: E501


        :return: The organization_id of this PipelineSlim.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PipelineSlim.


        :param organization_id: The organization_id of this PipelineSlim.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this PipelineSlim.  # noqa: E501


        :return: The user_id of this PipelineSlim.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PipelineSlim.


        :param user_id: The user_id of this PipelineSlim.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def pipeline_runs(self):
        """Gets the pipeline_runs of this PipelineSlim.  # noqa: E501


        :return: The pipeline_runs of this PipelineSlim.  # noqa: E501
        :rtype: list[PipelineRunSlim]
        """
        return self._pipeline_runs

    @pipeline_runs.setter
    def pipeline_runs(self, pipeline_runs):
        """Sets the pipeline_runs of this PipelineSlim.


        :param pipeline_runs: The pipeline_runs of this PipelineSlim.  # noqa: E501
        :type: list[PipelineRunSlim]
        """

        self._pipeline_runs = pipeline_runs

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
        if issubclass(PipelineSlim, dict):
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
        if not isinstance(other, PipelineSlim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
