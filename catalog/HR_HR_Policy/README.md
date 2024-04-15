# HR_HR_Policy

## Overview
Welcome to the HR_HR_Policy, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the HR industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the HR sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [HR_Policy.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/HR_HR_Policy/used_documents/HR_Policy.pdf)

## Dataset Details
- **Industry:** HR
- **Sub Industry:** HR Policy
- **Number of Question-Answer Pairs:** 122
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the HR sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the HR industry. It comprises a rich set of 122 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Multi choice questions from the dataset:

**Question:** Can the probationary period be extended for staff?

**Answer:** ['Yes, upon recommendation by the Reporting Officer and Head of Department/Executive Secretary of Industrial Union.', 'No, the probationary period cannot be extended, and staff must be confirmed or terminated at the end of the probationary period.', 'Yes, but only for staff who are on Grade N1 to N3.', 'Yes, but only for staff who are on probation for more than six months.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/HR_HR_Policy/screenshots/multi_choice.png)

#### Sample Token presence from the dataset:

**Question:** What is the probation period for staff appointed at Grade N1 to N3?

**Answer:** The probation period for staff appointed at Grade N1 to N3 is 3 months.

**Token Presence:** ['3 months']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/HR_HR_Policy/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** Can staff members claim transport reimbursement for traveling to places that are inaccessible by bus or MRT from their homes and vice versa for official purposes?

**Answer:** Yes, staff members can claim transport reimbursement for such travel, and they will be reimbursed the taxi fare after deducting the usual daily transport expenses incurred between home and office.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/HR_HR_Policy/screenshots/question_type.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

