# Text2SQL Project Using Streamlit, Google Gemini, and SQLite

## Project Overview

![Project Pipeline](https://via.placeholder.com/800x400.png?text=Project+Pipeline)

This project demonstrates an interactive web application for converting natural language queries into SQL commands using Google Gemini's generative AI capabilities. The application also executes the generated SQL commands on an SQLite database and displays the results. 

It is ideal for developers and data enthusiasts looking to integrate AI for SQL generation and streamline data retrieval workflows.

---

## Project Steps

### 1. Set Up the Environment
   - **Tools Used**: Streamlit, Python, SQLite, Google Gemini API
   - **Goal**: Build a web-based interface to accept natural language queries, convert them into SQL commands, and fetch results from a pre-defined database.

### 2. Install Required Libraries
   - Install the necessary Python libraries:
     ```bash
     pip install streamlit google-generativeai python-dotenv
     ```

### 3. Configure Google Gemini API
   - **API Setup**:
     - Obtain an API key from Google Cloud's Generative AI platform.
     - Create a `.env` file in your project directory and add your API key:
       ```env
       GOOGLE_API_KEY=your_api_key_here
       ```
   - **Integration**:
     - Use the `dotenv` library to load the API key into the application.

### 4. Set Up SQLite Database
   - **Database Creation**:
     - The database `student.db` is initialized with a `STUDENT` table containing columns `NAME`, `CLASS`, `SECTION`, and `MARKS`.
   - **Data Insertion**:
     - Populate the table with sample student records using the script provided in `sql.py`.

### 5. Define Prompt for Google Gemini
   - Use a structured prompt to guide the AI model in converting natural language queries into SQL commands. For example:
     - **Input**: "How many students are in Data Science class?"
     - **Output**: `SELECT COUNT(*) FROM STUDENT WHERE CLASS='Data Science';`

### 6. Build the Streamlit Application
   - **Interface**:
     - A simple form where users can input natural language queries.
   - **Functionality**:
     - Convert the input query to SQL using the Gemini API.
     - Execute the generated SQL command on the SQLite database.
     - Display results dynamically in the app.

### 7. Test the Application
   - Validate the SQL queries and results for different natural language inputs, ensuring accurate AI translations and correct database responses.

### 8. Publish and Share
   - Deploy the project using platforms like [Streamlit Cloud](https://streamlit.io/cloud) or containerize it using Docker for broader access.

---

## Project Requirements

- **Python 3.8+**
- **Python Libraries**:
  - `streamlit`, `google-generativeai`, `dotenv`, `sqlite3`
- **Google Gemini API Key**
- **Database**:
  - SQLite (`student.db` with `STUDENT` table)

---

## Project Structure

```plaintext
|-- .env                     # Environment file for storing API key
|-- app.py                   # Main Streamlit application script
|-- sql.py                   # Script to create SQLite database and populate it with records
|-- student.db               # SQLite database
|-- README.md                # Project documentation
|-- requirements.txt         # List of required Python libraries
```

---

## Application Workflow

1. **User Input**: Users enter a natural language query into the Streamlit app.
2. **AI Conversion**: The app sends the query to Google Gemini for conversion into SQL.
3. **Database Execution**: The generated SQL query is executed on the SQLite database.
4. **Result Display**: Results are fetched and displayed within the app.

---

## Future Enhancements

- **Database Expansion**: Add support for multiple tables and complex schemas.
- **Dashboard Integration**: Visualize query results using Streamlit charts or dashboards.
- **Enhanced AI Prompt**: Improve the prompt to handle ambiguous or multi-layered queries.
- **API Deployment**: Expose the functionality as an API for integration with other applications.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- **Google Generative AI**: For powering natural language to SQL conversion.
- **Streamlit**: For building a user-friendly application interface.
