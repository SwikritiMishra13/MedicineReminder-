# Data Schema for data/medicines.json

Each medicine entry (list of objects):

{
  "id": <int>,
  "name": <string>,
  "dosage": <string>,
  "time": <string>,       # format "HH:MM AM/PM" or ISO "HH:MM"
  "status": <string>      # "pending" | "taken" | "missed"
}