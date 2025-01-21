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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.	If not, see <http://www.gnu.org/licenses/>.
#


from pydantic import BaseModel, Field


class ChangeParametersPayload(BaseModel):
	"""The payload of the message to change the parameters of the component."""

	is_competent_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is competent when calculate the autonomy value.")
	has_been_informed_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has been informed when calculate the autonomy value.")
	is_coerced_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is coerced when calculate the autonomy value.")
