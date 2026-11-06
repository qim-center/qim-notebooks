# QIM Notebooks Collection

A collection of Jupyter Notebooks for working with volumetric 3D data using `qim3d`.

These notebooks demonstrate common workflows, analysis patterns, visualization techniques, and teaching material from the Qim Center. They are designed to help researchers, students, and developers reproduce examples, learn by doing, and extend the library for new use cases.

The `qim3d` library includes tools for loading and manipulating 3D image data, processing and filtering, visualization and interactive viewing, and advanced analysis routines. Learn more in the documentation: https://docs.qim.dk/qim3d/

For community discussions and support, visit: https://forum.qim.dk/

## Getting Started

To run any of the notebooks in this collection, you only need to install qim3d.
Installation instructions can be found here: https://docs.qim.dk/qim3d/#installation

Once qim3d is installed, you can open the notebooks in Jupyter Lab or Jupyter Notebook and run them directly.

## Categories

### 💽 Data

Loading, streaming, and managing large volumetric datasets. Includes examples for different file formats, chunked I/O, and working with limited RAM.

### 🔍 Visualization

Interactive plotting and 3D rendering. Includes qim3d viewers, volume rendering, and animation.

### 🧰 Processing

Filtering, segmentation, measurement, and morphological analysis. Shows how to combine qim3d components into reproducible processing workflows.

### 🧪 Generation

Creating synthetic volumetric data for testing and development.

## Contributors

This collection is developed and maintained by the **QIM Center** community. We welcome contributions from researchers, developers, and users of all skill levels! 

If you would like to contribute a new workflow notebook or improve an existing example, please submit a pull request. 

### Notebook Formatting Guidelines
To maintain consistency across the repository collection, **notebooks should adhere to the following format**. This is to ensure that all notebooks can be visualised consistently on our platform. Notebooks that do not include this exact structure will not be accepted:

1. **First cell as markdown:** The very first cell of the notebook should be a markdown cell.
2. **# H1 Title:** The very first line of the first cell **must** start with a single `#` to define an H1 title (e.g., `# Large data generation` or `# Tubular structure`).
3. **Short Description:** Immediately following the title in the same cell, you **must** include a short, one-sentence description explaining exactly what the notebook does. This description is required to fit into our documentation layout.

## Testing

This repository uses `pytest` and [`testbook`](https://testbook.readthedocs.io/) to validate notebook formatting, code syntax, and execution.

### Fast Local Checks (Default)

Running standard `pytest` executes format and AST syntax compilation checks across all notebooks in **< 1 second** without starting Jupyter kernels:

```bash
uv run pytest
```

- **Format Checks (`-m format`):** Verifies that the first cell is markdown with a single `#` H1 title followed by a short description.
- **Compilation Checks (`-m compile`):** Validates Python code cell AST syntax across all notebooks.

### Notebook Execution Tests

To test end-to-end notebook execution:

```bash
uv run pytest -m execution
```

- **Headless & Offscreen:** Automatically sets PyVista, VTK, Matplotlib, and Qt to run offscreen without opening GUI windows or disrupting desktop environments.
- **Heavy Notebook Isolation:** Notebooks requiring high RAM, local datasets, or GPU acceleration are skipped by default.

To include heavy notebooks:

```bash
uv run pytest -m execution --run-heavy
```

To run execution tests for a specific category or notebook:

```bash
uv run pytest -m execution -k visualization
uv run pytest -m execution -k Simple_visualization
```

If you have questions or want to discuss your notebook ideas before submitting a pull request, join the conversation on our community forum: https://forum.qim.dk/.