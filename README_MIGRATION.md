Flask-Migrate setup

This project now uses Flask-Migrate (Alembic) to manage schema migrations.

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize migrations (first time):

```bash
export FLASK_APP=app.py
flask db init
flask db migrate -m "initial"
flask db upgrade
```

Make schema changes (after editing models):

```bash
flask db migrate -m "describe change"
flask db upgrade
```

Notes:
- The SQLite DB is stored at `instance/blog.db`.
- For development convenience the app still runs `db.create_all()` at startup if tables are missing,
  but production migrations should be applied with `flask db upgrade`.
 
Database URL and TLS
- To use an external MySQL/TiDB database, set the `DATABASE_URL` environment variable, for example:

```bash
export DATABASE_URL="mysql+pymysql://3oV8VJkcAKS4Fqn.root:aGexgrJIm6YIWj7B@gateway01.eu-central-1.prod.aws.tidbcloud.com:4000/blog"
```

- To enable TLS/SSL verification with PyMySQL, set `DB_SSL_CA` to the path of your CA certificate file:

```bash
export DB_SSL_CA=/path/to/ca.pem
```

When `DB_SSL_CA` is set the app will pass `connect_args={'ssl': {'ca': '/path/to/ca.pem'}}` to the SQLAlchemy engine.
