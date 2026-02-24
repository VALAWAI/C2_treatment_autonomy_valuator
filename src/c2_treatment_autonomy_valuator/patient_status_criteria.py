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

from enum import Enum

from pydantic import BaseModel, Field


class AgeRangeOption(str, Enum):
    """The different ranges of ages for a patient."""

    # The age is between 0 and 19 years old.
    AGE_BETWEEN_0_AND_19 = "AGE_BETWEEN_0_AND_19"

    # The age is between 20 and 29 years old.
    AGE_BETWEEN_20_AND_29 = "AGE_BETWEEN_20_AND_29"

    # The age is between 30 and 39 years old.
    AGE_BETWEEN_30_AND_39 = "AGE_BETWEEN_30_AND_39"

    # The age is between 40 and 49 years old.
    AGE_BETWEEN_40_AND_49 = "AGE_BETWEEN_40_AND_49"

    # The age is between 50 and 59 years old.
    AGE_BETWEEN_50_AND_59 = "AGE_BETWEEN_50_AND_59"

    # The age is between 60 and 69 years old.
    AGE_BETWEEN_60_AND_69 = "AGE_BETWEEN_60_AND_69"

    # The age is between 70 and 79 years old.
    AGE_BETWEEN_70_AND_79 = "AGE_BETWEEN_70_AND_79"

    # The age is between 80 and 89 years old.
    AGE_BETWEEN_80_AND_89 = "AGE_BETWEEN_80_AND_89"

    # The age is between 90 and 99 years old.
    AGE_BETWEEN_90_AND_99 = "AGE_BETWEEN_90_AND_99"

    # The age is more than 99 years old.
    AGE_MORE_THAN_99 = "AGE_MORE_THAN_99"


class SurvivalOptions(str, Enum):
    """The possible survival options."""

    # The survival is less than 12 months.
    LESS_THAN_12_MONTHS = "LESS_THAN_12_MONTHS"

    # The survival is more than 12 months.
    MORE_THAN_12_MONTHS = "MORE_THAN_12_MONTHS"

    # The survival is unknown.
    UNKNOWN = "UNKNOWN"


class SPICT_Scale(str, Enum):
    """It helps identify the most fragile people who have one or more health
    problems. It is based on the comprehensive geriatric assessment (applicable
    to non-geriatric patients) that evaluates areas such as functional
    independence, nutritional status, cognitive, emotional, social, geriatric
    syndromes (confusion syndrome, falls, ulcers, polypharmacy, dysphagia),
    symptoms (pain or dyspnea) and oncological, respiratory, cardiac,
    neurological, digestive or renal diseases.
    """

    # The low option of the SPICT scale.
    LOW = "LOW"

    # The moderate option of the SPICT scale.
    MODERATE = "MODERATE"

    # The high option of the SPICT scale.
    HIGH = "HIGH"

    # The level in the SPICT scale.
    UNKNOWN = "UNKNOWN"


class ClinicalRiskGroupOption(str, Enum):
    """The possible clinical risk groups."""

    # The clinical risk group is promotion & prevention.
    PROMOTION_AND_PREVENTION = "PROMOTION_AND_PREVENTION"

    # The clinical risk group is self-management support.
    SELF_MANAGEMENT_SUPPORT = "SELF_MANAGEMENT_SUPPORT"

    # The clinical risk group is illness management.
    ILLNESS_MANAGEMENT = "ILLNESS_MANAGEMENT"

    # The clinical risk group is case management.
    CASE_MANAGEMENT = "CASE_MANAGEMENT"

    # The clinical risk group is unknown.
    UNKNOWN = "UNKNOWN"


class BarthelIndex(str, Enum):
    """This index allows checking the functional independence for basic activities."""

    # When the functional independence is between 0 and 20%.
    TOTAL = "TOTAL"

    # When the functional independence is between 21 and 60%.
    SEVERE = "SEVERE"

    # When the functional independence is between 61 and 90%.
    MODERATE = "MODERATE"

    # When the functional independence is between 91 and 99%.
    MILD = "MILD"

    # When the functional independence is 100%.
    INDEPENDENT = "INDEPENDENT"

    # When the functional independence is unknown.
    UNKNOWN = "UNKNOWN"


