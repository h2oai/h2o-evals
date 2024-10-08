import os
import pandas as pd

def generate_conditional_question(folder_name, row):
    question = f"#### Sample Conditional questions from the dataset:\n\n"
    question += f"**Question:** {row['question']}\n\n"
    question += f"**Answer:** {row['answer']}\n\n"
    question += f"![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/{folder_name}/screenshots/question_type.png)\n\n"
    return question

def generate_multi_choice_question(folder_name, row):
    question = f"#### Sample Multi choice questions from the dataset:\n\n"
    question += f"**Question:** {row['question']}\n\n"
    question += f"**Answer:** {row['choices']}\n\n"
    question += f"![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/{folder_name}/screenshots/multi_choice.png)\n\n"
    return question

def generate_token_presence_question(folder_name, row):
    question = f"#### Sample Token presence from the dataset:\n\n"
    question += f"**Question:** {row['question']}\n\n"
    question += f"**Answer:** {row['answer']}\n\n"
    question += f"**Token Presence:** {row['tokens_present']}\n\n"
    question += f"![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/{folder_name}/screenshots/tokens_present.png)\n\n"
    return question

def generate_dataset_info(row):
    dataset_info = (
        f"# {row['Dataset']}\n\n"
        f"## Overview\n"
        f"Welcome to the {row['Dataset']}, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the {row['Industry']} industry, focusing on {row['Evaluation_technique']}.\n\n"
        f"## Documents Used\n"
        f"The dataset is derived from a selection of key documents within the {row['Industry']} sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:\n"
    )

    used_documents_folder = os.path.join(row['Dataset_link'].split('/')[-1], 'used_documents')
    # used_documents_folder = os.path.join('https://github.com/h2oai/h2o-evals/tree/64ee8b5162e03fa569fda7a49261cc28aa1fe939/catalog', used_documents_folder)
    documents = os.listdir(f"./catalog/{used_documents_folder}")
    for index, document in enumerate(documents, start=1):
        document_path = os.path.join(used_documents_folder, document)
        dataset_info += f"{index}. [{document}](https://github.com/h2oai/h2o-evals/blob/main/catalog/{document_path})\n"

    dataset_info += (
        "\n## Dataset Details\n"
        f"- **Industry:** {row['Industry']}\n"
        f"- **Sub Industry:** {row['Sub_Industry']}\n"
        f"- **Number of Question-Answer Pairs:** {row['No_of_entries']}\n"
        f"- **Prompt Type:** {row['Prompt_type']}\n"
        f"- **Evaluation Techniques:** {row['Evaluation_technique']}\n\n"
        "## Industries and Evaluation Types\n"
        f"The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the {row['Industry']} sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.\n\n"
        "## Dataset Content\n"
        f"The dataset is carefully curated from a diverse set of documents within the {row['Industry']} industry. It comprises a rich set of {row['No_of_entries']} question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of {row['Evaluation_technique']}.\n\n"
    )

    return dataset_info

def process_folders(root_folder_path, csv_file_path):
    df = pd.read_csv(csv_file_path.split('/')[-1], encoding='unicode_escape')
    
    for i, row in df.iterrows():
        folder_name = 'catalog/'+row['Dataset_link']
        print(folder_name)
        folder_path = os.path.join(root_folder_path, folder_name.split('/')[-1])
        if True:
            questions = []
            
            for file_name in os.listdir(folder_name+'/CSV_files'):
                if file_name.endswith('.csv'):
                    csv_file_path = os.path.join(folder_name+'/CSV_files', file_name)
                    df_csv = pd.read_csv(csv_file_path)
                    if 'question_type' in file_name.lower() :
                        questions.append(generate_conditional_question(folder_name, df_csv.iloc[0]))
                    elif 'multi_choice' in file_name.lower() :
                        questions.append(generate_multi_choice_question(folder_name, df_csv.iloc[0]))
                    elif 'token_presence' in file_name.lower():
                        questions.append(generate_token_presence_question(folder_name, df_csv.iloc[0]))
            if questions:
                with open(os.path.join(folder_name, 'README.md'), 'w') as f:
                    f.write(generate_dataset_info(row))
                    f.write("## Dataset Configuration\n\n")
                    f.write("## Eval Studio Outputs\n\n")
                    f.write("# Sample Questions\n\n")
                    
                    for question in questions:
                        f.write(question)

                    f.write("## Usage\n\n")
                    f.write("This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.\n\n")
                    f.write("## How to Use\n\n")
                    f.write("1. **Download:** Acquire the dataset.\n")
                    f.write("2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.\n")
                    f.write("3. **Explore:** Familiarize yourself with the dataset's structure and content.\n")
                    f.write("4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.\n\n")
                    f.write("## Additional Information\n\n")
                    f.write("For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.\n\n")

def update_master_readme():
	df = pd.read_csv("data.csv", encoding= 'unicode_escape')

	html = """
| # | Dataset Name      | Industry | Sub Industry | No of Entries | Prompt Type |
|---| -------------- | --------- | -------------- | ----- | ----- |\n"""

	for i, r in df.iterrows():
		r = dict(r) 
		url = "https://github.com/h2oai/h2o-evals/tree/main/catalog/"
		html += f"| {int(r['ID'])}. | [{r['Dataset']}]({url + r['Dataset_link'].strip()})| `{r['Industry']}` | {r['Sub_Industry']} | {r['No_of_entries']} | {r['Prompt_type']} |"
		html += "\n"
	return html

def update_webpage_html():
	visited = []
	url = "https://github.com/h2oai/h2o-evals/blob/main/catalog/"
	html = ""
	df = pd.read_csv("data.csv", encoding= 'utf-8').fillna("NA")
	for i, r in df.iterrows():
		r = dict(r)

		## Uncomment to create new options in dropdown in HTML
		if r['Industry'].replace(" ", "") not in visited:
			visited.append(r['Industry'].replace(" ", ""))
			print (f"""<option value="{r['Industry'].replace(" ", "")}">{r['Industry']}</option>""")
		
		html += f"""<div class="card mb-4 all {r['Dataset'].replace(" ", "")} {r['Industry']} {r['Sub_Industry']}">
	<font color='#ffc107'><i class="fa-solid fa-2x fa-fire"></i></font>
	<h3 class="card-title">{r['Evaluation_technique']}</h3>
	<p>{r['Prompt_type']}</p>
	<p><span class="badge1">{r['Dataset']}</span> <span class="badge1">{r['Industry']}</span> <span class="badge1">{r['Sub_Industry']}</span> </p>
	<p class="card-icon"><a target='_blank' href="{url + r['Dataset_link'].strip()}"><i class="fa-solid fa-arrow-right"></i></a></p>
</div>"""
	return html

root_folder_path = 'https://github.com/h2oai/h2o-evals/blob/main/catalog/'
csv_file_path = 'https://github.com/h2oai/h2o-evals/blob/main/data.csv'

if __name__ == '__main__':
    # process_folders(root_folder_path, csv_file_path)
    print(update_master_readme())