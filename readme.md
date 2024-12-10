I DEVELOP THIS SMALL PROGRAM FOR STUDY PURPOSES. IT WILL NOT ENSURE THAT WILL KEEP YOU SAFE FROM MALICIOUS STUFF ON THE NET.

# Clickjacking Scanner

A simple Python script to scan websites for potential clickjacking vulnerabilities by checking for the presence of `X-Frame-Options` and `Content-Security-Policy` headers.

## Prerequisites

Ensure you have Python 3 installed on your system. You can verify the installation by running:

```bash
python3 --version
```

You also need the `requests` library to make HTTP requests. Install it using pip if you don’t already have it:

```bash
pip install requests
```

## Installation

1. Clone or download this repository to your local machine.
2. Save the script in a file named `clickjacking_scanner.py`.

## Usage

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script using the following command:

```bash
python3 clickjacking_scanner.py
```

### Input

When prompted, enter the URL of the website you want to scan. Ensure you include the protocol (e.g., `http://` or `https://`). Example:

```plaintext
Enter the URL to scan (include http/https): https://example.com
```

### Output

The script will analyze the headers returned by the website and output the following information:

1. **X-Frame-Options Header**: If present, its value will be displayed. If missing, a warning will appear.
2. **Content-Security-Policy Header**: If the `frame-ancestors` directive is present, its value will be displayed. If missing or not properly configured, a warning will appear.

### Example Output

```plaintext
X-Frame-Options header found: SAMEORIGIN
Content-Security-Policy (frame-ancestors) found: frame-ancestors 'self';
```

If any issues are detected:

```plaintext
X-Frame-Options header is missing!
Content-Security-Policy header is missing or doesn't include 'frame-ancestors'!
```

## Notes

This script is intended for basic scanning and learning purposes. For comprehensive security audits, consider using professional tools like OWASP ZAP or Burp Suite.

## Contributing

Feel free to contribute by submitting issues or pull requests to improve this script.

## License

This project is licensed under the MIT License.

## 📞 **Contact**

- Developer: Alberto Rogatto
- Email: [alrogattodev@gmail.com]
- GitHub: [https://github.com/alrogattodev](https://github.com/alrogattodev)