import os
import PyPDF2
import re
import shutil

def extract_name_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()

            # Extract the name using regular expression
            pattern = r'Name :\s*(.*?)\n'
            match = re.search(pattern, text)
            if match:
                name = match.group(1).strip()
                return name

    # If name is not found
    return None

# Prompt the user to enter the folder name
folder_path = input("Enter the folder name: ")

# Extract the base name of the input folder
folder_name = os.path.basename(folder_path)

# Create a new folder to store renamed files
new_folder_name = f"Renamed_Files_{folder_name}"
new_folder_path = os.path.join(os.getcwd(), new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# Extract the name from all PDF files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".pdf"):
            pdf_file_path = os.path.join(root, file)
            name = extract_name_from_pdf(pdf_file_path)
            if name:
                # Remove periods from names
                name = name.replace(".", "")
                # Rename the file as "name_original_file_name"
                new_file_name = f"{name}_{file}"
                new_file_path = os.path.join(new_folder_path, new_file_name)
                # Copy the file to the new folder with the renamed file name
                shutil.copy2(pdf_file_path, new_file_path)
                print(f"File copied: {new_file_path}")
            else:
                print(f"No name found in {pdf_file_path}.")