class CognitiveImpairmentLevel(str, Enum):
    """Define the possible cognitive impairment levels."""

    # The cognitive impairment is absent.
    ABSENT = "ABSENT"

    # The cognitive impairment is mild-moderate.
    MILD_MODERATE = "MILD_MODERATE"

    # The cognitive impairment is severe.
    SEVERE = "SEVERE"

    # The cognitive level is unknown.
    UNKNOWN = "UNKNOWN"


class DiscomfortDegree(str, Enum):
    """The degree of discomfort."""

    # The discomfort degree is low or there is no discomfort.
    LOW = "LOW"

    # The discomfort degree is medium.
    MEDIUM = "MEDIUM"

    # The discomfort degree is high.
    HIGH = "HIGH"

    # The cognitive level is unknown.
    UNKNOWN = "UNKNOWN"


class NITLevel(str, Enum):
    """The level of therapeutic intensity."""

    # It includes all possible measures to prolong survival.
    ONE = "ONE"

    # Includes all possible measures except CPR.
    TWO_A = "TWO_A"

    # Includes all possible measures except CPR and ICU.
    TWO_B = "TWO_B"

    # Includes complementary scans and non-invasive treatments.
    THREE = "THREE"

    # It includes empirical symptomatic treatments according to clinical suspicion,
    # which can be temporarily agreed upon.
    FOUR = "FOUR"

    # No complementary examinations or etiological treatments are carried out, only
    # comfort treatments.
    FIVE = "FIVE"


