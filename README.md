# Setup
I went to this directory and executed the following commands:

``
PS C:\Users\juant\Documents\coding\llm\django_llm>
``

``
python -m venv .env 
.env/Scripts/activate
pip install transformers torch fastapi uvicorn django djangorestframework
``

Then:

``
django-admin startproject myproject .
python manage.py startapp myapp
``

============ OTHER INSTRUCTIONS OMITTED ============

go to http://127.0.0.1:8000/myapp/api/qa/
and add:
{
  "context": "Hugging Face is creating amazing tools for the AI community.",
  "question": "What does Hugging Face do?"
}

