# Windsurf Setup Guide

A comprehensive guide and website for learning how to install, set up, and master Windsurf - the next-generation AI IDE.

## Overview

This repository contains two main resources:

1. A detailed markdown guide (`documents/windsurf_guide.md`) covering everything from installation to advanced usage
2. A component-based website (`documents/windsurf_site/`) that presents this information in an interactive format

## Website Structure

The website is built using a component-based architecture with:

- HTML components in the `components/` directory
- CSS styles in the `css/` directory
- JavaScript functionality in the `js/` directory

## Features

- Step-by-step installation instructions for all major platforms
- Detailed setup guide
- Comprehensive introduction to Cascade, Windsurf's AI assistant
- Overview of MCP (Model Context Protocol) functionality
- Troubleshooting section
- 8-lesson curriculum for beginners (~13 hours of instruction)
- Reference materials and resources

## Local Development

To view the website locally:

1. Clone this repository
2. Navigate to the project directory
3. Set up a local server (due to component loading requirements)

Example using Python's built-in server:
```bash
# For Python 3
cd documents/windsurf_site
python3 -m http.server

# For Python 2
cd documents/windsurf_site
python -m SimpleHTTPServer
```

Then open your browser to `http://localhost:8000`

## Contributions

Contributions are welcome! Feel free to submit pull requests with improvements to the guide or website.

## License

This project is intended for educational purposes.

## Last Updated

This guide was last updated on May 20, 2025.