class PatientStatusCriteria(BaseModel):
    """The status of a patient according to some criteria."""

    age_range: AgeRangeOption | None = Field(
        default=None, title="The age range of the patient status."
    )
    ccd: bool | None = Field(
        default=None, title="Whether the patient status has a Complex Chronic Disease (CCD)."
    )
    maca: bool | None = Field(
        default=None,
        title="A MACA patient status has answered no to the question: 'Would you be surprised if this patient died in less than 12 months?'"
    )
    expected_survival: SurvivalOptions | None = Field(
        default=None, title="The expected survival time for the patient status."
    )
    frail_VIG: SPICT_Scale | None = Field(
        default=None, title="The fragility index of the patient status."
    )
    clinical_risk_group: ClinicalRiskGroupOption | None = Field(
        default=None, title="The clinical risk group of the patient status."
    )
    has_social_support: bool | None = Field(
        default=None, title="Whether the patient status has social support."
    )
    independence_at_admission: BarthelIndex | None = Field(
        default=None, title="The independence for basic activities of daily living at admission."
    )
    independence_instrumental_activities: int | None = Field(
        default=None, title="The index that measures the independence for instrumental activities."
    )
    has_advance_directives: bool | None = Field(
        default=None, title="Whether the patient status has advance directives."
    )
    is_competent: bool | None = Field(
        default=None,
        title="Whether the patient status is competent to understand the instructions of health personnel."
    )
    has_been_informed: bool | None = Field(
        default=None,
        title="Whether the patient status or his/her authorized representative has been informed of possible treatments and the consequences of receiving them."
    )
    is_coerced: bool | None = Field(
        default=None,
        title="Whether it is detected that the patient status has been coerced/pressured by third parties."
    )
    has_cognitive_impairment: CognitiveImpairmentLevel | None = Field(
        default=None, title="Whether the patient status has cognitive impairment."
    )
    has_emocional_pain: bool | None = Field(
        default=None, alias="has_emocional_pain", title="Whether the patient status has emotional pain."
    )
    discomfort_degree: DiscomfortDegree | None = Field(
        default=None, title="Describes the degree of discomfort of the patient status before applying any action."
    )
    nit_level: NITLevel | None = Field(
        default=None, title="Describes the level of therapeutic intensity of the patient."
    )

    # Normalization constants
    _AGE_RANGE_MAP = {
        AgeRangeOption.AGE_BETWEEN_0_AND_19: 0.1,
        AgeRangeOption.AGE_BETWEEN_20_AND_29: 0.2,
        AgeRangeOption.AGE_BETWEEN_30_AND_39: 0.3,
        AgeRangeOption.AGE_BETWEEN_40_AND_49: 0.4,
        AgeRangeOption.AGE_BETWEEN_50_AND_59: 0.5,
        AgeRangeOption.AGE_BETWEEN_60_AND_69: 0.6,
        AgeRangeOption.AGE_BETWEEN_70_AND_79: 0.7,
        AgeRangeOption.AGE_BETWEEN_80_AND_89: 0.8,
        AgeRangeOption.AGE_BETWEEN_90_AND_99: 0.9,
        AgeRangeOption.AGE_MORE_THAN_99: 1.0,
    }

    _SURVIVAL_MAP = {
        SurvivalOptions.MORE_THAN_12_MONTHS: 1.0,
    }

    _FRAIL_VIG_MAP = {
        SPICT_Scale.LOW: 1.0,
        SPICT_Scale.MODERATE: 0.5,
    }

    _CLINICAL_RISK_MAP = {
        ClinicalRiskGroupOption.PROMOTION_AND_PREVENTION: 1.0,
        ClinicalRiskGroupOption.SELF_MANAGEMENT_SUPPORT: 0.5,
    }

    _BARTHEL_INDEX_MAP = {
        BarthelIndex.TOTAL: 0.1,
        BarthelIndex.SEVERE: 0.4,
        BarthelIndex.MODERATE: 0.75,
        BarthelIndex.MILD: 0.95,
        BarthelIndex.INDEPENDENT: 1.0,
    }

    _COGNITIVE_IMPAIRMENT_MAP = {
        CognitiveImpairmentLevel.ABSENT: 1.0,
        CognitiveImpairmentLevel.MILD_MODERATE: 0.5,
    }

    _DISCOMFORT_DEGREE_MAP = {
        DiscomfortDegree.LOW: 1.0,
        DiscomfortDegree.MEDIUM: 0.5,
    }

    def normalized_age_range(self) -> float:
        """Return the normalized value of the age range."""
        return self._AGE_RANGE_MAP.get(self.age_range, 0.0)

    def normalized_ccd(self) -> float:
        """Return the normalized value of the CCD."""
        return 1.0 if self.ccd is False else 0.0

    def normalized_maca(self) -> float:
        """Return the normalized value of the MACA."""
        return 1.0 if self.maca is False else 0.0

    def normalized_expected_survival(self) -> float:
        """Return the normalized value of the expected survival."""
        return self._SURVIVAL_MAP.get(self.expected_survival, 0.0)

    def normalized_frail_vig(self) -> float:
        """Return the normalized value of the frail VIG."""
        return self._FRAIL_VIG_MAP.get(self.frail_VIG, 0.0)

    def normalized_clinical_risk_group(self) -> float:
        """Return the normalized value of the clinical risk group."""
        return self._CLINICAL_RISK_MAP.get(self.clinical_risk_group, 0.0)

    def normalized_has_social_support(self) -> float:
        """Return the normalized value of the has social support."""
        return 1.0 if self.has_social_support is True else 0.0

    def normalized_independence_at_admission(self) -> float:
        """Return the normalized value of the independence at admission."""
        return self._BARTHEL_INDEX_MAP.get(self.independence_at_admission, 0.0)

    def normalized_independence_instrumental_activities(self) -> float:
        """Return the normalized value of the independence instrumental activities."""
        match self.independence_instrumental_activities:
            case None:
                return 0.0
            case i if 1 <= i <= 8:
                # Index scales roughly linearly from 1 to 8 to 0.13 to 1.0
                return round(i * 0.125, 2) if i < 8 else 1.0
            case _:
                return 0.0

    def normalized_has_advance_directives(self) -> float:
        """Return the normalized value of the has advance directives."""
        return 1.0 if self.has_advance_directives is True else 0.0

    def normalized_is_competent(self) -> float:
        """Return the normalized value of the is competent."""
        return 1.0 if self.is_competent is True else 0.0

    def normalized_has_been_informed(self) -> float:
        """Return the normalized value of the has been informed."""
        return 1.0 if self.has_been_informed is True else 0.0

    def normalized_is_coerced(self) -> float:
        """Return the normalized value of the is coerced."""
        return 1.0 if self.is_coerced is False else 0.0

    def normalized_has_cognitive_impairment(self) -> float:
        """Return the normalized value of the has cognitive impairment."""
        return self._COGNITIVE_IMPAIRMENT_MAP.get(self.has_cognitive_impairment, 0.0)

    def normalized_has_emocional_pain(self) -> float:
        """Return the normalized value of the has emotional pain."""
        return 1.0 if self.has_emocional_pain is False else 0.0

    def normalized_discomfort_degree(self) -> float:
        """Return the normalized value of the has discomfort degree."""
        return self._DISCOMFORT_DEGREE_MAP.get(self.discomfort_degree, 0.0)
