"""
Root handler for Vercel deployment
This file ensures that Vercel can properly route to our Django app
"""
from backend.whisperlink_backend.wsgi import application

# This is required for Vercel to understand the WSGI application
app = application
