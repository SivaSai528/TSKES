# Text_Summarization_and_Knowledge_Extraction_System

**Intelligent Text Summarization and Knowledge Extraction System**

**ABSTRACT**

Our project focuses on providing users with a convenient and efficient method
of understanding text without the need for extensive reading. We accomplish
this through text summarization, which can be categorized into two types:
abstraction and extraction. Abstraction summarization involves condensing the
main ideas and concepts of a text into a concise and coherent summary, while
extraction summarization focuses on extracting important sentences or phrases
directly from the original text. we go beyond summarization by generating
questions &answers and multiple-choice questions (MCQs) based on the
summarized text. This further aids users in comprehension and retention by
encouraging active engagement with the material. By combining these
techniques, our project aims to enhance the accessibility and comprehension of
various types of text, making it easier for users to grasp key information quickly
and effectively

**Problem Statement**

The problem at hand is to develop a user-friendly and efficient system that assists users in effectively summarizing long texts and generating relevant multiple-choice questions (MCQs) and questions and answers (Q&A). Reading lengthy documents can be timeconsuming and challenging, often leading to information overload. 

Users need a solution that can quickly extract the key points from a text and provide concise summaries, as well as generate relevant MCQs and Questions and answers to aid in comprehension and learning:

• Lengthy Texts: Reading long texts can be challenging and time-consuming, leading to information overload and decreased comprehension.
• Summarization: Users need a solution that can summarize texts, extracting the main ideas and essential details in a concise and coherent manner.
• Question and Answer Generation: Extracting relevant questions and answers from the text enables users to gain a deeper understanding of the material and clarify any uncertainties.
• MCQ Generation: Generating multiple-choice questions (MCQs) based on the text can
aid users in understanding and assessing their comprehension of the content.

**Proposed System**

• The system aims to help users understand text easily and save time.
• It utilizes two types of summarizations: abstraction and extraction.
• Abstraction summarization condenses the main ideas while preserving the overall meaning.
• Extraction summarization selects important sentences or phrases from the original text.
• The system generates questions and multiple-choice questions (MCQs) based on the
summaries.
• The questions serve to test users' comprehension and reinforce understanding.
• Overall, the system combines summarization and question generation to enhance text comprehension and learning


**How to Setup and Run your Project**

Open Visual Studio Code app and Select the Project Folder
Select New terminal and Select cmd
Run the following Commands to Install all necessities for the project
1. Create a Python Environment
Python -m venv _name_
2. Activate the Environment
_name_\Scripts\activate
3. Install Flask
pip install flask
4. Install Torch
pip install torch
5. Install Spacy
pip install -U spacy
6. Install Transformers
pip install transformers
7. Install Gensim
pip install genism
8. Install bert-extractive-summarizer
pip install bert-extractive-summarizer
9. Install SentencePiece
pip install sentencepiece
10. Install PKE
pip install git+https://github.com/boudinfl/pke.git
make sure you install git in your pc
11. Install EN datasets from spacy
python -m spacy download en
12. Install NLTK
pip install -U nltk
13. Install PYWSD
pip install -U pywsd
14. Download stopwords and popular from NLTK
python
>>>import nltk
>>>nltk.download(‘stopwords’)
>>>nltk.download(‘popular’)
15. Install Flashtext
pip install flashtext
 After installing all the Required modules and libraries
Run Esummary.py and Asummary.py to create pickle files for summarized models
• python Esummary.py
• python Asummary.py
After all the files have been Created
Run the flask file
• python app.py
copy paste the host address in any browser to run the project

