import json
import re
from pathlib import Path
import pytest
from conftest import NOTEBOOKS

@pytest.mark.format
@pytest.mark.parametrize("nb_path", NOTEBOOKS, ids=lambda p: f"{p.parent.name}/{p.stem}")
def test_notebook_format(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cells = data.get("cells", [])
    assert cells, f"Notebook {nb_path} contains no cells."

    first_cell = cells[0]
    assert first_cell.get("cell_type") == "markdown", (
        f"Notebook {nb_path}: First cell must be markdown, got '{first_cell.get('cell_type')}'."
    )

    source_text = "".join(first_cell.get("source", []))
    lines = [line.strip() for line in source_text.splitlines() if line.strip()]
    assert lines, f"Notebook {nb_path}: First markdown cell is empty."

    first_line = lines[0]
    assert re.match(r"^#\s+[^#]", first_line), (
        f"Notebook {nb_path}: First line must start with single '# ' H1 title. Got: '{first_line}'"
    )

    assert len(lines) >= 2, (
        f"Notebook {nb_path}: First cell must contain a short description following the H1 title."
    )
