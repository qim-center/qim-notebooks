from pathlib import Path
import pytest
from testbook import testbook
from conftest import NOTEBOOKS, REPO_ROOT

CATEGORY_TIMEOUTS = {
    "data": 300,
    "generation": 300,
    "processing": 180,
    "reconstruction": 180,
    "visualization": 180,
}

# Notebooks requiring high RAM, large disk space, local datasets, GPU acceleration, or Conda-only packages
HEAVY_NOTEBOOKS = {
    "generation/Large_data_generation.ipynb": "Generates large synthetic data volumes.",
    "processing/Larger_than_memory_processing.ipynb": "Generates multi-gigabyte synthetic datasets.",
    "processing/Dask_OME-zarr_pipeline-OpticalNerve.ipynb": "Requires local dataset OpticalNerve.zarr.",
    "processing/Dask_OME-zarr_pipeline.ipynb": "Requires local dataset vol_2000.zarr.",
    "processing/Reconstructed_data_insights.ipynb": "Requires DTU cluster network file path.",
    "reconstruction/padding.ipynb": "Requires DTU cluster network file path.",
    "reconstruction/ct_subsampling.ipynb": "Requires Conda C++ package ccpi-regulariser.",
}





def get_timeout(nb_path: Path) -> int:
    category = nb_path.parent.name
    return CATEGORY_TIMEOUTS.get(category, 180)

@pytest.mark.execution
@pytest.mark.parametrize("nb_path", NOTEBOOKS, ids=lambda p: f"{p.parent.name}/{p.stem}")
def test_notebook_runs(nb_path, tmp_work_dir, request):
    rel_path = str(nb_path.relative_to(REPO_ROOT))
    if rel_path in HEAVY_NOTEBOOKS:
        if not request.config.getoption("--run-heavy"):
            pytest.skip(f"Skipping heavy notebook (use --run-heavy to run): {HEAVY_NOTEBOOKS[rel_path]}")

    abs_nb_path = nb_path.resolve()

    timeout = get_timeout(nb_path)
    with testbook(
        str(abs_nb_path),
        execute=True,
        timeout=timeout,
        cd=tmp_work_dir,
    ) as tb:
        pass
