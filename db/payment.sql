create table if not exists payment(
    id integer primary key autoincrement,
    transaction_type text not null,
    payment_type text not null,
    date_time text not null,
    patient_id text not null,
    total_amount text not null,
    description text not null
);