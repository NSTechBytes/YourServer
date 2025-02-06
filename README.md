# YourServer

YourServer is a simple local HTTP server with a GUI interface built using Tkinter. It allows users to serve a documentation directory locally and provides a system tray icon for easy access and control.

## Features

- Runs a local HTTP server on port **2100**.
- Serves files from the `documentation` directory.
- Provides a minimalistic GUI with a custom title bar.
- Allows window dragging functionality.
- Includes a system tray icon with **Show** and **Exit** options.
- Ability to hide the window to the system tray.

## Prerequisites

Ensure you have **Python 3.x** installed along with the required dependencies:

```bash
pip install pystray pillow
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/YourServer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd YourServer
   ```
3. Run the server:
   ```bash
   python yourserver.py
   ```

## How It Works

- The script checks for the `documentation` directory.
- Starts an HTTP server on `http://localhost:2100`.
- Opens a Tkinter-based GUI.
- Provides an option to minimize the app to the system tray.

## System Tray Functionality

- **Show**: Restores the application window.
- **Exit**: Stops the server and closes the application.

## Notes

- Ensure the `documentation` folder exists before running the script.
- To change the serving directory, modify the `DIRECTORY` variable in the script.
- You can change the port by modifying the `PORT` variable.

## License

This project is licensed under the **MIT License**. Feel free to modify and distribute it.

## Author

[NSTechBytes](https://github.com/NSTechBytes)

---

### Contributions

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

### Support

If you find this project useful, consider giving it a ⭐ on GitHub!

Happy coding! 🚀
