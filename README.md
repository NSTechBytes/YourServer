# YourServer

A lightweight Python-based HTTP server with a GUI and system tray integration.

## Features

- Serves static files from the `documentation` directory.
- Automatically finds an available port starting from 2100.
- Minimal GUI for controlling the server.
- System tray integration to minimize the application.

## Prerequisites

Ensure you have Python installed (Python 3.x recommended). Install the required dependencies:

```sh
pip install pystray pillow
```

## How to Run

1. Clone the repository or copy the script to your local machine.
2. Run the script:
   ```sh
   python yourserver.py
   ```
3. The server will start and be accessible at `http://localhost:<port>`.

## Usage

- The application automatically looks for an available port.
- The GUI allows minimizing to the system tray.
- Click "Hide to Tray" to send the app to the system tray.
- Right-click the tray icon to show the window or exit the app.

## Directory Structure

```
.
├── yourserver.py      # Main script
├── documentation  # Folder to serve files from
```

## Troubleshooting

- If the `documentation` directory does not exist, the script will create it.
- If port 2100 is in use, the application will automatically find an available port.

## License

This project is licensed under the Apache License. Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or feature requests.
