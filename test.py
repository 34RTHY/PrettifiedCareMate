unsorted_suggested_medical_codes = """
Here are the medical codes organized and presented as requested:

- **ICD 11 code:**
  - Multiple injuries of wrist or hand, unspecified | MDC90.Z (Multiple injuries of wrist or hand, unspecified)
  - Other specified multiple injuries of wrist or hand | MDC90.Y (Other specified multiple injuries of wrist or hand)
  - Injury of multiple sites of wrist | MDC90.1 (Injury of multiple sites of wrist)
  - Mouth ulcers | 6B72.0 (Mouth ulcers)
  - Seropositive rheumatoid arthritis | FA20.0 (Seropositive rheumatoid arthritis)
  - Seronegative rheumatoid arthritis | FA20.1 (Seronegative rheumatoid arthritis)
  - Systemic lupus erythematosus, unspecified | M32.9 (Systemic lupus erythematosus, unspecified)
  - Other specified pericarditis | BB2Y (Other specified pericarditis)
  - Postinfectious arthropathies, unspecified | FA12.Z (Postinfectious arthropathies, unspecified)
  - Disorder of skin, unspecified | 6B72.Z (Disorder of skin, unspecified)

- **CPT code:**
  - Incision and drainage of abscess; simple or single | 25000 (Incision and drainage of abscess; simple or single)
  - Incision and drainage of abscess; complicated or multiple | 25005 (Incision and drainage of abscess; complicated or multiple)
  - Biopsy of oral tissue, single lesion | 40805 (Biopsy of oral tissue, single lesion)
  - Immunization administration through age 18 years, with counseling by physician or other qualified health care professional; first or only component of each vaccine or toxoid component administered | 90765 (Immunization administration)
  - Therapeutic, prophylactic, or diagnostic injection; subcutaneous or intramuscular | 96372 (Therapeutic, prophylactic, or diagnostic injection; subcutaneous or intramuscular)   
  - Office or other outpatient visit for the evaluation and management of a new patient | 99201-99205 (Office or other outpatient visit for the evaluation and management of a new patient)
  - Office or other outpatient visit for the evaluation and management of a new patient | 99203 (Office or other outpatient visit for the evaluation and management of a new patient)

- **HCPCS code:**
  - Contusion of right wrist, initial encounter | S60.811A (Contusion of right wrist, initial encounter)
  - Contusion of left wrist, initial encounter | S60.812A (Contusion of left wrist, initial encounter)
  - Oral pain management, initial encounter | G9382 (Oral pain management, initial encounter)
  - Injection, ketorolac tromethamine, per 15 mg | J0129 (Injection, ketorolac tromethamine, per 15 mg)
  - Injection, infliximab, excludes biosimilar, 10 mg | J1745 (Injection, infliximab, excludes biosimilar, 10 mg)
  - Injection, triamcinolone acetonide, not otherwise specified, per 10 mg | J1890 (Injection, triamcinolone acetonide, not otherwise specified, per 10 mg)
"""

def splitcodes(unsorted_suggested_medical_codes):
    Suggested_ICD_11_Codes_Text = ""
    Suggested_CPT_Codes_Text = ""
    Suggested_HCPCS_Codes_Text = ""
    
    for section in unsorted_suggested_medical_codes.split('\n\n'):
        clean_section = section.replace('*Add more codes if relevant', '').strip()
        if '- **ICD 11 codes:**' in section:
            Suggested_ICD_11_Codes_Text = clean_section.replace('- **ICD 11 codes:**', '').strip()
        elif '- **CPT codes:**' in section:
            Suggested_CPT_Codes_Text = clean_section.replace('- **CPT codes:**', '').strip()
        elif '- **HCPCS codes:**' in section:
            Suggested_HCPCS_Codes_Text = clean_section.replace('- **HCPCS codes:**', '').strip()

    # Remove leading spaces before hyphens
    Suggested_ICD_11_Codes_Text = "\n".join([line.strip() for line in Suggested_ICD_11_Codes_Text.split('\n')])
    Suggested_CPT_Codes_Text = "\n".join([line.strip() for line in Suggested_CPT_Codes_Text.split('\n')])
    Suggested_HCPCS_Codes_Text = "\n".join([line.strip() for line in Suggested_HCPCS_Codes_Text.split('\n')])

    print(Suggested_ICD_11_Codes_Text)
    print(Suggested_CPT_Codes_Text)
    print(Suggested_HCPCS_Codes_Text)
    return Suggested_ICD_11_Codes_Text, Suggested_CPT_Codes_Text, Suggested_HCPCS_Codes_Text


Suggested_ICD_11_Codes_Text,Suggested_CPT_Codes_Text,Suggested_HCPCS_Codes_Text = splitcodes(unsorted_suggested_medical_codes)

print('############################################################')
print("Suggested ICD-11 Codes:##############################")
print(Suggested_ICD_11_Codes_Text)
print("Suggested ICD-11 Codes:##############################")
print(Suggested_CPT_Codes_Text)
print("Suggested ICD-11 Codes:##############################")
print(Suggested_HCPCS_Codes_Text)
