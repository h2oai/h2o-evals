# Financial Statement Dataset

## Overview
Welcome to the Financial Statement Dataset, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Banking industry, focusing on Conditional Questions.

## Documents Used
The dataset is derived from a selection of key documents within the Banking sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [TSLA-Q1-2023-Update.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/financial_statement_eval/used_documents/TSLA-Q1-2023-Update.pdf)
2. [doc1.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/financial_statement_eval/used_documents/doc1.pdf)

## Dataset Details
- **Industry:** Banking
- **Sub Industry:** Company financial statement
- **Number of Question-Answer Pairs:** 1200
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Banking sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Banking industry. It comprises a rich set of 1200 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What was the total revenue for Tesla in Q1 2023?

**Answer:** The total revenue for Tesla in Q1 2023 was $23.3 billion, representing a 24% increase year over year.

**Token Presence:** ['$23.3 billion', '24%']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/financial_statement_eval/screenshots/token_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** What was the revenue of Alphabet Inc. in the first quarter of 2023?

**Answer:** ['$68,011', '$69,787', '$74,548', '$61,961']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/financial_statement_eval/screenshots/multi_choice.png)

#### Sample Conditional questions from the dataset:

**Question:** How much did the change in accounting estimate for the useful lives of servers and network equipment reduce depreciation expense and increase net income in the three months ended March 31, 2023?

**Answer:** The change in accounting estimate reduced depreciation expense by $988 million and increased net income by $770 million, or $0.06 per basic and $0.06 per diluted share.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/financial_statement_eval/screenshots/question_type.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

