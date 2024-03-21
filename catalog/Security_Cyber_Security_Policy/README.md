# Security_Cyber_Security_Policy

## Overview
Welcome to the Security_Cyber_Security_Policy, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Security industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Security sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Cyber_Security_Policy.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Security_Cyber_Security_Policy/used_documents/Cyber_Security_Policy.pdf)

## Dataset Details
- **Industry:** Security
- **Sub Industry:** Cyber Security
- **Number of Question-Answer Pairs:** 125
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Security sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Security industry. It comprises a rich set of 125 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Information Security Policy?

**Answer:** The purpose of the Information Security Policy is to express <Organization>’s commitment to managing information security risks effectively and efficiently, coordinated globally and in compliance with applicable regulations wherever it conducts business.

**Token Presence:** ['commitment', 'managing', 'information', 'security', 'risks', 'effectively', 'efficiently', 'globally', 'compliance', 'regulations', '<Organization>']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Security_Cyber_Security_Policy/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** Is it acceptable to provide information about <Organization> or its employees, clients, customers, patients, or associates to any outside party without authorization?

**Answer:** No, the policy prohibits providing information about <Organization> or its employees, clients, customers, patients, or associates to any outside party without explicit authorization.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Security_Cyber_Security_Policy/screenshots/question_type.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the role of an Information Owner?

**Answer:** ['To implement, operate, and maintain security measures defined by Information Owners.', 'To designate the relevant sensitivity classification and appropriate level of criticality for information.', 'To safeguard information, including implementing access control systems and making backups.', 'To create, distribute, access, or manage information by means of <Organization>’s information technology systems.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Security_Cyber_Security_Policy/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

