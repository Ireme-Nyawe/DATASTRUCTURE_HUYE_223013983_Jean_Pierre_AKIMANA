# Hospital Patient Queue Management

This Python program simulates a hospital queue management system. Patients are registered based on their priority (emergency cases come first). It allows undoing patient registrations and processing patients with the highest priority first using a queue.

## Features

1. **Register Patients:** Register patients with their details (Name, Age, Condition, and Priority).
2. **Undo Registration:** Undo the most recent patient registration.
3. **Process Patients:** Process patients in the order of their priority, with higher priority patients processed first.

## How to Use

1. **Register Patients:** Enter patient details such as name, age, condition, and priority. The priority determines their place in the queue (lower number means higher priority).
2. **Undo Registrations:** Undo the most recent patient registration if needed.
3. **Process Patients:** Process patients based on the queue, starting from the highest priority patient.

## Exmple to test
### Register
`registerPatient("Mucyo Jean", 30, "Malaria", 4)`


### Undoing
`undoRegistration()`


### process
`processPatient()`

-------------------------------------------------------------------------------------
# Participants 
| S/N | REG        | Last Name   | First Name     |
|-----|------------|-------------|----------------|
| 1   | 223013983  | AKIMANA     | Jean Pierre    |             
| 2   | 223007511  | NIYONSABA   | Erina          |   
| 3   | 223004810  | NIYONSENGA  | Ange Carine    |             
| 4   | 223016138  | Niyonsenga  | Aphrodis       |             
| 5   | 223011216  | NIYONSHUTI  | Florence       |             
| 6   | 223011370  | NICYOGIHE   | Rebeca         |             
| 7   | 221007304  | MUTONI      | AIMABLE        |             
| 8   | 223018803  | MUKAMA      | UYISENGA Lea   |       
| 9   | 223010019  | MUKAMAKOM   | BE Violette    |        
| 10  | 223009957  | MUNEZERO    | Grace          |         


