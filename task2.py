import pandas as pd
from fpdf import FPDF
import os

# Read data from CSV file
data = pd.read_csv("landmarks.csv", names=['landmark'], encoding='latin1')

data[['Name', 'Location', 'Best Time', 'Rating', 'Description']] = data['landmark'].str.split(',', expand=True)

# Create a directory for reports if it doesn't exist
if not os.path.exists("tour_reports"):
    os.mkdir("tour_reports")

# Generate PDF reports
for index, row in data.iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, f"Name: {row['Name']}", ln=True)
    pdf.cell(0, 10, f"Location: {row['Location']}", ln=True)
    pdf.cell(0, 10, f"Best Time: {row['Best Time']}", ln=True)
    pdf.cell(0, 10, f"Rating: {row['Rating']}", ln=True)
    pdf.multi_cell(0, 10, f"Description: {row['Description']}")

    pdf.output(f"tour_reports/{row['Name'].replace(' ', '_')}.pdf")
    print(f"PDF saved for {row['Name']}.")

print("All the reports ares generated successfully.")
