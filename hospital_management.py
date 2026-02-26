def search_by_disease(patients, disease):
    result = [patient["Name"] for patient in patients if patient["Disease"] == disease]
    return result


# Example Input
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

disease = "Flu"
result = search_by_disease(patients, disease)

print(f"Patients with {disease}:", result)