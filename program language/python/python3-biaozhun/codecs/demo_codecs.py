import codecs

# r1 = codecs.encode("\xe9\x92\x9f", encoding="ascii", errors='surrogateescape').replace(rb"\x", b"").decode()
r1 = "\xe9\x92\x9f".encode(encoding="ascii", errors="backslashreplace").replace(b"\\x", b"").decode()
r1 = bytes.fromhex(r1).decode()
r2 = codecs.decode(b'\xe9\x92\x9f')
r3 = 0x8000 << 48

print(type(r1), r1)
print(type(r2), r2)
print(type(r3), r3)

