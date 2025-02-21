Environment Setup: Installed spacy, pandas, PyPDF2, and loaded en_core_web_sm.
Entity Selection: Chose 30 entities (15 from Customer Support & 15 from Customer Service).
Training Data: Created sample sentences covering all 30 entity types.
ER Model Setup: Initialized a blank spacy model, added NER pipeline, and assigned labels.
NEXT STEPS:
Train the NER model using TRAIN_DATA.
save and test the trained model.
Implement user input for real time entity recognition
organize and zip the files for submission

\*\*ShanieWIP:
Environment Setup: flask
What was done:
-Set up flask for web based UI
-Set up UI with text box, entity checkboxes, text process button, and container for processed text
\*Entities need to be updated to be unique based on instructions. There are some that are duplicate
**These are duplicats: Customer Names, Support Reps/Agents, Service Request Types, Complaint Types, Refund Request, Customer Feedback, Shipping Info, Time/Date
**These are what I found to replace (but there are not enough that are not duplicates? Not sure what to do about that): Issue/Problem Descriptions, Service Level Agreement Terms (SLA), Location/Region
