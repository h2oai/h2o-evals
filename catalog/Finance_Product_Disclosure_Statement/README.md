# Finance_Product_Disclosure_Statement

## Overview
Welcome to the Finance_Product_Disclosure_Statement, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Finance industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Finance sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Product_Disclosure_Statement.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Finance_Product_Disclosure_Statement/used_documents/Product_Disclosure_Statement.pdf)

## Dataset Details
- **Industry:** Finance
- **Sub Industry:** Product Disclosure Statement
- **Number of Question-Answer Pairs:** 123
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Finance sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Finance industry. It comprises a rich set of 123 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Product Disclosure Statement?

**Answer:** The purpose of the Product Disclosure Statement is to provide important information about the investment in Finance Direct Limited's first ranking secured Debenture Stock to help potential investors decide whether they want to invest.

**Token Presence:** ['The purpose of the Product Disclosure Statement is to', 'invest', "Finance Direct Limited's", 'first ranking secured Debenture Stock', 'potential investors', 'decide', 'whether', 'they', 'want', 'to invest']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Finance_Product_Disclosure_Statement/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** What are the claims on the assets of the Company that will or may rank ahead of an investor's claim if the Company is put into liquidation or wound up?

**Answer:** The claims on the assets of the Company that will or may rank ahead of an investor's claim if the Company is put into liquidation or wound up are described in Section 4 of the PDS (Key features of the Debenture Stock).

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Finance_Product_Disclosure_Statement/screenshots/question_type.png)

#### Sample Multi choice questions from the dataset:

**Question:** How are interest payments made on the Debenture Stock?

**Answer:** ['Interest payments are made annually.', 'Interest payments are made monthly.', 'Interest payments are made quarterly.', 'Interest payments are made semi-annually.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Finance_Product_Disclosure_Statement/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

