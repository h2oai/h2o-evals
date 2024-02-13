# Legal_IRS_Document_2

## Overview
Welcome to the Legal_IRS_Document_2, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Legal industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Legal sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [IRS_Document_2.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Legal_IRS_Document_2/used_documents/IRS_Document_2.pdf)

## Dataset Details
- **Industry:** Legal
- **Sub Industry:** IRS Filing Policy
- **Number of Question-Answer Pairs:** 126
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Legal sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Legal industry. It comprises a rich set of 126 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Conditional questions from the dataset:

**Question:** Who can check the "Married filing jointly" box at the top of Form 1040 or 1040-SR?

**Answer:** You can check the "Married filing jointly" box at the top of Form 1040 or 1040-SR if you were married at the end of 2023, even if you didn't live with your spouse at the end of 2023, your spouse died in 2023 and you didn't remarry in 2023, or you were married at the end of 2023 and your spouse died in 2024 before filing a 2023 return.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/catalog/Legal_IRS_Document_2/screenshots/question_type.png)

#### Sample Token presence from the dataset:

**Question:** What is the deadline for filing Form 1040 or 1040-SR for the 2023 tax year?

**Answer:** The deadline for filing Form 1040 or 1040-SR for the 2023 tax year is April 15, 2024.

**Token Presence:** ['April 15, 2024']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/catalog/Legal_IRS_Document_2/screenshots/tokens_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** How can you learn about your taxpayer rights?

**Answer:** ['By contacting the Taxpayer Advocate Service (TAS) for assistance.', 'By visiting the TAS website (TaxpayerAdvocate.IRS.gov) to understand the Taxpayer Bill of Rights.', 'By calling the IRS toll-free at 800-TAX-FORM (800-829-3676) to request information.', 'By consulting a tax professional or attorney for advice.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/catalog/Legal_IRS_Document_2/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

