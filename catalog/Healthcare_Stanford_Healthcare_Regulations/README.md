# Healthcare_Stanford_Healthcare_Regulations

## Overview
Welcome to the Healthcare_Stanford_Healthcare_Regulations, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Health industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Health sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Stanford_Healthcare_Regulations.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Healthcare_Stanford_Healthcare_Regulations/used_documents/Stanford_Healthcare_Regulations.pdf)

## Dataset Details
- **Industry:** Health
- **Sub Industry:** Health Regulations
- **Number of Question-Answer Pairs:** 114
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Health sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Health industry. It comprises a rich set of 114 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Medical Staff Rules and Regulations at Stanford Health Care?

**Answer:** The purpose of the Medical Staff Rules and Regulations is to ensure the quality of medical care rendered at Stanford Health Care and to establish guidelines for professional medical care performed at the hospital.

**Token Presence:** ['quality', 'medical', 'care', 'guidelines', 'hospital']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Healthcare_Stanford_Healthcare_Regulations/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** What is the requirement for documenting a patient's history and physical examination (H&P) before surgery or a procedure requiring anesthesia services?

**Answer:** A H&P must be completed no more than 30 days before or 24 hours after inpatient or outpatient admission, and an updated examination (H&P Interval) must be completed and documented within 24 hours after admission.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Healthcare_Stanford_Healthcare_Regulations/screenshots/question_type.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the purpose of the Medical Staff Rules and Regulations at Stanford Health Care?

**Answer:** ['To establish the qualifications and responsibilities of the Medical Staff.', 'To define patient types and admission criteria.', 'To outline the services provided by the hospital.', "To describe the hospital's billing and reimbursement policies."]

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Healthcare_Stanford_Healthcare_Regulations/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

