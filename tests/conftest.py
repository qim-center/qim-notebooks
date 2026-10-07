import os
from pathlib import Path
import pytest

# Set headless environment variables to prevent GUI display crashes during notebook execution
os.environ.setdefault("PYVISTA_OFF_SCREEN", "true")
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("VTK_DEFAULT_OFF_SCREEN", "true")

REPO_ROOT = Path(__file__).parents[1]

def get_all_notebooks():
    """Recursively find all notebooks excluding virtual environments and hidden directories."""
    return sorted(
        p for p in REPO_ROOT.glob("**/*.ipynb")
        if not any(part.startswith(".") or part in ("venv", "node_modules") for part in p.parts)
    )

NOTEBOOKS = get_all_notebooks()


def pytest_addoption(parser):
    """Add CLI flags for pytest."""
    parser.addoption(
        "--run-heavy",
        action="store_true",
        default=False,
        help="Run heavy/large-memory notebooks that require high RAM or GPU acceleration.",
    )


@pytest.fixture
def tmp_work_dir(tmp_path, monkeypatch):
    """Fixture to change working directory to an isolated temporary folder for notebook execution."""
    import shutil
    monkeypatch.chdir(tmp_path)
    yield tmp_path
    # Clean up generated temp files to prevent disk quota exhaustion
    shutil.rmtree(tmp_path, ignore_errors=True)

