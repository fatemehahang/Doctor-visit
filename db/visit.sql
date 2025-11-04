create table if not exists visit(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    phone_number text not null,
    doctor_name text not null,
    date_time text not null,
    description text not null
);