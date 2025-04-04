<<<<<<< HEAD
import zlib
data = input("Enter a string: ").encode()
compressed = zlib.compress(data)
print("Compressed:", compressed)
print("Decompressed:", zlib.decompress(compressed).decode())
=======
# Example of compress and decompress in python.

import zlib

data = input("Enter a string: ").encode()
compressed = zlib.compress(data)

print("Compressed:", compressed)
print("Decompressed:", zlib.decompress(compressed).decode())
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
