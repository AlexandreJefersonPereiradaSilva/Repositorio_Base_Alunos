CREATE TABLE message (
    id SERIAL PRIMARY KEY,
    channel INTEGER NOT NULL,
    source TEXT NOT NULL,
    content TEXT, NOT NULL
);

CREATE OR REPLACE FUNCTION notify_on_insert( RETURNS trigger AS )