# Legal_UPC_Agreement

## Overview
Welcome to the Legal_UPC_Agreement, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Legal industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Legal sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [UPC_Agreement.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Legal_UPC_Agreement/used_documents/UPC_Agreement.pdf)

## Dataset Details
- **Industry:** Legal
- **Sub Industry:** UPC Agreement
- **Number of Question-Answer Pairs:** 141
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Legal sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Legal industry. It comprises a rich set of 141 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Conditional questions from the dataset:

**Question:** In what circumstances can a defendant obtain translations of relevant documents in the language of the Member State of residence, principal place of business or, in the absence of residence or principal place of business, place of business?

**Answer:** A defendant can obtain translations of relevant documents in the language of the Member State of residence, principal place of business or, in the absence of residence or principal place of business, place of business, if jurisdiction is entrusted to the central division in accordance with Article 33(1) third or fourth subparagraph, the language of proceedings at the central division is a language which is not an official language of the Member State where the defendant has its residence, principal place of business or, in the absence of residence or principal place of business, place of business, and the defendant does not have proper knowledge of the language of the proceedings. (Article 51(3)(a-c))

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Legal_UPC_Agreement/screenshots/question_type.png)

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Agreement on a Unified Patent Court?

**Answer:** The purpose of the Agreement on a Unified Patent Court is to improve the enforcement of patents and the defense against unfounded claims and patents which should be revoked, and to enhance legal certainty by setting up a Unified Patent Court for litigation relating to the infringement and validity of patents.

**Token Presence:** ['improve', 'enforce', 'defense', 'unfounded', 'patents', 'legal', 'certainty', 'setting', 'litigation', 'infringement', 'validity']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Legal_UPC_Agreement/screenshots/tokens_present.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the significance of the European Patent Convention (EPC) in relation to the Unified Patent Court?

**Answer:** ['The EPC established the Unified Patent Court and its procedures.', 'The EPC provides for a single procedure for granting European patents by the European Patent Office, which can then be litigated at the Unified Patent Court.', 'The EPC gives the Unified Patent Court exclusive competence in respect of European patents with unitary effect and European patents granted under the provisions of the EPC.', 'The EPC is not relevant to the Unified Patent Court, as it only applies to national patent laws.']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Legal_UPC_Agreement/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

