import os
import requests
from dotenv import load_dotenv
from exceptions import DivarAPIException
from schemas import Message
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)

load_dotenv()

class DivarKenarChat:
    BASE_URL = "https://metal-clowns-create.loca.lt"

    def __init__(self):
        self.api_key = "eyJhbGciOiJSUzI1NiIsImtpZCI6InByaXZhdGVfa2V5XzIiLCJ0eXAiOiJKV1QifQ.eyJhcHBfc2x1ZyI6InNwcmluZy1yb2FuLW5pbmphIiwiYXVkIjoic2VydmljZXByb3ZpZGVycyIsImV4cCI6MTc1MzcwMjY3NiwianRpIjoiNWQzZDBmMjctM2M4MS0xMWYwLTk4NGQtZWExNDRhMjEzYmQyIiwiaWF0IjoxNzQ4NTE4Njc2LCJpc3MiOiJkaXZhciIsInN1YiI6ImFwaWtleSJ9.YfGTsENl7zrMgXA579NNUVG1-p7GkBPAWGj6S5_2ihHhHhqREsMvs0AhW3fzhsZElM8ChgYDq2dqtg1r8iEsU8AOdyu4SdJ4LcLd680tmdvsc4DPGy1OfKvD_cyL5CYQEJeKl-0TMgDXg2xHwqWFRSsAY22aW9Ys3-nEe3py1w98m2Wk6kPAT0KqbwJTCLTDHGVUduz9CcMKIfUinM1kugTAjle6tJyCMo-EJQhORdtNqCcdu5s79t2i_V30a-zGm6lLJd1U4p8QjzJLsFN2CPDEq9Jh-2ICLAWd2_oyB5QdM-IRyqUo5qpynDYZDkxfLo3tQKm9xKRiGxylsJ8MUg"
        if not self.api_key:
            raise ValueError("Missing DIVAR_API_KEY in environment variables")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        logger.info("DivarKenarChat initialized with API key: %s...%s", self.api_key[:3], self.api_key[-3:])

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            # Capture more detailed error information
            error_detail = {
                "status_code": response.status_code,
                "url": response.url,
                "response_text": response.text,
                "headers": dict(response.headers)
            }
            logger.error("API Error: %s", json.dumps(error_detail, indent=2))
            raise DivarAPIException(f"HTTP Error {response.status_code}: {response.text}") from err
        except requests.exceptions.JSONDecodeError:
            logger.error("Invalid JSON response: %s", response.text)
            raise DivarAPIException("Invalid JSON response")
        except Exception as e:
            logger.exception("Unexpected error")
            raise DivarAPIException(f"Unexpected error: {str(e)}")

    def start_conversation(self, post_token: str, message: Message) -> dict:
        url = f"{self.BASE_URL}/api/start-process"
        payload = {
            "post_token": post_token,
            "message": message.dict(exclude_none=True)  # Remove None values
        }
        logger.debug("Starting conversation with payload: %s", json.dumps(payload, indent=2))
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            return self._handle_response(response)
        except Exception as e:
            logger.exception("Failed to start conversation")
            raise DivarAPIException(f"Failed to start conversation: {str(e)}")
 