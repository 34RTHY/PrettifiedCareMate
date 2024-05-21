import streamlit as st
class medicalcoding:
    def splitcodes(unsorted_suggested_medical_codes):
        ICD_code_list = []
        CPT_code_list = []
        HCPCS_code_list = []

        for i in unsorted_suggested_medical_codes.split('\n'):
            tmp_string = i.replace('*Add more codes if relevant', '')
            try:
                if tmp_string[0] == '-' and 'Not' not in tmp_string and 'not' not in tmp_string:
                    if 'ICD' in tmp_string:
                        ICD_code_list.append(tmp_string)
                    elif 'CPT' in tmp_string:
                        CPT_code_list.append(tmp_string)
                    elif 'HCPCS' in tmp_string:
                        HCPCS_code_list.append(tmp_string)
            except:
                continue

        Suggested_ICD_11_Codes_Text = "\n".join([ '\t' + "".join(i.split(': ')[1:]) for i in ICD_code_list])
        Suggested_CPT_Codes_Text = "\n".join([ '\t' + "".join(i.split(': ')[1:]) for i in CPT_code_list])
        Suggested_HCPCS_Codes_Text = "\n".join([ '\t' + "".join(i.split(': ')[1:]) for i in HCPCS_code_list])

        return Suggested_ICD_11_Codes_Text,Suggested_CPT_Codes_Text,Suggested_HCPCS_Codes_Text
    
    def outputmedcode(Suggested_ICD_11_Codes_Text,Suggested_CPT_Codes_Text,Suggested_HCPCS_Codes_Text):
        with st.container(border = True):
            st.markdown('## Suggested ICD 11 Codes')
            for Each_code in Suggested_ICD_11_Codes_Text.split('\t'):
                if Each_code.strip() == '' or Each_code == None or None:
                    continue
                str_list = Each_code.split('|')
                Symptom_name = str_list[0].strip()
                try:
                    Code_name = str_list[1].strip()
                except:
                    Code_name = str_list[0].strip()
                st.markdown(f'- **{Symptom_name}** : {Code_name}')
        with st.container(border = True):
            st.markdown('## Suggested CPT Codes')
            for Each_code in Suggested_CPT_Codes_Text.split('\t'):
                if Each_code.strip() == '' or Each_code == None or None:
                    continue
                str_list = Each_code.split('|')
                Symptom_name = str_list[0].strip()
                try:
                    Code_name = str_list[1].strip()
                except:
                    Code_name = str_list[0].strip()
                st.markdown(f'- **{Symptom_name}** : {Code_name}')
        with st.container(border = True):
            st.markdown('## Suggested HCPCS Codes')
            for Each_code in Suggested_HCPCS_Codes_Text.split('\t'):
                if Each_code.strip() == '' or Each_code == None or None:
                    continue
                str_list = Each_code.split('|')
                Symptom_name = str_list[0].strip()
                try:
                    Code_name = str_list[1].strip()
                except:
                    Code_name = str_list[0].strip()
                st.markdown(f'- **{Symptom_name}** : {Code_name}')
    