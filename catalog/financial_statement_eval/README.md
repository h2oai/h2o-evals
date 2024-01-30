# Financial Statement Dataset

## Overview
Welcome to the Financial Statement Dataset, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the banking industry, focusing on Conditional Questions, Multi choice Questions and Token Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Finance sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [2023Q1_alphabet_earnings_release.pdf](https://github.com/h2oai/h2o-evals/blob/4b3a9eba91da49a8c8cafdde9b9272bdea5e6998/catalog/financial_statement_eval/used_documents/doc1.pdf)
2. [TSLA_Q1_2023_update.pdf](https://github.com/h2oai/h2o-evals/blob/4b3a9eba91da49a8c8cafdde9b9272bdea5e6998/catalog/financial_statement_eval/used_documents/TSLA-Q1-2023-Update.pdf)
<!-- 2. [Document Name 2]
3. [Document Name 3] -->

## Dataset Details
- **Industry:** Finance
- **Sub Industry:** Company financial statement
- **Number of Question-Answer Pairs:** 1200
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions, Multi choice questions and Token Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the finance sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the finance industry. It comprises a rich set of 1200 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of conditional questions, Multi choice questions and Token Presence.

## Dataset Configuration 

## Eval Studio Outputs

## Sample Question 
#### Here is a sample conditional question from the dataset:

**Question:** Factors affecting Tesla's factory ramp-up?

**Answer:** Some of the factors that could affect Tesla's ability to ramp its factories in accordance with its plans include the ability to procure supply of battery cells, including through its own manufacturing, and risks relating to international expansion.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/2e12107f1b90038a4e5db956c774ee41966ecab9/catalog/financial_statement_eval/screenshots/2.png)


#### Here is a sample Multi choice questions from the dataset:

**Question:** What was the revenue of Alphabet Inc. in the first quarter of 2023?

**Answer:** ['$68,011', '$69,787', '$74,548', '$61,961']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/2e12107f1b90038a4e5db956c774ee41966ecab9/catalog/financial_statement_eval/screenshots/1.png)

#### Here is a sample Token presence from the dataset:

**Question:** What was the total revenue for Tesla in Q1 2023?

**Answer:** The total revenue for Tesla in Q1 2023 was $23.3 billion, representing a 24% increase year over year.

**Token Presence:**  ['$23.3 billion', '24%']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/2e12107f1b90038a4e5db956c774ee41966ecab9/catalog/financial_statement_eval/screenshots/3.png)


## Usage
This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use
1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information
For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.