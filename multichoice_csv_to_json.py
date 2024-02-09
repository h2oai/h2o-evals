import pandas as pd
import json
import uuid

def csv_to_json(csv_file):
    tests = []
    test_cases = []
    test_key = str(uuid.uuid4())
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        
        try:
            question = row['question']
            choices = eval(row['choices'])
            answer_index = int(row['answer'])
            answer = choices[answer_index]

        except IndexError:
            print("IndexError: list index out of range")
            print("Row with IndexError:", row)

        prompt = f"Respond to the following question with single letter answer.\n\nQuestion: {question}\nHow do you respond?\n"
        for i, choice in enumerate(choices):
            prompt += f"{chr(65 + i)}. {choice}\n"

        test_cases.append({
            "key": str(uuid.uuid4()),
            "prompt": prompt,
            "categories": ["question-answering"],
            "constraints": [f"REGEXP^{chr(65 + answer_index)}.*"],
            "expected_output": str(chr(65 + answer_index))
        })

    tests.append({
            "key": test_key,
            "documents": ['T-TUT-PROTO-2019-PDF-E.pdf'],
            "test_cases": test_cases
        })   

    return {"tests": tests}

csv_file = '/Users/admin/Documents/h2o-evals/Telcom_T-TUT-PROTO-2019-PDF-E/multi_choice_telcom.csv'
# json_file = 'multi_choice_financial_statement_output.json'
json_data = csv_to_json(csv_file)

with open(f"{csv_file.split('/')[-1].split('.')[0]}_output.json", 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
