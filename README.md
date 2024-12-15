<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Integrate Streamlit effortlessly with the Xircuits Component Library! Build and deploy interactive web applications with ease.</i></p>


---

## Xircuits Component Library for Streamlit

Integrates Xircuits with Streamlit for creating interactive web apps and real-time workflows.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

![streamlit_sample](https://github.com/user-attachments/assets/bbad8044-4e41-4e2b-9e79-bb20ce6ebe72)

### The Result:

![streamlit_sample_result](https://github.com/user-attachments/assets/cf6da186-cd8e-4477-8764-fe5579238ad3)

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.

## Main Xircuits Components

### Streamlit_Component:
Displays a Streamlit interface for analyzing Uber pickups in NYC, with features for data visualization and filtering.

<img src="https://github.com/user-attachments/assets/a890880a-a220-4875-b20a-60fca4a8da3c" alt="Streamlit_Component" width="200" height="100" />

### StreamlitMainLayout Component:
Provides the main Streamlit layout module to define the app's structure.

<img src="https://github.com/user-attachments/assets/d8a93115-1f7f-4994-b3cf-390cbde92823" alt="StreamlitMainLayout" width="200" height="75" />

### StreamlitSidebarLayout Component:
Outputs the Streamlit sidebar module to manage side panel layouts.

### StreamlitMakeColumns Component:
Creates a specified number of columns in the layout for organizing content.

### StreamlitWrite Component:
Displays text or objects in the main layout or a specified section.

### StreamlitDataFrame Component:
Renders a Pandas DataFrame as an interactive table in the layout.

### StreamlitTable Component:
Displays a Pandas DataFrame as a static table for non-editable data.

## Try The Examples

We have provided an example workflow to help you get started with the Streamlit component library. Give it a try and see how you can create custom Streamlit components for your applications.

### Streamlit Example

This example demonstrates the integration of Streamlit components to create an interactive data visualization app. It loads a CSV file, displays the data in a table, and plots a line chart. Additionally, it uses a sidebar to display and manage user inputs, like a text input field. The workflow is a simple yet effective showcase of building interactive interfaces with Streamlit and Xircuits.

## Installation
To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the Streamlit library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install streamlit
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-streamlit xai_components/xai_streamlit
pip install -r xai_components/xai_streamlit/requirements.txt 
```