# Telcom_Technical_Report

## Overview
Welcome to the Telcom_Technical_Report, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Telecom industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Telecom sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Technical_Report.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Telcom_Technical_Report/used_documents/Technical_Report.pdf)

## Dataset Details
- **Industry:** Telecom
- **Sub Industry:** Technical Report
- **Number of Question-Answer Pairs:** 130
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Telecom sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Telecom industry. It comprises a rich set of 130 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Conditional questions from the dataset:

**Question:** What is the main issue that inhibits the mitigation of vulnerabilities in the "DFS over telecom" ecosystem?

**Answer:** The main issue that inhibits the mitigation of vulnerabilities in the "DFS over telecom" ecosystem is a misalignment of interests and misplaced liability between the telecom and financial regulators.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Telcom_Technical_Report/screenshots/question_type.png)

#### Sample Token presence from the dataset:

**Question:** What is the main issue that inhibits the mitigation of vulnerabilities in the "DFS over telecom" ecosystem?

**Answer:** The main issue that inhibits the mitigation of vulnerabilities in the "DFS over telecom" ecosystem is a misalignment of interests and misplaced liability between the telecom and financial regulators.

**Token Presence:** ['misalignment', 'interests', 'misplaced', 'liability', 'telecom', 'financial', 'regulators']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Telcom_Technical_Report/screenshots/tokens_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the purpose of the Annex B in the report?

**Answer:** ['It provides a technical description of SS7 and Diameter protocols.', 'It describes the vulnerabilities of SS7 and their effect on digital financial services.', 'It provides mitigation measures for operators and DFS providers.', 'It provides a template for a model MOU between a telecommunication regulator and central bank related to DFS security.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Telcom_Technical_Report/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

