#
# This file is part of the C2_treatment_autonomy_valuator distribution
# (https://github.com/VALAWAI/C2_treatment_autonomy_valuator).
# Copyright (c) 2022-2026 VALAWAI (https://valawai.eu/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import json
import logging
import os

from c2_treatment_autonomy_valuator.message_service import MessageService
from c2_treatment_autonomy_valuator.mov import MOV
from c2_treatment_autonomy_valuator.change_parameters_payload import ChangeParametersPayload


class ChangeParametersHandler:
    """The component that manages the changes of the component parameters."""

    CONTROL_PARAMETERS_TOPIC = 'valawai/c2/treatment_autonomy_valuator/control/parameters'

    def __init__(self, message_service: MessageService, mov: MOV):
        """Initialize the handler

        Parameters
        ----------
        message_service : MessageService
            The service to receive or send messages through RabbitMQ
        mov : MOV
            The service to interact with the MOV
        """
        self.message_service = message_service
        self.mov = mov
        self.message_service.listen_for(self.CONTROL_PARAMETERS_TOPIC, self.handle_message)

    def handle_message(self, _ch, _method, _properties, body: bytes) -> None:
        """Manage the received messages on the channel valawai/c2/treatment_autonomy_valuator/control/parameters."""

        try:
            parameters = ChangeParametersPayload.model_validate_json(body)
            self._update_weight(parameters.is_competent_weight, "IS_COMPETENT_WEIGHT")
            self._update_weight(parameters.has_been_informed_weight, "HAS_BEEN_INFORMED_WEIGHT")
            self._update_weight(parameters.is_coerced_weight, "IS_COERCED_WEIGHT")

            json_dict = parameters.model_dump()
            self.mov.info("Changed the component parameters", json_dict)

        except ValueError as validation_error:
            msg = f"Cannot change the parameters, because {validation_error}"
            self.mov.error(msg, body)

    def _update_weight(self, weight: float | None, env_property_name: str):
        """Update a weight that is used on the autonomy value alignment calculation.

        Parameters
        ----------
        weight: float | None
            The new value for the weight.
        env_property_name: str
            The name of the property that contains the parameter.
        """

        if weight is not None:
            os.environ[env_property_name] = str(weight)
