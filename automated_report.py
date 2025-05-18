# Import required libraries
import pandas as pd
from fpdf import FPDF

# Define file path
csv_file = "data.csv"

# Step 1: Load data from CSV
try:
    data = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found.")
    exit()

# Step 2: Analyze data
average = data["Score"].mean()
maximum = data["Score"].max()
minimum = data["Score"].min()
top_scorer = data.loc[data["Score"].idxmax(), "Name"]

# Step 3: Create a PDF report using FPDF
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Score Report", ln=True, align="C")
        self.ln(10)

    def summary(self, avg, max_, min_, top):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Average Score: {avg:.2f}", ln=True)
        self.cell(0, 10, f"Highest Score: {max_} (by {top})", ln=True)
        self.cell(0, 10, f"Lowest Score: {min_}", ln=True)
        self.ln(10)

    def table(self, data):
        self.set_font("Arial", "B", 12)
        self.cell(60, 10, "Name", 1)
        self.cell(40, 10, "Score", 1)
        self.ln()
        self.set_font("Arial", "", 12)
        for _, row in data.iterrows():
            self.cell(60, 10, row["Name"], 1)
            self.cell(40, 10, str(row["Score"]), 1)
            self.ln()

# Create and generate the report
pdf = PDFReport()
pdf.add_page()
pdf.summary(average, maximum, minimum, top_scorer)
pdf.table(data)
pdf.output("automated_report.pdf")

print("Report generated successfully: automated_report.pdf")
