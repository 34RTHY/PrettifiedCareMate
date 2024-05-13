from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from datetime import datetime
import PyPDF2
import docx
import io
import streamlit as st
class writer:
    def extract_text_from_txt(file_contents):
        return file_contents.decode("utf-8")

    def extract_text_from_docx(file_contents):
        doc = docx.Document(io.BytesIO(file_contents))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text

    def extract_text_from_pdf(file_contents):
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_contents))
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
        return text
    
    def Gettextfromfile(file_contents, file_type):
        if file_type == "text/plain":
            return writer.extract_text_from_txt(file_contents)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return writer.extract_text_from_docx(file_contents)
        elif file_type == "application/pdf":
            return writer.extract_text_from_pdf(file_contents)
        else:
            st.error("Unsupported file format.")
    def calculate_height(str_list):
            page_height = 0
            max_width = 512  # Maximum width
            line_height = 15  # Height of each line

            for paragraph in str_list:
                for line in paragraph.split('\n'):
                    words = line.split()
                    foo = ''  # Initialize line string
                    for word in words:
                        if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < max_width:
                            foo += ' ' + word if foo else word  # Add word to line
                        else:
                            page_height += line_height  # Increase page height
                            foo = word  # Start new line with current word
                    page_height += line_height  # Increase page height for new line
            return page_height

    def generate_medical_code_report(Suggested_ICD_11_Codes_Text, Suggested_CPT_Codes_Text, Suggested_HCPCS_Codes_Text, output_path):
        page_height = writer.calculate_height([Suggested_ICD_11_Codes_Text,Suggested_CPT_Codes_Text,Suggested_HCPCS_Codes_Text])+300
        wxh_page = (612.0,page_height)
        y_offset = page_height
        c = canvas.Canvas(output_path, pagesize=wxh_page)

        # Report title and generated time
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_offset-52, "Symptoms Assessment Report")
        generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.drawString(100, y_offset-72, f"Generated time: {generated_time}")

        # Patient's Information section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset-102, "Suggested ICD 11 Codes")
        c.line(100, y_offset-107, 500, y_offset-107)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset = y_offset-122
        for line in Suggested_ICD_11_Codes_Text.split('\n'):
            words = line.split()
            foo = '-'
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # Patient's Symptoms section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Suggested CPT Codes")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Suggested_CPT_Codes_Text.split('\n'):
            words = line.split()
            foo = '-'
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # CareMate Suggestion section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Suggested HCPCS Codes")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Suggested_HCPCS_Codes_Text.split('\n'):
            words = line.split()
            foo = '-'
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15
        c.save()

    def generate_patient_mode_report(Possible_diseases, Treatments_for_each_disease,doctor_or_pharmacy,Next_steps_for_the_patient, output_path):
        page_height = writer.calculate_height([Possible_diseases,Treatments_for_each_disease,doctor_or_pharmacy,Next_steps_for_the_patient])+300
        wxh_page = (612.0,page_height)
        y_offset = page_height
        c = canvas.Canvas(output_path, pagesize=wxh_page)

        # Report title and generated time
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_offset-52, "Symptoms Assessment Report")
        generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.drawString(100, y_offset-72, f"Generated time: {generated_time}")

        # Patient's Information section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset-102, "Possible diseases based on the symptoms described")
        c.line(100, y_offset-107, 500, y_offset-107)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset = y_offset-122
        for line in Possible_diseases.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # Patient's Symptoms section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Treatments for each disease")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Treatments_for_each_disease.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # CareMate Suggestion section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Specify whether the patient should go to a doctor or pharmacy")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in doctor_or_pharmacy.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Next steps for the patient")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Next_steps_for_the_patient.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        c.save()

    def generate_doctor_mode_report(Suggested_Diagnosis, Suggested_Actions,Suggested_Laboratory_Tests,output_path):
        page_height = writer.calculate_height([Suggested_Diagnosis,Suggested_Actions,Suggested_Laboratory_Tests])+300
        wxh_page = (612.0,page_height)
        y_offset = page_height
        c = canvas.Canvas(output_path, pagesize=wxh_page)

        # Report title and generated time
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_offset-52, "Symptoms Assessment Report")
        generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.drawString(100, y_offset-72, f"Generated time: {generated_time}")

        # Patient's Information section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset-102, "Suggested Diagnosis")
        c.line(100, y_offset-107, 500, y_offset-107)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset = y_offset-122
        for line in Suggested_Diagnosis.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # Patient's Symptoms section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Suggested Actions to Assist the Doctor")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Suggested_Actions.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        # CareMate Suggestion section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_offset - 20, "Suggested Laboratory Tests for Precise Diagnosis")
        c.line(100, y_offset - 25, 500, y_offset - 25)  # Horizontal line
        c.setFont("Helvetica", 10)
        y_offset -= 40
        for line in Suggested_Laboratory_Tests.split('\n'):
            words = line.split()
            foo = ''
            for word in words:
                if stringWidth(foo + ' ' + word, "Helvetica-Bold", 12) < 512:
                    foo += ' ' + word if foo else word
                else:
                    foo = foo.replace('|',':')
                    c.drawString(100, y_offset, foo)
                    y_offset -= 15
                    foo = word
            foo = foo.replace('|',':')
            c.drawString(100, y_offset, foo)
            y_offset -= 15

        c.save()