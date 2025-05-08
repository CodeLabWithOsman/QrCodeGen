# Import the qrcode module
import qrcode

# Define a function to create the QR code image
def create_qr_code(url):
    try:
        # Create a QRCode object with specific settings
        qr = qrcode.QRCode(
            version=1,         # Controls the size of the QR code (1 is the smallest)
            box_size=10,       # Size of each box (pixel) in the QR code
            border=4           # Thickness of the border (minimum is 4)
        )
        
        # Add the URL data to the QR code
        qr.add_data(url)
        qr.make(fit=True)  # Automatically adjust the size to fit the data

        # Create the image with colors (default: black on white)
        img = qr.make_image(fill_color="black", back_color="white")

        # Set output file path and save the image
        output_path = "qr_code.png"
        img.save(output_path)

        # Return success message
        return f"QR code saved as {output_path}! Scan it to visit the URL."
    
    except Exception as e:
        # Return an error message if something goes wrong
        return f"Error: {str(e)}. Check your URL."

# Main function to run the program
def main():
    print("=== QR Code Generator by @codelabwithosman ===")
    print("Turn a URL into a scannable QR code!")

    # Start an infinite loop to allow multiple inputs
    while True:
        # Ask the user to enter a URL
        url = input("Enter URL (or 'quit' to exit): ").strip()

        # Exit if user types 'quit'
        if url.lower() == "quit":
            print("Thanks for using! Follow @codelabwithosman for more tech hacks!")
            break

        # Validate the URL format
        if not url or not url.startswith(("http://", "https://")):
            print("Please enter a valid URL (e.g., https://example.com)")
            continue

        # Call the function to create the QR code and print the result
        result = create_qr_code(url)
        print(result)
        print()

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
