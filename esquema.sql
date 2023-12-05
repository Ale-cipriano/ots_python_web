DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
id integer primary key autoincrement,
titulo STRING not null,
texto STRING not null,
data_criacao TIMESTAMP NULL default current_timestamp
)