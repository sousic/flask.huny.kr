--회원정보 테이블
CREATE TABLE `member` (
	`seq`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`user_id`	TEXT NOT NULL,
	`user_pwd`	TEXT NOT NULL,
	`pwd_fail_cnt`	INTEGER DEFAULT ''0'',
	`user_name`	TEXT,
	`create_date`	TEXT,
	`last_login`	TEXT,
	`is_del`	INTEGER DEFAULT ''0'',
	`is_confirm`	INTEGER DEFAULT ''0'',
	`is_login_lock`	INTEGER DEFAULT ''0''
);

--입금내역
CREATE TABLE deposit
(
    seq INTEGER PRIMARY KEY,
    year TEXT,
    month TEXT,
    user_id TEXT,
    amount TEXT,
    reg_date TEXT
);