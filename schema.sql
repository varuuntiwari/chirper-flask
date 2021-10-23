drop table if exists posts;

create table posts (
    id integer primary key autoincrement,
    name text not null,
    chirp text not null
);