import json

def save_memory(role):
    with open("interview_memory.json", "w") as file:
        json.dump({"role": role}, file)

def load_memory():
    try:
        with open("interview_memory.json", "r") as file:
            data = json.load(file)
            return data.get("role", "No previous role")
    except:
        return "No previous role"