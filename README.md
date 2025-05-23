# AUTOMATED-REPORT-GENERATION

Company : Codtech IT solution

Name : Harshada Ashoksingh Rajput

Intern ID : CT04DL620

Domain : Python Programming

Duration : 4 weeks

Mentor : Neela Santhosh

*Description* : 
This project focuses on automating the generation of formatted PDF reports from a structured CSV file. It demonstrates how to use Python to:
-Read and process data from a file,
-Perform basic analysis or transformation,
-Format and export the data into clean, professional-looking PDF documents using the FPDF library.
project overview
1. Data Input and Processing
The script reads data from a CSV file called landmarks.csv, where each row contains details about a famous tourist landmark in a single comma-separated string.
It splits each row into multiple fields:
*Name
*Location
*Best Time to Visit
*Rating
*Description
2. PDF Report Generation
-Loops through each row in the dataset.
-Uses the FPDF library to:
-Add a page for each report,
-Set font and layout,
-Insert information like the name, location, rating, etc.,
-Use multi_cell() for multi-line descriptions.
-Each report is saved as a PDF file with a name based on the landmark's name (spaces replaced with underscores).

*Output* : 
PDF saved for name.
PDF saved for Eiffel Tower.
PDF saved for red fort .
PDF saved for Amer fort.
All the reports ares generated successfully
![Image](https://github.com/user-attachments/assets/b3d3c101-aa2e-4af8-954f-7f2229866dbc)
![Image](https://github.com/user-attachments/assets/34e5f8d0-6ab2-4f99-9c2e-0a8df5e2273b)
![Image](https://github.com/user-attachments/assets/f1dafa62-bfd8-4e62-be5d-06bc4c39d61d)
