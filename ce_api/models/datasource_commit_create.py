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

class DatasourceCommitCreate(object):
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
        'message': 'str',
        'used_schema': 'object',
        'workers': 'int',
        'cpus_per_worker': 'int',
        'orchestration_backend': 'str',
        'orchestration_args': 'object',
        'processing_backend': 'str',
        'processing_args': 'object'
    }

    attribute_map = {
        'message': 'message',
        'used_schema': 'used_schema',
        'workers': 'workers',
        'cpus_per_worker': 'cpus_per_worker',
        'orchestration_backend': 'orchestration_backend',
        'orchestration_args': 'orchestration_args',
        'processing_backend': 'processing_backend',
        'processing_args': 'processing_args'
    }

    def __init__(self, message=None, used_schema=None, workers=None, cpus_per_worker=None, orchestration_backend=None, orchestration_args=None, processing_backend=None, processing_args=None):  # noqa: E501
        """DatasourceCommitCreate - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._used_schema = None
        self._workers = None
        self._cpus_per_worker = None
        self._orchestration_backend = None
        self._orchestration_args = None
        self._processing_backend = None
        self._processing_args = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if used_schema is not None:
            self.used_schema = used_schema
        if workers is not None:
            self.workers = workers
        if cpus_per_worker is not None:
            self.cpus_per_worker = cpus_per_worker
        if orchestration_backend is not None:
            self.orchestration_backend = orchestration_backend
        if orchestration_args is not None:
            self.orchestration_args = orchestration_args
        if processing_backend is not None:
            self.processing_backend = processing_backend
        if processing_args is not None:
            self.processing_args = processing_args

    @property
    def message(self):
        """Gets the message of this DatasourceCommitCreate.  # noqa: E501


        :return: The message of this DatasourceCommitCreate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DatasourceCommitCreate.


        :param message: The message of this DatasourceCommitCreate.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def used_schema(self):
        """Gets the used_schema of this DatasourceCommitCreate.  # noqa: E501


        :return: The used_schema of this DatasourceCommitCreate.  # noqa: E501
        :rtype: object
        """
        return self._used_schema

    @used_schema.setter
    def used_schema(self, used_schema):
        """Sets the used_schema of this DatasourceCommitCreate.


        :param used_schema: The used_schema of this DatasourceCommitCreate.  # noqa: E501
        :type: object
        """

        self._used_schema = used_schema

    @property
    def workers(self):
        """Gets the workers of this DatasourceCommitCreate.  # noqa: E501


        :return: The workers of this DatasourceCommitCreate.  # noqa: E501
        :rtype: int
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        """Sets the workers of this DatasourceCommitCreate.


        :param workers: The workers of this DatasourceCommitCreate.  # noqa: E501
        :type: int
        """

        self._workers = workers

    @property
    def cpus_per_worker(self):
        """Gets the cpus_per_worker of this DatasourceCommitCreate.  # noqa: E501


        :return: The cpus_per_worker of this DatasourceCommitCreate.  # noqa: E501
        :rtype: int
        """
        return self._cpus_per_worker

    @cpus_per_worker.setter
    def cpus_per_worker(self, cpus_per_worker):
        """Sets the cpus_per_worker of this DatasourceCommitCreate.


        :param cpus_per_worker: The cpus_per_worker of this DatasourceCommitCreate.  # noqa: E501
        :type: int
        """

        self._cpus_per_worker = cpus_per_worker

    @property
    def orchestration_backend(self):
        """Gets the orchestration_backend of this DatasourceCommitCreate.  # noqa: E501


        :return: The orchestration_backend of this DatasourceCommitCreate.  # noqa: E501
        :rtype: str
        """
        return self._orchestration_backend

    @orchestration_backend.setter
    def orchestration_backend(self, orchestration_backend):
        """Sets the orchestration_backend of this DatasourceCommitCreate.


        :param orchestration_backend: The orchestration_backend of this DatasourceCommitCreate.  # noqa: E501
        :type: str
        """

        self._orchestration_backend = orchestration_backend

    @property
    def orchestration_args(self):
        """Gets the orchestration_args of this DatasourceCommitCreate.  # noqa: E501


        :return: The orchestration_args of this DatasourceCommitCreate.  # noqa: E501
        :rtype: object
        """
        return self._orchestration_args

    @orchestration_args.setter
    def orchestration_args(self, orchestration_args):
        """Sets the orchestration_args of this DatasourceCommitCreate.


        :param orchestration_args: The orchestration_args of this DatasourceCommitCreate.  # noqa: E501
        :type: object
        """

        self._orchestration_args = orchestration_args

    @property
    def processing_backend(self):
        """Gets the processing_backend of this DatasourceCommitCreate.  # noqa: E501


        :return: The processing_backend of this DatasourceCommitCreate.  # noqa: E501
        :rtype: str
        """
        return self._processing_backend

    @processing_backend.setter
    def processing_backend(self, processing_backend):
        """Sets the processing_backend of this DatasourceCommitCreate.


        :param processing_backend: The processing_backend of this DatasourceCommitCreate.  # noqa: E501
        :type: str
        """

        self._processing_backend = processing_backend

    @property
    def processing_args(self):
        """Gets the processing_args of this DatasourceCommitCreate.  # noqa: E501


        :return: The processing_args of this DatasourceCommitCreate.  # noqa: E501
        :rtype: object
        """
        return self._processing_args

    @processing_args.setter
    def processing_args(self, processing_args):
        """Sets the processing_args of this DatasourceCommitCreate.


        :param processing_args: The processing_args of this DatasourceCommitCreate.  # noqa: E501
        :type: object
        """

        self._processing_args = processing_args

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
        if issubclass(DatasourceCommitCreate, dict):
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
        if not isinstance(other, DatasourceCommitCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
