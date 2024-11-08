import struct
import argparse
import os

def parse_git_index(index_path):
    with open(index_path, 'rb') as f:
        # Read the index header
        header = f.read(12)
        signature, version, num_entries = struct.unpack('!4sII', header)

        # Check if the file is a valid Git index
        if signature != b'DIRC':
            raise ValueError("The file is not a valid Git index.")
        print(f"Index version: {version}, Number of entries: {num_entries}")

        # List to store the filenames
        filenames = []

        for _ in range(num_entries):
            # Read the index entry
            try:
                # Try to read the 62 bytes of metadata for each entry
                entry_header = f.read(62)
                if len(entry_header) < 62:
                    raise ValueError("Incomplete entry in the index file.")
                
                # Unpack only the main required fields
                unpacked_data = struct.unpack('!10I20sH', entry_header)
                sha1 = unpacked_data[9]  # Keep SHA-1 only as a reference for checking
                
                # The filename field has a variable length
                name_bytes = b''
                while True:
                    byte = f.read(1)
                    if byte == b'\x00':
                        break
                    name_bytes += byte
                filename = name_bytes.decode('utf-8', errors='replace')
                filenames.append(filename)

                # Advance to the next entry block (8-byte alignment)
                padding = (8 - (len(entry_header) + len(name_bytes) + 1) % 8) % 8
                f.read(padding)

            except struct.error as e:
                print(f"Error reading an entry: {e}")
                break

        return filenames

def main():
    # Configure command-line arguments
    parser = argparse.ArgumentParser(description="List files in the Git index and save them to a .txt file")
    parser.add_argument("index_path", help="Path to the index file (.git/index)")
    parser.add_argument("output_file", help="Name of the output file (e.g., files.txt)")
    args = parser.parse_args()

    # Check if the index file exists
    if not os.path.isfile(args.index_path):
        print(f"Error: The file '{args.index_path}' does not exist.")
        return

    # Parse the index and get the filenames
    try:
        filenames = parse_git_index(args.index_path)
        
        # Save the listing to the output file with UTF-8 encoding
        with open(args.output_file, 'w', encoding='utf-8') as output_file:
            for filename in filenames:
                output_file.write(filename + '\n')
        
        print(f"File listing saved in '{args.output_file}'.")

    except Exception as e:
        print(f"Error reading the index file: {e}")

if __name__ == "__main__":
    main()
