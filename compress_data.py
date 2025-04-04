import zlib

# Get user input
user_input = input("Enter a string to compress: ")

# Compress the string
compressed_data = zlib.compress(user_input.encode())
print("Compressed Data:", compressed_data)

# Decompress the string
decompressed_data = zlib.decompress(compressed_data).decode()
print("Decompressed Data:", decompressed_data)