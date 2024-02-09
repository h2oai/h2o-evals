import pandas as pd
import json
import uuid

def csv_to_json(csv_file):
    tests = []
    test_cases = []
    test_key = str(uuid.uuid4())
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        question = row['question']
        question_type = row['question_type']
        answer = (row['answer'])

        prompt = f"Question: {question}\n"

        test_cases.append({
            "key": str(uuid.uuid4()),
            "prompt": prompt,
            "categories": [question_type],
            "constraints": [""],
            "expected_output": [answer]
        })

    tests.append({
            "key": test_key,
            "documents": ['question_type_telcom.pdf'],
            "test_cases": test_cases
        })   

    return {"tests": tests}

csv_file = './Telcom_T-TUT-PROTO-2019-PDF-E/question_type_telcom.csv'
# json_file = 'multi_choice_financial_statement_output.json'
json_data = csv_to_json(csv_file)

with open(f"{csv_file.split('/')[-1].split('.')[0]}_output.json", 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
