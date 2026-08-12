student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"}
}

print(student_data)

print("Accessing id1:", student_data.get("id1", "Not Found"))
print("Accessing id5 (before adding):", student_data.get("id5", "Not Found"))

student_data["id5"] = {"name": "Ananya", "class": "V", "subject": "science, math, art"}
print(student_data)

student_data["id2"]["subject"] = "english, math, computer science"
print("Updated id2 details:", student_data["id2"])

cleaned_data = {}
seen_records = []

for key, details in student_data.items():
    record_tuple = (details["name"], details["class"], details["subject"])
    if record_tuple not in seen_records:
        seen_records.append(record_tuple)
        cleaned_data[key] = details

student_data = cleaned_data
print(student_data)

student_data.pop("id4", None)
print(f"Remaining student records count: {len(student_data)}")

for student_id, details in student_data.items():
    print(f"ID: {student_id} | Name: {details['name']} | Class: {details['class']} | Subject: {details['subject']}")