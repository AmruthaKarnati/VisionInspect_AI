import unittest

from anomaly_detector import calculate_severity


class RequirementTests(unittest.TestCase):
    def test_severity_calculation_matches_requirements(self):
        result = calculate_severity(
            size_score=85,
            location_score=90,
            defect_type_score=95,
            confidence_score=92,
        )

        self.assertAlmostEqual(result["severity_score"], 88.0, places=1)
        self.assertEqual(result["severity_level"], "Critical")
        self.assertIn("Reject Product", result["recommended_action"])


if __name__ == "__main__":
    unittest.main()
