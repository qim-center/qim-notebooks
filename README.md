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

## Contribution

Each Jupyter notebook must include a specific first cell format for proper display in the QIM platform.

### First Cell Pattern

The **first cell** of every notebook must be a **markdown cell** with the following structure:

```markdown
# Notebook Title

Brief description of what the notebook does.
```

### Requirements

- **Cell type**: Must be a markdown cell (not code)
- **Line 1**: Title starting with `#` (single hash for H1 heading)
  - The `#` symbol will be automatically stripped when displayed
  - Becomes the notebook's display title in the gallery
- **Line 2**: Description text
  - Used as preview text in the notebook gallery
  - Keep under 300 characters for best display (automatically truncated if longer)
  - Should concisely explain the notebook's purpose

### Example

```markdown
# Image Segmentation with Machine Learning

This notebook demonstrates how to use deep learning for semantic segmentation of microscopy images using PyTorch and the U-Net architecture.
```
