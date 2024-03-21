# Government_US_Veterans_Affairs

## Overview
Welcome to the Government_US_Veterans_Affairs, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Government industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Government sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [US_Veterans_Affairs.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_US_Veterans_Affairs/used_documents/US_Veterans_Affairs.pdf)

## Dataset Details
- **Industry:** Government
- **Sub Industry:** Veterans Affairs
- **Number of Question-Answer Pairs:** 121
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Government sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Government industry. It comprises a rich set of 121 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Multi choice questions from the dataset:

**Question:** What is the purpose of the Section 508 Compliance Statement?

**Answer:** ['To provide access to healthcare for veterans with disabilities.', "To ensure that VA's electronic and information technologies are accessible to individuals with disabilities.", "To modernize VA's systems and processes for claims and appeals.", 'To invest in groundbreaking research that contributes to the quality of life for Veterans.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_US_Veterans_Affairs/screenshots/multi_choice.png)

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Section 508 Compliance Statement?

**Answer:** The purpose of the Section 508 Compliance Statement is to ensure that the electronic and information technologies used by the U.S. Department of Veterans Affairs are accessible to individuals with disabilities in accordance with Section 508 of the Rehabilitation Act.

**Token Presence:** ['Section 508', 'Compliance', 'Statement', 'accessible', 'individuals', 'disabilities', 'Rehabilitation', 'Act']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_US_Veterans_Affairs/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** What is the third strategic objective under the goal of Veterans Choose VA for Easy Access, Greater Choices, and Clear Information to Make Informed Decisions?

**Answer:** The third strategic objective under this goal is to ensure that veterans have easy access to VA services, regardless of their location or circumstances.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_US_Veterans_Affairs/screenshots/question_type.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

