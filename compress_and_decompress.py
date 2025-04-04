import zlib
data = input("Enter a string: ").encode()
compressed = zlib.compress(data)
print("Compressed:", compressed)
print("Decompressed:", zlib.decompress(compressed).decode())