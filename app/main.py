import logging
import os
# from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Header, Request
from .config import SECRET_KEY
from .models import WebsiteDetails
from .scraper import extract_details_with_langchain

# FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("SECRET_KEY:", os.getenv("SECRET_KEY"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# POST endpoint to accept the website URL
@app.post("/scrape", response_model=WebsiteDetails)
async def scrape_website(request: Request, Authorization: str = Header(...)):
    try:
        # Authorization check
        if Authorization != f"Bearer {SECRET_KEY}":
            logger.warning("Unauthorized access attempt")
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Extract data from the request
        data = await request.json()
        url = data.get("url")

        # Validate URL
        if not url:
            logger.error("No URL provided")
            raise HTTPException(status_code=400, detail="URL is required")

        # Extract details using AI
        logger.info(f"Scraping website: {url}")
        details = extract_details_with_langchain(url)

        # Return the extracted details
        return details

    except HTTPException as http_exc:
        # Log HTTP-specific exceptions (e.g., 400, 401, etc.)
        logger.error(f"HTTP error occurred: {http_exc.detail}")
        raise http_exc
    
    except Exception as e:
        # Log general exceptions
        logger.error(f"Error occurred during processing: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")