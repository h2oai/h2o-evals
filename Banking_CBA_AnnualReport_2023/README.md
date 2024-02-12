# Banking_CBA_AnnualReport_2023

## Overview
Welcome to the Banking_CBA_AnnualReport_2023, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Banking industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Banking sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [CBA_AnnualReport_2023.pdf](https://github.com/h2oai/h2o-evals/blob/main/Banking_CBA_AnnualReport_2023/used_documents/CBA_AnnualReport_2023.pdf)

## Dataset Details
- **Industry:** Banking
- **Sub Industry:** Annual Report
- **Number of Question-Answer Pairs:** 120
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Banking sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Banking industry. It comprises a rich set of 120 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What is the name of the bank that released the 2023 Annual Report?

**Answer:** The name of the bank that released the 2023 Annual Report is Commonwealth Bank of Australia.

**Token Presence:** ['Commonwealth Bank of Australia']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/Banking_CBA_AnnualReport_2023/screenshots/tokens_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the name of the bank that released the 2023 Annual Report?

**Answer:** ['Commonwealth Bank of Australia', 'BlueScope Steel Ltd', 'TXU Energy', 'Coles Group Limited']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/Banking_CBA_AnnualReport_2023/screenshots/multi_choice.png)

#### Sample Conditional questions from the dataset:

**Question:** Who are the individuals who, at the request of the Bank or a related body corporate, act as director, secretary or senior manager of a body corporate which is not a related body corporate of the Bank?

**Answer:** Persons who, at the request of the Bank or a related body corporate, act as director, secretary or senior manager of a body corporate which is not a related body corporate of the Bank are indemnified by the Bank under the deed poll.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/Banking_CBA_AnnualReport_2023/screenshots/question_type.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

