**Project: End-to-End Text to SQL LLM App with Google Gemini Pro**
This project demonstrates the development of an interactive application that converts natural language text into SQL queries using Google Gemini Pro, and allows querying a SQLite database for results. The app is built using Streamlit for the user interface and utilizes Google Gemini Pro API to process and generate SQL queries from English language questions.

**Overview**
The app allows users to type questions in plain English, such as "What is the highest mark in the class?" or "List all students in Data Science class," and converts them into SQL queries using Google’s generative AI. The generated SQL queries are then executed against a SQLite database to retrieve relevant data.

**Technologies Used**
*Google Gemini Pro* for generating SQL queries from natural language.
*Streamlit* for building the web-based user interface.
*SQLite* for the database that stores student data.
*Python-dotenv* for managing environment variables securely.

**Project Structure**
sql.py: Contains code to set up the SQLite database, create tables, and insert records.
app.py: The main application file that uses Streamlit to interact with users, generate SQL queries with Google Gemini Pro, and query the SQLite database.

1.) **sql.py** – SQLite Database Setup and Record Insertion. This file contains the setup for the database and the insertion of sample data. 
[]{![image](https://github.com/user-attachments/assets/6c434f4e-02fe-4f3c-a750-f6be43fd2ace)}

2.) **app.py** – Streamlit App for User Interaction and Querying This file sets up the Streamlit app and integrates Google Gemini Pro to handle user input and generate SQL queries. 
[]{![image](https://github.com/user-attachments/assets/330b5e68-06db-435b-bf6f-41c0c0299a64)}

3.) **.env** – Storing API Keys Securely In the .env file, store your Google API key: 
[]{![image](https://github.com/user-attachments/assets/6fb2adc7-f16b-4a09-85ab-27dce00c6b13)}

**How to Run the Project**

Install Dependencies To set up the project, you’ll need to install the required Python libraries:
**code: pip install -r requirements.txt**

Create and Load the SQLite Database Run sql.py to create the database and insert sample data: 
**code : python sql.py**

Run the Streamlit App Launch the app by running the following command:
**code: streamlit run app.py**

Access the App Visit the URL provided by Streamlit to interact with the app in your browser.



