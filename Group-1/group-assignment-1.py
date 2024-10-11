# Hospital Patient Queue Management: Registers patients based on priority, 
# allows undoing registrations, and processes patients with higher priority first(queue based on priority).

from collections import deque

patient_list = []
patient_queue = deque()
un_registered = []

def registerPatient(name, age, condition, priority):
    patient = {"Name": name, "Age": age, "Condition": condition, "Priority": priority}
    patient_list.append(patient)
    
    if not patient_queue:
        patient_queue.append(patient)
    else:
        inserted = False
        for i, exPatient in enumerate(patient_queue):            
            if exPatient["Priority"] < patient["Priority"]:
                patient_queue.insert(i, patient)
                inserted = True
                break
        
        if not inserted:
            patient_queue.append(patient)

def undoRegistration():
    if patient_list:
        undonePatient = patient_list.pop()
        patient_queue.remove(undonePatient)
        print(f"Undone registration: {undonePatient['Name']}")
    else:
        print("No Patient Found")

def processPatient():
    if patient_queue:
        patient = patient_queue.popleft()
        print(f"Processing Patient: {patient['Name']}")
    else:
        print("No Patient Found")

# Test the program functionalities

# here we have done all system functionalities let's test one by one

# call register function to register patient
registerPatient("Mucyo Jean", 30, "Malaria", 4)
registerPatient("Muhire David", 45, "Broken Leg", 1)
registerPatient("Mukiza Alice", 23, "Cold", 2)
registerPatient("Mugisha Patrick", 35, "Typhoid", 3)
registerPatient("Aline Uwase", 50, "Pneumonia", 5)
registerPatient("Nshuti Eric", 29, "Flu", 2)
registerPatient("Ines Kamikazi", 32, "Malaria", 1)
registerPatient("Iradukunda Anita", 40, "Broken Leg", 3)
registerPatient("Mutesi Diane", 28, "Cold", 4)
registerPatient("Patrick Mugabo", 42, "Typhoid", 2)
registerPatient("Uwase Marie", 31, "Pneumonia", 5)
registerPatient("Niyonzima Eric", 33, "Flu", 3)
registerPatient("Kamikazi Aline", 34, "Malaria", 1)
registerPatient("Murenzi Samuel", 48, "Broken Leg", 4)
registerPatient("Gakuba Peter", 27, "Cold", 5)
registerPatient("Mukeshimana Rose", 39, "Typhoid", 3)
registerPatient("Habimana Claude", 41, "Pneumonia", 2)
registerPatient("Kamanzi Olivier", 25, "Flu", 4)
registerPatient("Nzeyimana Frank", 36, "Malaria", 1)
registerPatient("Uwimana Fabiola", 47, "Broken Leg", 5)


# test undoing registration
undoRegistration()
undoRegistration()
undoRegistration()
undoRegistration()
undoRegistration()

# test proccessing patient
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()
processPatient()


print(f"All Registered Patients: {patient_list}")
print(f"All Patients In Queue: {list(patient_queue)}")
