KEYS = [
"ST-0001-a36e904f9431ff6b18079881a20af2b3403b86b4a6bace5f3a6a47e945b95cce937c415bedaad6c86bb86b59f0b1d137442537a8",
"ST-0002-708e558bec86c4222185c944e92b15d1c83298a7e0697682b8904371b506eae7216be45c662ce73710cf5247f4381b2971cf9014",
"ST-0003-310c8cf65504794702b5d29f74aa8f5d7a2a68448d57732b8bc2278a8c6526ebb2820d41a9f809a56e8b542ec029ff20ff3f0d08",
"ST-0004-9eeb558b5502a826d67b0bddb25f06fe4014d97aff40a5674e35b9dcc4e696b9a720e25f2ad8ae5b9b63b993dcf826258e65ae5b",
]

hash160= "b4a8ec2c59e5d11f3df37a01ecc1b979d41c3c4a"
address = "5KLgpBYPoeKfuqE2gtx7RzTBxFbhWnyg5w2VwS3vkXRRWCfuCpd"
print(len(KEYS[0]))
from secretsharing import PlaintextToHexSecretSharer
shares = PlaintextToHexSecretSharer.split_secret(address, 2, 4)

print(shares)
for i in shares:
	print(len(i))