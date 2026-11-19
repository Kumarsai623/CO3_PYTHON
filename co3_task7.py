import re
import time
import random

# Normalise phone number
def normalise_number(number):
    if not number:
        return ""

    digits = "".join(
        character for character in number
        if character.isdigit()
    )

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits

# Normalise name
def normalise_name(name):
    return " ".join(name.strip().lower().split())

# Merge contacts
def merge_contacts(contacts):
    merged = {}
    missing_phone = []

    for contact in contacts:
        name = contact.get("name", "").strip()
        phone = normalise_number(contact.get("phone", ""))
        email = contact.get("email", "").strip().lower()

        if not phone:
            missing_phone.append({
                "name": name,
                "email": email
            })
            continue

        if phone not in merged:
            merged[phone] = {
                "names": set(),
                "phones": set(),
                "emails": set()
            }

        if name:
            merged[phone]["names"].add(name)

        merged[phone]["phones"].add(phone)

        if email:
            merged[phone]["emails"].add(email)

    return merged, missing_phone

# Sample contacts
contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "RAVI@gmail.com"
    },
    {
        "name": "ravi kumar",
        "phone": "9840012345",
        "email": "ravi@example.com"
    },
    {
        "name": "Anu",
        "phone": "9876543210",
        "email": "anu@gmail.com"
    },
    {
        "name": "Ravi",
        "phone": "98400-12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Unknown",
        "phone": "",
        "email": "unknown@gmail.com"
    }
]

merged, missing = merge_contacts(contacts)

print("Merged Contacts:")

for phone, details in merged.items():
    print("\nPhone:", phone)
    print("Names:", sorted(details["names"]))
    print("Numbers:", sorted(details["phones"]))
    print("Emails:", sorted(details["emails"]))

print("\nContacts with missing phone:", missing)

# Verify a small result manually
print("\nNumber of merged contacts:", len(merged))

# Performance experiment
for size in [1000, 100000]:
    large_contacts = []

    for i in range(size):
        number = str(9000000000 + (i // 2))

        large_contacts.append({
            "name": "Person " + str(i),
            "phone": number,
            "email": "person" + str(i) + "@example.com"
        })

    start = time.perf_counter()
    result, missing_result = merge_contacts(large_contacts)
    elapsed = time.perf_counter() - start

    print("\nInput contacts:", size)
    print("Merged contacts:", len(result))
    print("Execution time:", elapsed)
