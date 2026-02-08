# Advanced API Project (Books)

## Endpoints

Base path: `/api/`

### Public (no authentication required)
- `GET /books/`  
  Lists all books. Supports optional filters:
  - `?author=<author_id>`
  - `?year=<publication_year>`
  Optional search/ordering:
  - `?search=<text>` (searches by title)
  - `?ordering=publication_year` or `?ordering=title`

- `GET /books/<id>/`  
  Retrieves a single book by ID.

### Protected (authentication required)
- `POST /books/create/`  
  Creates a new book. Requires JSON:
  ```json
  { "title": "Example", "publication_year": 2000, "author": 1 }
