# YourServer

`YourServer` is a lightweight web server application that serves files from a local directory, with the added functionality of being able to hide the server window into the system tray. It uses Python, Tkinter for the graphical user interface, and PyStray for tray icon management.

## Features
- Starts a local web server to serve files from the `documentation` directory.
- Runs on an available port dynamically (avoids port conflicts).
- Customizable and minimalist GUI built with Tkinter.
- Option to hide the server window to the system tray.
- Cross-platform compatible (tested on Windows).

## Requirements
- Python 3.x
- `pystray` for system tray functionality
- `Pillow` for image handling
- `Tkinter` (usually pre-installed with Python)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/YourServer.git
   ```

2. Navigate into the project directory:

   ```bash
   cd YourServer
   ```

3. Install the required dependencies:

   ```bash
   pip install pystray pillow
   ```

## Usage

1. Place the `documentation` directory in the same directory as the Python script, or modify the `DIRECTORY` variable to point to the correct folder.
   
2. Run the server script:

   ```bash
   python yourserver.py
   ```

3. The server will start running and be accessible at:
   ```
   http://localhost:2100
   ```

   If port 2100 is already in use, the server will automatically try the next available port.

4. The window can be hidden to the system tray by clicking the "Hide to Tray" button, and can be restored from there by clicking "Show".

5. The application can be exited from the system tray or by clicking the close button on the window.


## Contributing

If you would like to contribute to `YourServer`, feel free to fork this repository, create a new branch, and submit a pull request with your improvements or bug fixes.

## License

This project is open-source and available under the [Apache License](LICENSE).

## Acknowledgements

- **Tkinter**: For building the GUI.
- **PyStray**: For managing system tray icons.
- **Pillow**: For image creation and manipulation.
