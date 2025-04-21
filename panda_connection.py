import pandas as pd

# Create Data
data = {
    "Roll Number":list(range(1, 21)),
    "Name": [ "Nitish", "Keval", "Kunal", "Arvind", "Arshiyan", "Tejaswini", "Aastha", "Aditee", "Shivam", "Nitu", 
                "Janhvi", "Meena", "Dwisha", "Mahamud", "Ganesh", "Ashmita", "Shatabdi", "Vishal", "Yash", "Om"],
    "Phone Number": [9373937166, 8347840284, 9616295389, 8899775133, 6688571455, 8965238942, 9758461235, 9999888857, 7895462351, 8978856400,
                        7984651320, 9845326176, 8479561253, 9878654312, 6688571455, 8965238942, 9758461235, 9999888857, 7895462351, 8978856400],
    "Class": ['MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA','MCA'],
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first 5 records
print("First 5 records:\n",df.head())

# Display last 5 records
print("\nLast 5 records:\n",df.tail())

# Check for null values
print("\nCheck for null values:\n",df.isnull().sum())