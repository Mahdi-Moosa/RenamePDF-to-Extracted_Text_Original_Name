# RenamePDF-to-Extracted_Text_Original_Name

Steps:
- Asks for input Folder
- Create an output folder named as {Renamed_Files}_{Input_Folder}
- Fetches _Names_ from the PDF file(s). Logic - extract all texts after "Name :" till the first new-line character.
- Copy each file to the newly created {Renamed_Files}\_{Input_Folder} with file name renamed as {Extracted_Name}_{Original_PDF_File_Name).
