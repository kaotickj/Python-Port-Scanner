# Python Port Scanner

This Python script is a simple yet effective port scanner that allows you to scan a target host for open ports. It supports multi-threading to improve the scanning speed and provides colorful and informative output.

## Features

- Scans a range of ports on a target host for open ports.
- Utilizes multi-threading for concurrent scanning.
- Displays open ports with additional information if available.
- Provides colorful output for better readability.

## Prerequisites

- Python 3.x installed.

## Usage

1. Clone this repository or download the `port_scanner.py` file.

2. Open a terminal or command prompt.

3. Navigate to the directory where the `port_scanner.py` script is located.

4. Run the script using the following command:

```shell
python port_scanner.py <host> -p <port_range> -t <timeout> -c <concurrency>
```
5. Replace the placeholders:

    <host>: The target host you want to scan (can be an IP address or hostname).
    <port_range>: The range of ports to scan, e.g., 1-1024.
    <timeout>: Timeout for each port scan in seconds (optional, default is 1 second).
    <concurrency>: Maximum number of concurrent threads (optional, default is 10).

Example:

```shell
python port_scanner.py example.com -p 1-1024 -t 1 -c 20
```

The script will start scanning the specified ports on the target host and display the results in the terminal.

## Notes

>This script is intended for educational and ethical use. Please make sure you have proper authorization before scanning any target host.

## License

This project is licensed under the GNU General Public License, version 3 (GPL-3.0). Feel free to use, modify, and distribute it according to the terms of the license.
