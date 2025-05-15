#run this code on any online python compiler replace the device_id with your id which will be shown when you start the notepad.exe file 
import hashlib

def compute_key(device_id: str) -> str:
    sha256_hash = hashlib.sha256(device_id.encode('utf-8')).hexdigest().upper()
    key = (
        "F" +
        sha256_hash[0:5] + "-" +
        sha256_hash[5:10] + "-" +
        sha256_hash[10:15] + "-" +
        sha256_hash[15:20] + "-" +
        sha256_hash[20:25] +
        "F"
    )
    return key

device_id = "c2b89211-64ee-48c8-b196-58d7b695e2be"
print("Generated Key:", compute_key(device_id))
