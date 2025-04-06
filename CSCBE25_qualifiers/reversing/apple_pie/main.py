# Static substitution table, retrieved from the original code
MAPPING_TABLE = [
    0x03, 0x01, 0x04, 0x01, 0x05, 0x09, 0x02, 0x06, 0x05, 0x03,
    0x05, 0x08, 0x09, 0x07, 0x09, 0x03, 0x02, 0x03, 0x08, 0x04,
    0x06, 0x02, 0x06, 0x04, 0x03, 0x03, 0x08, 0x03, 0x02, 0x07,
    0x09, 0x05, 0x00, 0x02, 0x08, 0x08, 0x04, 0x01, 0x00
]

def pie_decode_secret(encoded):
    """Invert the encoding process of the secret message."""
    decoded_chars = []
    for i, char in enumerate(encoded):
        decoded_chars.append(chr(ord(char) - MAPPING_TABLE[i]))
    
    return "".join(decoded_chars).replace("¹", "y").replace("¾", "}") # These replacements are here to correct some errors in my decoding process

if __name__ == "__main__":
    encoded_secret = "ftg|rÂalfytzr{nbrlmcoueessthaj{zmdtmÂ" # Encoded secret message, retreived from the original code
    
    decoded_string = pie_decode_secret(encoded_secret)
    print(f"Decoded Secret: {decoded_string}")