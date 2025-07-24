import hashlib

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return "File not found. Please check the file path."

if __name__ == "__main__":
    # Prompt the user for the file name
    file_path = input("Enter the path of the file to calculate its checksum: ")
    
    checksum = calculate_md5(file_path)
    print(f"MD5 Checksum for {file_path}: {checksum}")
