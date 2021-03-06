/*DROP TABLE IF EXISTS posts;*/

CREATE TABLE IF NOT EXISTS  products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    productname TEXT NOT NULL,
    brand TEXT NOT NULL,
    category TEXT NOT NULL,
    stockstatus TEXT NOT NULL,
    store TEXT NOT NULL,
    quantity INTEGER,
    UNIQUE (productname,store)  ON CONFLICT ROLLBACK
);
