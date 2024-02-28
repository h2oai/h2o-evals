# Government_Home_Affairs

## Overview
Welcome to the Government_Home_Affairs, part of the H2O.ai LLM Evaluation Datasets collection. This dataset is tailored for evaluating Large Language Models (LLM) and RAG systems within the Government industry, focusing on Conditional Questions Multi Choice and Tokens Presence.

## Documents Used
The dataset is derived from a selection of key documents within the Government sector, enhancing the real-world relevance of the evaluation. The following source documents were instrumental in generating this dataset:
1. [Home_Affairs.pdf](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_Home_Affairs/used_documents/Home_Affairs.pdf)

## Dataset Details
- **Industry:** Government
- **Sub Industry:** Home Affairs
- **Number of Question-Answer Pairs:** 116
- **Prompt Type:** RAG
- **Evaluation Techniques:** Conditional Questions Multi Choice and Tokens Presence

## Industries and Evaluation Types
The H2O LLM Evaluation Datasets encompass various industries and evaluation types. This dataset, specifically tailored for the Government sector, focuses on conditional questions, Multi choice questions and Token presence to ensure targeted evaluation.

## Dataset Content
The dataset is carefully curated from a diverse set of documents within the Government industry. It comprises a rich set of 116 question-answer pairs, emphasizing the assessment of language models' understanding and reasoning in the context of Conditional Questions Multi Choice and Tokens Presence.

## Dataset Configuration

## Eval Studio Outputs

# Sample Questions

#### Sample Token presence from the dataset:

**Question:** What is the purpose of the Procedural Instruction (PI) for arrivals without a visa?

**Answer:** The purpose of the PI is to provide guidance for Border Clearance Officers (BCOs) in the Aviation environment when dealing with non-citizen travellers who do not appear to hold a visa.

**Token Presence:** ['guidance', 'Border Clearance Officers', 'Aviation', 'non-citizen travellers', 'visa']

![token_presence_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_Home_Affairs/screenshots/tokens_present.png)

#### Sample Conditional questions from the dataset:

**Question:** What is the purpose of the Immigration Clearance of Australian Citizens – PI (BC-2536) and Immigration Clearance of Australian Citizens without an Australian Passport – PI (BC-2458)?

**Answer:** The purpose of the Immigration Clearance of Australian Citizens – PI (BC-2536) and Immigration Clearance of Australian Citizens without an Australian Passport – PI (BC-2458) is to provide guidance on the clearance of Australian citizens who do not hold an Australian passport.

![conditional_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_Home_Affairs/screenshots/question_type.png)

#### Sample Multi choice questions from the dataset:

**Question:** What is the scope of the PI?

**Answer:** ['This PI covers referrals of non-citizen travellers in immigration clearance who do not appear to hold a visa.', 'This PI covers immigration clearance of non-citizens who hold a visa, including imposters who appear to hold a visa or apply for a visa whilst in clearance.', 'This PI covers immigration clearance of non-citizens without a visa in the Maritime environment.', 'This PI covers clearance of travellers and/or goods under the Customs Act 1901 (Customs Act).']

![multi_choice_question_image](https://github.com/h2oai/h2o-evals/blob/main/catalog/Government_Home_Affairs/screenshots/multi_choice.png)

## Usage

This dataset is a valuable resource for evaluating the performance of Large Language Models and RAG systems. Integration with H2O Eval Studio enables seamless evaluation, empowering users to conduct thorough assessments on this domain-specific dataset.

## How to Use

1. **Download:** Acquire the dataset.
2. **Import:** Ingest the dataset into H2O Eval Studio or your preferred evaluation environment.
3. **Explore:** Familiarize yourself with the dataset's structure and content.
4. **Evaluate:** Utilize the dataset to evaluate the performance of your language models in handling banking-related conditional questions.

## Additional Information

For further details or inquiries, feel free to contact [H2O.ai](https://www.h2o.ai/) or refer to the comprehensive documentation provided by H2O.ai for their LLM Data Studio.

