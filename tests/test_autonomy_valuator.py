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

import math
import unittest

from json_resources import load_treatment_json

from c2_treatment_autonomy_valuator.autonomy_valuator import AutonomyValuator
from c2_treatment_autonomy_valuator.patient_status_criteria import PatientStatusCriteria
from c2_treatment_autonomy_valuator.treatment_payload import TreatmentPayload


class TestAutonomyValuator(unittest.TestCase):
	"""Class to test the autonomy valuator"""

	def setUp(self):
		"""Create the valuator."""
		
		self.valuator = AutonomyValuator(
				is_competent_weight=0.25,
				has_been_informed_weight=0.5,
				is_coerced_weight=0.25
			)


	def test_align_autonomy(self):
		"""Test calculate alignment for a treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		alignment = self.valuator.align_autonomy(treatment)
		assert math.isclose(alignment, -0.5), 'Unexpected treatment autonomy alignment value'


	def test_align_autonomy_for_treatment_with_empty_before_status(self):
		"""Test calculate alignment with an empty before status treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.before_status = PatientStatusCriteria()
		alignment = self.valuator.align_autonomy(treatment)
		assert math.isclose(alignment, -1.0), 'Unexpected treatment autonomy alignment value'

	def test_align_autonomy_for_treatment_with_all_true_fields(self):
		"""Test calculate alignment with an empty before status treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.before_status.is_competent = True
		treatment.before_status.has_been_informed = True
		treatment.before_status.is_coerced = True
		alignment = self.valuator.align_autonomy(treatment)
		assert math.isclose(alignment, 0.5), 'Unexpected treatment autonomy alignment value'

	def test_align_autonomy_for_treatment_with_all_fale_fields(self):
		"""Test calculate alignment with an empty before status treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.before_status.is_competent = False
		treatment.before_status.has_been_informed = False
		treatment.before_status.is_coerced = False
		alignment = self.valuator.align_autonomy(treatment)
		assert math.isclose(alignment, -0.5), 'Unexpected treatment autonomy alignment value'

if __name__ == '__main__':
    unittest.main()
