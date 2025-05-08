import qrcode

def create_qr_code(url):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        output_path = "qr_code.png"
        img.save(output_path)
        return f"QR code saved as {output_path}! Scan it to visit the URL."
    except Exception as e:
        return f"Error: {str(e)}. Check your URL."

def main():
    print("=== QR Code Generator by @codelabwithosman ===")
    print("Turn a URL into a scannable QR code!")
    while True:
        url = input("Enter URL (or 'quit' to exit): ").strip()
        if url.lower() == "quit":
            print("Thanks for using! Follow @codelabwithosman for more tech hacks!")
            break
        if not url or not url.startswith(("http://", "https://")):
            print("Please enter a valid URL (e.g., https://example.com)")
            continue
        result = create_qr_code(url)
        print(result)
        print()

if __name__ == "__main__":
    main()
