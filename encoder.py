import base64
import time

def encode_string(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')
    
    # Encode the bytes to base64
    encoded_bytes = base64.b64encode(input_bytes)
    
    # Convert the encoded bytes back to string
    encoded_string = encoded_bytes.decode('utf-8')
    
    return encoded_string

# Test the function
test_string = input("Enter your string that you want to encode. ")
print("Encoding...")
time.sleep(3)
print(f"Original String: {test_string}")
print(f"Encoded String: {encode_string(test_string)}")
time.sleep(15)