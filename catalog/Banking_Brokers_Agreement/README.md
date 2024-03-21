# Banking_Brokers_Agreement

## Overview
Welcome to the Banking_Brokers_Agreement, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Banking industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Banking sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Broker_Agreement.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Brokers_Agreement/used_documents/Broker_Agreement.pdf)

## Dataset Details
- **Industry:** Banking
- **Sub Industry:** Brokers Agreement
- **Number of Question-Answer Pairs:** 58
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Banking sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Banking industry. It comprises a rich set of 58 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Conditional questions from the dataset:

**Question:** What is the process for LSB to release the related Loan file and execute instruments of transfer or assignment upon receipt of the Repurchase Price?

**Answer:** LSB shall release the related Loan file and execute such instruments of transfer or assignment, in each case without recourse or warranty, as shall be necessary to vest in Seller or its designee title to the repurchased Loan.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Brokers_Agreement/screenshots/question_type.png)

#### Sample Token presence from the dataset:

**Question:** What is the date of the agreement?

**Answer:** The agreement is dated as of the [insert date] day of [insert month], 20[insert year].

**Token Presence:** ['[insert date]', '[insert month]', '20[insert year]']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Brokers_Agreement/screenshots/tokens_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** What laws and regulations must the seller comply with?

**Answer:** ["Federal, State, and local laws and regulations that directly or indirectly relate to the seller's activities under the agreement.", "Laws and regulations that apply to the seller's business, including those related to lending, banking, and financial services.", "Laws and regulations that apply to the seller's formation, existence, and standing, such as corporate law and licensing requirements.", "Laws and regulations that apply to the seller's interactions with LSB, including contract law and privacy laws."]

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Banking_Brokers_Agreement/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

