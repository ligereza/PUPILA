import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from pupila import (  # noqa: E402
    InterfaceElement,
    InterfaceSnapshot,
    Task,
    TaskStep,
    associate_interfaces,
    translate_task,
)


class PUPILAAssociationTests(unittest.TestCase):
    def setUp(self):
        self.source = InterfaceSnapshot(
            "known-app",
            "1",
            (
                InterfaceElement(
                    "export",
                    "button",
                    "Exportar proyecto",
                    "export",
                    ("mouse", "keyboard"),
                    ("file_export",),
                ),
            ),
        )
        self.target = InterfaceSnapshot(
            "new-app",
            "2",
            (
                InterfaceElement(
                    "save-as",
                    "button",
                    "Export file",
                    "export",
                    ("mouse",),
                    ("file_export",),
                ),
                InterfaceElement("render", "button", "Render", "render", ("touch",), ("render",)),
            ),
        )

    def test_returns_mapping_with_evidence_and_never_executes(self):
        result = associate_interfaces(self.source, self.target)
        self.assertEqual(result.status, "CANDIDATES_AVAILABLE")
        self.assertEqual(result.candidates[0].target_element_id, "save-as")
        self.assertIn("action_exact", result.candidates[0].evidence)
        self.assertEqual(result.provenance["execution"], "not_performed")

    def test_ambiguous_result_keeps_candidates(self):
        ambiguous = InterfaceSnapshot(
            "ambiguous",
            "1",
            (
                InterfaceElement("a", "button", "Export", "export"),
                InterfaceElement("b", "button", "Export", "export"),
            ),
        )
        result = associate_interfaces(self.source, ambiguous, ambiguity_margin=0.5)
        self.assertEqual(result.status, "AMBIGUOUS_CANDIDATES")
        self.assertEqual(len(result.for_source("export")), 2)

    def test_task_translation_does_not_hide_unavailable_step(self):
        task = Task("export-task", (TaskStep("step-1", "export the project", "export"),))
        translated = translate_task(task, self.source, self.target)
        self.assertEqual(translated["steps"][0]["status"], "MAPPED")
        self.assertEqual(translated["steps"][0]["execution"], "not_performed")

    def test_missing_source_mapping_is_review_required(self):
        task = Task("unknown-task", (TaskStep("step-1", "publish", "missing"),))
        translated = translate_task(task, self.source, self.target)
        self.assertEqual(translated["status"], "REVIEW_REQUIRED")
        self.assertEqual(translated["steps"][0]["status"], "UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
