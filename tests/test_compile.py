import ast
import json
import pytest
from conftest import NOTEBOOKS

@pytest.mark.compile
@pytest.mark.parametrize("nb_path", NOTEBOOKS, ids=lambda p: f"{p.parent.name}/{p.stem}")
def test_notebook_compiles(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for idx, cell in enumerate(data.get("cells", []), 1):
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", []))
            # Remove IPython magic commands (% or !) before AST compilation check
            python_lines = [
                line for line in source.splitlines()
                if not line.strip().startswith(("%", "!"))
            ]
            clean_source = "\n".join(python_lines)
            try:
                ast.parse(clean_source, filename=f"{nb_path.name}:cell_{idx}")
            except SyntaxError as e:
                pytest.fail(f"Notebook '{nb_path.name}' cell {idx} failed Python AST compilation:\n{e}")
