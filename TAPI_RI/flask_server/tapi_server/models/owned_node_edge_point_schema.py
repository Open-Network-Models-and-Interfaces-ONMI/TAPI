# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connection_end_point import ConnectionEndPoint  # noqa: F401,E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.node_edge_point import NodeEdgePoint  # noqa: F401,E501
from tapi_server import util


class OwnedNodeEdgePointSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, administrative_state: str=None, operational_state: str=None, lifecycle_state: str=None, termination_direction: str=None, termination_state: str=None, layer_protocol_name: str=None, aggregated_node_edge_point: List[str]=None, mapped_service_interface_point: List[str]=None, link_port_direction: str=None, link_port_role: str=None, owned_node_edge_point_uuid: str=None, connection_end_point: List[ConnectionEndPoint]=None):  # noqa: E501
        """OwnedNodeEdgePointSchema - a model defined in Swagger

        :param uuid: The uuid of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type uuid: str
        :param name: The name of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type name: List[NameAndValue]
        :param administrative_state: The administrative_state of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type administrative_state: str
        :param operational_state: The operational_state of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type operational_state: str
        :param lifecycle_state: The lifecycle_state of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type lifecycle_state: str
        :param termination_direction: The termination_direction of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type termination_direction: str
        :param termination_state: The termination_state of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type termination_state: str
        :param layer_protocol_name: The layer_protocol_name of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type layer_protocol_name: str
        :param aggregated_node_edge_point: The aggregated_node_edge_point of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type aggregated_node_edge_point: List[str]
        :param mapped_service_interface_point: The mapped_service_interface_point of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type mapped_service_interface_point: List[str]
        :param link_port_direction: The link_port_direction of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type link_port_direction: str
        :param link_port_role: The link_port_role of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type link_port_role: str
        :param owned_node_edge_point_uuid: The owned_node_edge_point_uuid of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type owned_node_edge_point_uuid: str
        :param connection_end_point: The connection_end_point of this OwnedNodeEdgePointSchema.  # noqa: E501
        :type connection_end_point: List[ConnectionEndPoint]
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'administrative_state': str,
            'operational_state': str,
            'lifecycle_state': str,
            'termination_direction': str,
            'termination_state': str,
            'layer_protocol_name': str,
            'aggregated_node_edge_point': List[str],
            'mapped_service_interface_point': List[str],
            'link_port_direction': str,
            'link_port_role': str,
            'owned_node_edge_point_uuid': str,
            'connection_end_point': List[ConnectionEndPoint]
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'administrative_state': 'administrative-state',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'termination_direction': 'termination-direction',
            'termination_state': 'termination-state',
            'layer_protocol_name': 'layer-protocol-name',
            'aggregated_node_edge_point': 'aggregated-node-edge-point',
            'mapped_service_interface_point': 'mapped-service-interface-point',
            'link_port_direction': 'link-port-direction',
            'link_port_role': 'link-port-role',
            'owned_node_edge_point_uuid': 'owned-node-edge-point_uuid',
            'connection_end_point': 'connection-end-point'
        }

        self._uuid = uuid
        self._name = name
        self._administrative_state = administrative_state
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._termination_direction = termination_direction
        self._termination_state = termination_state
        self._layer_protocol_name = layer_protocol_name
        self._aggregated_node_edge_point = aggregated_node_edge_point
        self._mapped_service_interface_point = mapped_service_interface_point
        self._link_port_direction = link_port_direction
        self._link_port_role = link_port_role
        self._owned_node_edge_point_uuid = owned_node_edge_point_uuid
        self._connection_end_point = connection_end_point

    @classmethod
    def from_dict(cls, dikt) -> 'OwnedNodeEdgePointSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The owned-node-edge-point_schema of this OwnedNodeEdgePointSchema.  # noqa: E501
        :rtype: OwnedNodeEdgePointSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this OwnedNodeEdgePointSchema.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this OwnedNodeEdgePointSchema.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this OwnedNodeEdgePointSchema.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this OwnedNodeEdgePointSchema.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this OwnedNodeEdgePointSchema.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this OwnedNodeEdgePointSchema.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this OwnedNodeEdgePointSchema.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def administrative_state(self) -> str:
        """Gets the administrative_state of this OwnedNodeEdgePointSchema.


        :return: The administrative_state of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state: str):
        """Sets the administrative_state of this OwnedNodeEdgePointSchema.


        :param administrative_state: The administrative_state of this OwnedNodeEdgePointSchema.
        :type administrative_state: str
        """
        allowed_values = ["LOCKED", "UNLOCKED"]  # noqa: E501
        if administrative_state not in allowed_values:
            raise ValueError(
                "Invalid value for `administrative_state` ({0}), must be one of {1}"
                .format(administrative_state, allowed_values)
            )

        self._administrative_state = administrative_state

    @property
    def operational_state(self) -> str:
        """Gets the operational_state of this OwnedNodeEdgePointSchema.


        :return: The operational_state of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state: str):
        """Sets the operational_state of this OwnedNodeEdgePointSchema.


        :param operational_state: The operational_state of this OwnedNodeEdgePointSchema.
        :type operational_state: str
        """
        allowed_values = ["DISABLED", "ENABLED"]  # noqa: E501
        if operational_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operational_state` ({0}), must be one of {1}"
                .format(operational_state, allowed_values)
            )

        self._operational_state = operational_state

    @property
    def lifecycle_state(self) -> str:
        """Gets the lifecycle_state of this OwnedNodeEdgePointSchema.


        :return: The lifecycle_state of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state: str):
        """Sets the lifecycle_state of this OwnedNodeEdgePointSchema.


        :param lifecycle_state: The lifecycle_state of this OwnedNodeEdgePointSchema.
        :type lifecycle_state: str
        """
        allowed_values = ["PLANNED", "POTENTIAL_AVAILABLE", "POTENTIAL_BUSY", "INSTALLED", "PENDING_REMOVAL"]  # noqa: E501
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state` ({0}), must be one of {1}"
                .format(lifecycle_state, allowed_values)
            )

        self._lifecycle_state = lifecycle_state

    @property
    def termination_direction(self) -> str:
        """Gets the termination_direction of this OwnedNodeEdgePointSchema.

        The overall directionality of the LP.  - A BIDIRECTIONAL LP will have some SINK and/or SOURCE flowss. - A SINK LP can only contain elements with SINK flows or CONTRA_DIRECTION_SOURCE flows - A SOURCE LP can only contain SOURCE flows or CONTRA_DIRECTION_SINK flows  # noqa: E501

        :return: The termination_direction of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._termination_direction

    @termination_direction.setter
    def termination_direction(self, termination_direction: str):
        """Sets the termination_direction of this OwnedNodeEdgePointSchema.

        The overall directionality of the LP.  - A BIDIRECTIONAL LP will have some SINK and/or SOURCE flowss. - A SINK LP can only contain elements with SINK flows or CONTRA_DIRECTION_SOURCE flows - A SOURCE LP can only contain SOURCE flows or CONTRA_DIRECTION_SINK flows  # noqa: E501

        :param termination_direction: The termination_direction of this OwnedNodeEdgePointSchema.
        :type termination_direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "SINK", "SOURCE", "UNDEFINED_OR_UNKNOWN"]  # noqa: E501
        if termination_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `termination_direction` ({0}), must be one of {1}"
                .format(termination_direction, allowed_values)
            )

        self._termination_direction = termination_direction

    @property
    def termination_state(self) -> str:
        """Gets the termination_state of this OwnedNodeEdgePointSchema.

        Indicates whether the layer is terminated and if so how.  # noqa: E501

        :return: The termination_state of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._termination_state

    @termination_state.setter
    def termination_state(self, termination_state: str):
        """Sets the termination_state of this OwnedNodeEdgePointSchema.

        Indicates whether the layer is terminated and if so how.  # noqa: E501

        :param termination_state: The termination_state of this OwnedNodeEdgePointSchema.
        :type termination_state: str
        """
        allowed_values = ["LP_CAN_NEVER_TERMINATE", "LT_NOT_TERMINATED", "TERMINATED_SERVER_TO_CLIENT_FLOW", "TERMINATED_CLIENT_TO_SERVER_FLOW", "TERMINATED_BIDIRECTIONAL", "LT_PERMENANTLY_TERMINATED", "TERMINATION_STATE_UNKNOWN"]  # noqa: E501
        if termination_state not in allowed_values:
            raise ValueError(
                "Invalid value for `termination_state` ({0}), must be one of {1}"
                .format(termination_state, allowed_values)
            )

        self._termination_state = termination_state

    @property
    def layer_protocol_name(self) -> str:
        """Gets the layer_protocol_name of this OwnedNodeEdgePointSchema.


        :return: The layer_protocol_name of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: str):
        """Sets the layer_protocol_name of this OwnedNodeEdgePointSchema.


        :param layer_protocol_name: The layer_protocol_name of this OwnedNodeEdgePointSchema.
        :type layer_protocol_name: str
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY"]  # noqa: E501
        if layer_protocol_name not in allowed_values:
            raise ValueError(
                "Invalid value for `layer_protocol_name` ({0}), must be one of {1}"
                .format(layer_protocol_name, allowed_values)
            )

        self._layer_protocol_name = layer_protocol_name

    @property
    def aggregated_node_edge_point(self) -> List[str]:
        """Gets the aggregated_node_edge_point of this OwnedNodeEdgePointSchema.


        :return: The aggregated_node_edge_point of this OwnedNodeEdgePointSchema.
        :rtype: List[str]
        """
        return self._aggregated_node_edge_point

    @aggregated_node_edge_point.setter
    def aggregated_node_edge_point(self, aggregated_node_edge_point: List[str]):
        """Sets the aggregated_node_edge_point of this OwnedNodeEdgePointSchema.


        :param aggregated_node_edge_point: The aggregated_node_edge_point of this OwnedNodeEdgePointSchema.
        :type aggregated_node_edge_point: List[str]
        """

        self._aggregated_node_edge_point = aggregated_node_edge_point

    @property
    def mapped_service_interface_point(self) -> List[str]:
        """Gets the mapped_service_interface_point of this OwnedNodeEdgePointSchema.


        :return: The mapped_service_interface_point of this OwnedNodeEdgePointSchema.
        :rtype: List[str]
        """
        return self._mapped_service_interface_point

    @mapped_service_interface_point.setter
    def mapped_service_interface_point(self, mapped_service_interface_point: List[str]):
        """Sets the mapped_service_interface_point of this OwnedNodeEdgePointSchema.


        :param mapped_service_interface_point: The mapped_service_interface_point of this OwnedNodeEdgePointSchema.
        :type mapped_service_interface_point: List[str]
        """

        self._mapped_service_interface_point = mapped_service_interface_point

    @property
    def link_port_direction(self) -> str:
        """Gets the link_port_direction of this OwnedNodeEdgePointSchema.

        The orientation of defined flow at the LinkEnd.  # noqa: E501

        :return: The link_port_direction of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._link_port_direction

    @link_port_direction.setter
    def link_port_direction(self, link_port_direction: str):
        """Sets the link_port_direction of this OwnedNodeEdgePointSchema.

        The orientation of defined flow at the LinkEnd.  # noqa: E501

        :param link_port_direction: The link_port_direction of this OwnedNodeEdgePointSchema.
        :type link_port_direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "INPUT", "OUTPUT", "UNIDENTIFIED_OR_UNKNOWN"]  # noqa: E501
        if link_port_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `link_port_direction` ({0}), must be one of {1}"
                .format(link_port_direction, allowed_values)
            )

        self._link_port_direction = link_port_direction

    @property
    def link_port_role(self) -> str:
        """Gets the link_port_role of this OwnedNodeEdgePointSchema.

        Each LinkEnd of the Link has a role (e.g., symmetric, hub, spoke, leaf, root)  in the context of the Link with respect to the Link function.   # noqa: E501

        :return: The link_port_role of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._link_port_role

    @link_port_role.setter
    def link_port_role(self, link_port_role: str):
        """Sets the link_port_role of this OwnedNodeEdgePointSchema.

        Each LinkEnd of the Link has a role (e.g., symmetric, hub, spoke, leaf, root)  in the context of the Link with respect to the Link function.   # noqa: E501

        :param link_port_role: The link_port_role of this OwnedNodeEdgePointSchema.
        :type link_port_role: str
        """
        allowed_values = ["SYMMETRIC", "ROOT", "LEAF", "TRUNK", "UNKNOWN"]  # noqa: E501
        if link_port_role not in allowed_values:
            raise ValueError(
                "Invalid value for `link_port_role` ({0}), must be one of {1}"
                .format(link_port_role, allowed_values)
            )

        self._link_port_role = link_port_role

    @property
    def owned_node_edge_point_uuid(self) -> str:
        """Gets the owned_node_edge_point_uuid of this OwnedNodeEdgePointSchema.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The owned_node_edge_point_uuid of this OwnedNodeEdgePointSchema.
        :rtype: str
        """
        return self._owned_node_edge_point_uuid

    @owned_node_edge_point_uuid.setter
    def owned_node_edge_point_uuid(self, owned_node_edge_point_uuid: str):
        """Sets the owned_node_edge_point_uuid of this OwnedNodeEdgePointSchema.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param owned_node_edge_point_uuid: The owned_node_edge_point_uuid of this OwnedNodeEdgePointSchema.
        :type owned_node_edge_point_uuid: str
        """

        self._owned_node_edge_point_uuid = owned_node_edge_point_uuid

    @property
    def connection_end_point(self) -> List[ConnectionEndPoint]:
        """Gets the connection_end_point of this OwnedNodeEdgePointSchema.


        :return: The connection_end_point of this OwnedNodeEdgePointSchema.
        :rtype: List[ConnectionEndPoint]
        """
        return self._connection_end_point

    @connection_end_point.setter
    def connection_end_point(self, connection_end_point: List[ConnectionEndPoint]):
        """Sets the connection_end_point of this OwnedNodeEdgePointSchema.


        :param connection_end_point: The connection_end_point of this OwnedNodeEdgePointSchema.
        :type connection_end_point: List[ConnectionEndPoint]
        """

        self._connection_end_point = connection_end_point
