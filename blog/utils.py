import re
from datetime import datetime
from sqlalchemy import or_

from .models import Post

WORD_RE = re.compile(r"\w+")


def tokenize(q):
    if not q:
        return []
    return [t.lower() for t in WORD_RE.findall(q) if len(t) > 1]


def score_post_for_query(post, tokens):
    text = ((post.title or "") + " " + (post.content or "")).lower()
    match_count = sum(text.count(t) for t in tokens)

    # small recency boost (newer posts score slightly higher)
    try:
        age_seconds = (datetime.utcnow() - post.date_created).total_seconds()
        recency = 1.0 / (1 + age_seconds / (3600 * 24 * 30))
    except Exception:
        recency = 0

    return match_count + recency


def recommend_for_query(query, limit=6, session=None):
    """Return top posts matching `query` using a simple SQL LIKE + python scoring.

    - session should be the SQLAlchemy session (e.g. db.session).
    - limit controls number of returned posts.
    """
    tokens = tokenize(query)
    if not tokens or session is None:
        return []

    # broad candidate set (limit to keep it fast)
    filters = []
    for t in tokens:
        pattern = f"%{t}%"
        filters.append(Post.title.ilike(pattern))
        filters.append(Post.content.ilike(pattern))

    candidates = session.query(Post) \
        .filter(or_(*filters)) \
        .filter(Post.is_published == True) \
        .limit(300).all()

    scored = []
    for p in candidates:
        s = score_post_for_query(p, tokens)
        if s > 0:
            scored.append((s, p))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored[:limit]]
