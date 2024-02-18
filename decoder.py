import base64
import time

def decode_string(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')
    
    # Decode the bytes from base64
    decoded_bytes = base64.b64decode(input_bytes)
    
    # Convert the decoded bytes back to string
    decoded_string = decoded_bytes.decode('utf-8')
    
    return decoded_string

# Test the function
test_string = input("Enter your string that you want to decode. ")
print("Decoding...")
time.sleep(3)
print(f"Encoded String: {test_string}")
print(f"Decoded String: {decode_string(test_string)}")
time.sleep(15)