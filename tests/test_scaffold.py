from pathlib import Path


def test_learner_package_layout():
    root = Path(__file__).resolve().parents[1]
    assert (root / 'packages/solution/solution/pid_class.py').is_file()
    assert (root / 'packages/pid_controller/pid_controller/pid_controller_node.py').is_file()