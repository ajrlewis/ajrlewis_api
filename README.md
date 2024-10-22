# ajrlewis_api

A.J.R.Lewis API served by FastAPI (optimized for serverless Vercel deployment).

See the docs: https://api.ajrlewis.com/docs

## Environment Variables

```bash
PYTHONPATH="${PYTHONPATH}:src/"
SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://user:password@postgresserver/db"
LOGURU_LEVEL="DEBUG"
HF_TOKEN="<Your Hugging Face API Key"
```

## Migrations

1. Create an alembic directory for migrations:

```bash
source venv/bin/activate
alembic init alembic
```

2. Make the following changes to the `alembic/env.py` file:

```python
import os

section = config.config_ini_section
config.set_section_option(
    section, "sqlalchemy.url", os.environ.get("SQLALCHEMY_DATABASE_URL")
)
```

and

```python
from src.models import Base

target_metadata = Base.metadata
```

3. Create the database and models specified in `__init__.py` in `src/models`:

```bash
alembic revision --autogenerate -m "Init"
alembic upgrade head
```

## API Examples

### Image

### Text Extraction from Image

### Chat

### Data Extraction from Text

```bash
curl -X 'POST' \
  'https://api.ajrlewis.com/chat/extract/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Mariana Anderson UI / UX Designer & +123-456-7890 +123-456-7890 @ www.reallygreatsite.com >» hello@reallygreatsite.com ) 123 Anywhere St., Any City, ST 12345 Liceria & Co. Real Estate",
  "data_points": {
        "full_name": "The full name of card.",
        "job_title": "The job title of the card.",
        "company": "The name of the company.",
        "phone_number": "The phone number.",
        "email": "The email address.",
        "URL": "The website URL.",
        "address": "The location/address."
    }
}'
```

```json
{
  "full_name": "Mariana Anderson",
  "job_title": "UI / UX Designer",
  "phone_number": "+123-456-7890",
  "email": "hello@reallygreatsite.com",
  "URL": "www.reallygreatsite.com",
  "address": "123 Anywhere St., Any City, ST 12345"
}
```

## API Flow Examples

### Business Card Image Read and Contact Extraction

Step 1. (img) -> api.ajrlewis.com/image/extract-text -> (text)

Step 2. (text, data_points) -> api.ajrlewis.com/chat/extract -> (data)

```bash
'{
    "full_name": "the ...",
    "company": "the ...",
    "job_title": "the ...",
    "phone_number": "the ...",
    "email": "the ...",
    "social": "the ..."
}'
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## TODO

### Using llmkit + imagekit

- image/card

- image/card/reader
    - Returns a V-card object of the supplied PNG image.

### Using imagekit + nostrkit

- nostr/events
    - get
        - query npub, kind, tags
    - post
        - nsec, kind, tags, content

- nostr/card
    - Given an npub, create back and front business card PNG

- web/
    Extracts text from website

