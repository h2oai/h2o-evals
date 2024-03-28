# Banking_Policy_Document

## Overview
Welcome to the Banking_Policy_Document, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Banking industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Banking sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Policy_Document.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Policy_Document/used_documents/Policy_Document.pdf)

## Dataset Details
- **Industry:** Banking
- **Sub Industry:** Policy Document
- **Number of Question-Answer Pairs:** 125
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Banking sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Banking industry. It comprises a rich set of 125 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Multi choice questions from the dataset:

**Question:** What are the general guidelines for handling and retaining records in a bank?

**Answer:** ['All books and registers must be entered serially in the register of current-cum-old records.', 'An employee handling a particular book/register/file will be responsible for its custody during the day time.', 'Record warehouses/rooms may be opened at metropolitan centers where there is a cluster of branches.', 'All documents and papers connected with account opening forms must be kept in the strong room overnight.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Policy_Document/screenshots/multi_choice.png)

#### Sample Token presence from the dataset:

**Question:** What is the purpose of maintaining records in a bank?

**Answer:** The purpose of maintaining records in a bank is to have a reference for various purposes like verification by internal auditors, inspectors, officials, and external statutory bodies like RBI, SEBI, etc. Records are also required for verifying old transactions, processes, or events, and in case of any complaint or information sought by any citizen of India under RTI Act.

**Token Presence:** ['maintaining', 'records', 'bank', 'verification', 'internal', 'auditors', 'inspectors', 'officials', 'external', 'statutory', 'bodies', 'RTI', 'Act']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Policy_Document/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** What is the minimum retention period for the following documents:

1. Files of rejected loan proposals?
2. Application forms for closed loans?
3. Bill realization letters received from collecting Bankers/Branches?
4. Acknowledgements?
5. V.P. Receipts files?
6. NOSTRO A/c. /Position Register?
7. Confirmations for Telegrams?
8. Purchase/Sale Note?
9. Reconciliation sheets?
10. GR/SBF/EP/PP/SOFTEX Form Register/System generated Hard Copy?


**Answer:** The purpose of the Mid-year review is to assess the progress of the branch's operations and identify areas that require improvement.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Policy_Document/screenshots/question_type.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

