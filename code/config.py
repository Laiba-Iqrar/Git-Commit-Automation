from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")

# Repository paths
REPO_PATHS = [
    "D:/Airline Booking and Management System/Airline-Booking-and-Management-System/Code",
    "D:/TWQUran"
]