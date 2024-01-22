# Golias

## Overview

**Golias** is a Python script designed for conducting login brute-force attacks on a target URL. This script supports both `POST` and `GET` methods for sending login requests. Please note that unauthorized use of this script on any system without explicit permission may violate privacy and legal regulations. The author is not responsible for any misuse of the script.

## Features

- **Flexible Request Methods**: Golias supports both `POST` and `GET` request methods for login attempts.

- **Brute-force Attack**: The script utilizes a brute-force approach, attempting to log in with a predefined username and a list of passwords from a wordlist.

- **Dynamic Input**: Users can input the target URL, request method, and the path to a wordlist file interactively.

## Prerequisites

Before using Golias, ensure you have the necessary dependencies installed:

```bash
pip install requests
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/TUR14CUS/Golias.git
cd Golias
```

2. Run the script with the desired target URL, request method, and wordlist file:

```bash
python golias.py
```

Follow the prompts to input the target URL, request method (`POST` or `GET`), and the path to the wordlist file.

## Script Options

- **Target URL**: The URL where the login attempts will be made.

- **Request Method**: Specify the HTTP request method (`POST` or `GET`) to use for login attempts.

- **Wordlist File**: Provide the path to a text file containing a list of passwords to attempt.

## Example

```bash
python golias.py
Enter target URL: http://example.com/login
Enter request method (POST or GET): POST
Enter file path: /path/to/wordlist.txt
```

## Disclaimer

This script is provided for educational purposes only. Unauthorized use of this script on systems without explicit permission may violate privacy and legal regulations. The author is not responsible for any misuse of the script.

## Author

- **TUR14CUS** - [GitHub](https://github.com/TUR14CUS)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
