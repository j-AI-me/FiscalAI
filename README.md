# FiscalAI

This repository contains a minimal skeleton for FiscalAI, an application that helps businesses optimize their taxation strategy.

## Backend
The backend is implemented with **FastAPI**. To run it locally:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

This will start a development server on `http://localhost:8000` with a `/api/form` endpoint to receive form submissions.

## Frontend
A placeholder React application can be found in the `frontend` directory (to be expanded).
