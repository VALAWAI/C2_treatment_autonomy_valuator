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

import os

from c2_treatment_autonomy_valuator.treatment_payload import TreatmentPayload


class AutonomyValuator:
    """The component that obtains the autonomy value from a patient treatment."""

    def __init__(self,
                 is_competent_weight: float = float(os.getenv('IS_COMPETENT_WEIGHT', "0.25")),
                 has_been_informed_weight: float = float(os.getenv('HAS_BEEN_INFORMED_WEIGHT', "0.5")),
                 is_coerced_weight: float = float(os.getenv('IS_COERCED_WEIGHT', "0.25"))
                 ):
        """Initialize the autonomy valuator.

        Parameters
        ----------
        is_competent_weight: float
            The importance of 'is competent' when calculating the autonomy value.
        has_been_informed_weight: float
            The importance of 'has been informed' when calculating the autonomy value.
        is_coerced_weight: float
            The importance of 'is coerced' when calculating the autonomy value.
        """
        self.is_competent_weight = is_competent_weight
        self.has_been_informed_weight = has_been_informed_weight
        self.is_coerced_weight = is_coerced_weight

    def align_autonomy(self, treatment: TreatmentPayload) -> float:
        """Calculate the alignment of a treatment with the autonomy value.

        Parameters
        ----------
        treatment : TreatmentPayload
            The treatment to apply to a patient.

        Returns
        -------
        float
            The alignment of the treatment with the autonomy value.
        """
        alignment = 0.0
        status = treatment.before_status

        # Is competent alignment
        if status.normalized_is_competent() == 1.0:
            alignment += self.is_competent_weight
        else:
            alignment -= self.is_competent_weight

        # Has been informed alignment
        if status.normalized_has_been_informed() == 1.0:
            alignment += self.has_been_informed_weight
        else:
            alignment -= self.has_been_informed_weight

        # Is coerced alignment
        if status.normalized_is_coerced() == 1.0:
            alignment += self.is_coerced_weight
        else:
            alignment -= self.is_coerced_weight

        return alignment
