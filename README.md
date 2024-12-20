
# Website Scraping Bot with AI-Powered Insights

This project is a **FastAPI application** that extracts structured business details (industry, company size, and location) from a given website URL. The extraction leverages **OpenAI's GPT models** with **LangChain** for consistent and validated responses.

---

## Features

- **AI-Powered Data Extraction**: Extracts business-related details like:
  - **Industry**
  - **Company Size**
  - **Company Location**
- **CORS Enabled**: Handles cross-origin requests for client integration.
- **Secure Authorization**: Protects API access with an authorization token.
- **LangChain Integration**: Ensures structured, deterministic AI outputs.

---

## Technologies Used

- **Python 3.9+**
- **FastAPI**: For building the RESTful API.
- **LangChain**: For structured AI prompt handling and output validation.
- **OpenAI GPT Models**: For extracting meaningful insights from website content.
- **BeautifulSoup**: For parsing website HTML.

---

## Installation

### Prerequisites

1. **Python 3.9+**
2. **OpenAI API Key**: [Generate an API Key](https://platform.openai.com/signup/).
3. **Virtual Environment** (optional but recommended).

---

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/website_scraping_bot.git
   cd website_scraping_bot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```bash
     touch .env
     ```
   - Add the following variables to the `.env` file:
     ```
     SECRET_KEY=your-secret-key
     OPENAI_API_KEY=your-openai-api-key
     ```

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**:
   - Open your browser and navigate to the interactive API documentation:
     ```
     http://127.0.0.1:8000/docs
     ```
   - You can test the `/scrape` endpoint directly from the documentation.

---

## Usage

### API Endpoint: **`POST /scrape`**

#### Request

**Headers**:
```json
{
  "Authorization": "Bearer your-secret-key",
  "Content-Type": "application/json"
}
```

**Body**:
```json
{
  "url": "https://example.com"
}
```

#### Response

**Success Response**:
```json
{
  "industry": "Technology",
  "company_size": "Medium",
  "company_location": "San Francisco, CA"
}
```

**Error Response**:
```json
{
  "detail": "Unauthorized"
}
```

---

## Testing the Application

1. **Using `curl`**:
   ```bash
   curl -X POST http://127.0.0.1:8000/scrape         -H "Authorization: Bearer your-secret-key"         -H "Content-Type: application/json"         -d '{"url": "https://example.com"}'
   ```

2. **Using Postman**:
   - Import the API endpoint into Postman.
   - Set the `Authorization` header to `Bearer your-secret-key`.
   - Add the JSON body with the `url` field.
   - Send the request and check the response.

---

## Troubleshooting

### Common Issues

1. **Environment Variables Not Loaded**:
   Ensure `.env` is in the project root and loaded properly.

2. **Invalid JSON Output**:
   Check if the website content is properly scraped and the AI response aligns with the prompt structure.

3. **OpenSSL Warnings**:
   Update OpenSSL on your machine:
   ```bash
   brew install openssl
   brew reinstall python
   ```

4. **LangChain Deprecations**:
   Ensure you're using the latest versions:
   ```bash
   pip install -U langchain langchain-community langchain-openai
   ```

---

## Deployment

### Using Render
1. **Deploy the Code**:
   Push the code to GitHub and connect it to Render.
2. **Set Environment Variables**:
   Configure `SECRET_KEY` and `OPENAI_API_KEY` in Render's environment settings.
3. **Access the Application**:
   The API will be available at `https://<your-app>.onrender.com`.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Added new feature"`.
4. Push the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
