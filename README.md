# Internet Connectivity Checker and Rebooter

This Python script checks internet connectivity by attempting to retrieve the external IP address. If the internet is not available, it triggers a system reboot.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Have you ever wanted an automated way to check internet connectivity and reboot your system if the internet is not available? This Python script does just that. It attempts to retrieve the external IP address and, if unsuccessful after multiple attempts, triggers a system reboot.

## Features

- **Internet Connectivity Check**: Uses an external service to check internet connectivity.
- **Automatic Reboot**: If the internet is not available, the script triggers a system reboot.
- **Logging and Error Handling**: Detailed logging of events and error handling for improved diagnostics.

## Requirements

- Python 3.x
- Internet connection for the script to check

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xhico/CheckInternet .git

2. Change into the project directory:

    ```bash
    cd CheckInternet
    ```

3. Run the script:

    ```bash
    python3 CheckInternet.py
    ```

## Usage

1. Execute the script, and it will check internet connectivity.
2. If the internet is not available, the script will trigger a system reboot.

## Logging
The script logs events and errors for better diagnostics. You can find the log file at CheckInternet.log in the same directory as the script.

## Error Handling
If an error occurs during script execution, an email notification with the error details will be sent using the sendEmail function.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
