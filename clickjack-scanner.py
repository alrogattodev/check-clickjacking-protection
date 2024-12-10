import requests

def check_clickjacking_protection(url):
    try:
        # Make a request to the website
        response = requests.get(url)
        
        # Check for X-Frame-Options header
        x_frame_options = response.headers.get('X-Frame-Options', None)
        if x_frame_options:
            print(f"X-Frame-Options header found: {x_frame_options}")
        else:
            print("X-Frame-Options header is missing!")
        
        # Check for Content-Security-Policy header
        csp = response.headers.get('Content-Security-Policy', None)
        if csp and 'frame-ancestors' in csp:
            print(f"Content-Security-Policy (frame-ancestors) found: {csp}")
        else:
            print("Content-Security-Policy header is missing or doesn't include 'frame-ancestors'!")
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# URL to test
url_to_scan = input("Enter the URL to scan (include http/https): ")
check_clickjacking_protection(url_to_scan)
