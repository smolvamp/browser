# PyQt6 Web Browser

A simple web browser application built using PyQt6, featuring basic navigation functionalities, a search bar, and download handling. This project demonstrates how to create a custom browser interface with PyQt6 and integrate web browsing capabilities through `QWebEngineView`.

## Features

- **Navigation Controls**: 
  - Back button
  - Forward button
  - Reload button
- **Search Bar**: Enter URLs directly or perform searches.
- **Download Handling**: Allows users to choose a directory to save files when downloading.
- **Maximized Window**: The window opens in a maximized state by default.
- **Custom Icons**: Adds custom icons for window, navigation buttons, and more.

## Requirements

To run this project, you'll need to install the following Python libraries:

- `PyQt6`
- `PyQt6.QtWebEngineWidgets`
- `PyQt6.QtWebEngineCore`

You can install the required libraries via pip:

```bash
pip install PyQt6 PyQt6-WebEngine
```
## Usage

  Clone the repository or download the source code.
  Ensure you have the necessary icons (icon.jpeg, previous.png, next-button.png, and power.png) in the src/ directory.
  Run the Python script.
```
python browser.py
```
The browser will open in a maximized window with Google's homepage loaded by default. You can:

  Navigate through web pages using the back, forward, and reload buttons.
  Enter a new URL or perform a search using the search bar.
  Download files to a specified directory using the download feature.

## Contributing

Feel free to fork this repository and submit issues or pull requests for improvements. If you'd like to contribute, please follow these steps:

  Fork the repository.
  Create a new branch (git checkout -b feature-name).
  Make your changes.
  Commit your changes (git commit -am 'Add feature').
  Push to the branch (git push origin feature-name).
  Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/smolvamp/browser/blob/main/LICENSE) file for details.
