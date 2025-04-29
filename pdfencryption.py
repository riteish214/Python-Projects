import pikepdf

# Open the original PDF
old_pdf = pikepdf.Pdf.open("a.pdf")

# Define permissions (disable content extraction)
permissions = pikepdf.Permissions(extract=False)

# Save the new PDF with encryption
old_pdf.save(
    "new.pdf",
    encryption=pikepdf.Encryption(
        user="123asd",      # Password required to open the PDF
        owner="ri",         # Owner password (can override restrictions)
        allow=permissions   # Permissions to apply
    )
)

print("PDF encrypted and saved as new.pdf")
