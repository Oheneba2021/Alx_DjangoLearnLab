# Social Media API (Django + DRF)

## Setup

### 1. Install dependencies
```bash
pip install django djangorestframework djangorestframework-authtoken pillow


## Posts & Comments API

Base URL: `/api/`

Authentication: Token  
Header: `Authorization: Token <token>`

### Posts
- `GET /posts/` — list posts (paginated)
- `POST /posts/` — create post (auth required)
- `GET /posts/{id}/` — retrieve post
- `PATCH /posts/{id}/` — update post (owner only)
- `DELETE /posts/{id}/` — delete post (owner only)

Search:
- `GET /posts/?search=<text>` searches `title` and `content`

Example create post:
```json
{
  "title": "My first post",
  "content": "Hello API world"
}