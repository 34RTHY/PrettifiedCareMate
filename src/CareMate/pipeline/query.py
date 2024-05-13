
class getquerystr:
    def medical_coding_query(text) -> str:
        query_str = f"""
As a medical coding and billing tool,
you'll analyze clinical reports to suggest ICD, CPT, and HCPCS codes
for various medical terms, symptoms, diagnoses, treatments, and procedures.
Provide multiple relevant codes when necessary.

Here is the task: {text}

-----------Response Format-----------

\t- ICD 11 code: original text | code (code name) *Add more codes if relevant
\t- CPT code: original text | code (code name) *Add more codes if relevant
\t- HCPCS code: original text | code (code name) *Add more codes if relevant
*Add more Medical Terminology if relevent

-----------Response Format-----------
"""
        return query_str
    
    def patient_mode_query(Patient_input) -> str:
        query_str = f"""As a professional medical service, diagnose three possible diseases based on the provided data:{Patient_input}. Use bullet points to list diseases from most likely to least likely. Include reasons for each diagnosis.

If unsure, avoid sharing false information. Outline treatment options for each identified disease and specify whether the patient should seek professional medical attention or opt for self-care at a pharmacy.

Response in MarkDown Format:
## Possible diseases based on the symptoms described:
- **Name Of Disease 1** : Reason
- **Name Of Disease 2** : Reason
- **Name Of Disease 3** : Reason

## Treatments for each disease:
- **Name Of Disease 1** : Treatment 1
- **Name Of Disease 2** : Treatment 2
- **Name Of Disease 3** : Treatment 3


## Specify whether the patient should go to a doctor or pharmacy:
- **Answer**: Reason

## Next steps for the patient:
- **Answer** : Reason
"""
        return query_str
    
    def doctor_mode_query(patientdata) -> str:
        query_str = f"""As a professional medical health service provider, our task is to accurately assess possible diseases based on the given clinical laboratory test data and patient description, while ensuring the response remains faithful to the provided context. If the patient is healthy and unaffected, we will indicate that the patient's health is normal. We prioritize providing accurate information and refrain from sharing false information.

Patient Presentation:
The patient presents with the following clinical laboratory test data:
{patientdata}

Your task:
Please find below the possible diseases and reasons for their consideration, listed from most likely to least likely:
To assist the doctor in accurately diagnosing the symptoms, we recommend the following actions in priority order:
To enhance diagnostic accuracy, we suggest conducting the following laboratory tests in priority order:

-----RESPONSE in Markdown FORMAT-----

## Suggested Diagnosis:
- **Disease** : Reason
- **Disease** : Reason (if suspected)
- **Disease** : Reason (if suspected)

## Suggested Actions to Assist the Doctor:
- **Recommendation** : Reason
- **Recommendation** : Reason (if relevant)
- **Recommendation** : Reason (if relevant)

## Suggested Laboratory Tests for Precise Diagnosis:
- **Test** : Reason
- **Test** : Reason (if relevant)
- **Test** : Reason (if relevant)

-----RESPONSE FORMAT-----
"""
        return query_str