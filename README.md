# Setup
In the following directory: `` PS C:\Users\juant\Documents\coding\llm\django_llm> `` execute:

- ``python -m venv .env ``
- ``.env/Scripts/activate``
- ``pip install transformers torch fastapi uvicorn django djangorestframework``
- ``django-admin startproject myproject .``
- ``python manage.py startapp myapp``

# API
- ``python manage.py migrate``
- ``python manage.py runserver``
- Go to ``http://127.0.0.1:8000/myapp/api/qa/`` and add:

``
{
  "context": "Hugging Face is creating amazing tools for the AI community.",
  "question": "What does Hugging Face do?"
}
``

