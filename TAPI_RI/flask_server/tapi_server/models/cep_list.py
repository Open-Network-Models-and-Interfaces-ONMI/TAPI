# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connection_end_point import ConnectionEndPoint  # noqa: F401,E501
from tapi_server import util


class CepList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, connection_end_point: List[ConnectionEndPoint]=None):  # noqa: E501
        """CepList - a model defined in Swagger

        :param connection_end_point: The connection_end_point of this CepList.  # noqa: E501
        :type connection_end_point: List[ConnectionEndPoint]
        """
        self.swagger_types = {
            'connection_end_point': List[ConnectionEndPoint]
        }

        self.attribute_map = {
            'connection_end_point': 'connection-end-point'
        }

        self._connection_end_point = connection_end_point

    @classmethod
    def from_dict(cls, dikt) -> 'CepList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The cep-list of this CepList.  # noqa: E501
        :rtype: CepList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def connection_end_point(self) -> List[ConnectionEndPoint]:
        """Gets the connection_end_point of this CepList.


        :return: The connection_end_point of this CepList.
        :rtype: List[ConnectionEndPoint]
        """
        return self._connection_end_point

    @connection_end_point.setter
    def connection_end_point(self, connection_end_point: List[ConnectionEndPoint]):
        """Sets the connection_end_point of this CepList.


        :param connection_end_point: The connection_end_point of this CepList.
        :type connection_end_point: List[ConnectionEndPoint]
        """

        self._connection_end_point = connection_end_point
