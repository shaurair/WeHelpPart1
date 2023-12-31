## 要求三:SQL CRUD
### 1. create members
command line
```
INSERT INTO member(name,username,password) VALUES('testname1','test','test');
INSERT INTO member(name,username,password,follower_count) VALUES('testname2','user2','userPWD2',1);
INSERT INTO member(name,username,password,follower_count) VALUES('testname3','user3','userPWD3',2);
INSERT INTO member(name,username,password,follower_count) VALUES('testname4','user4','userPWD4',3);
INSERT INTO member(name,username,password,follower_count) VALUES('testname5','user5','userPWD5',4);
```
results

<img src="pics/task3_add_members.png" style="width:700px;">

### 2. read all members
command line
```
SELECT * FROM member;
```
results

<img src="pics/task3_all_member.png" style="width:700px;">

### 3. read all members from newest to oldest
command line
```
SELECT * FROM member ORDER BY time DESC;
```
results

<img src="pics/task3_time_order.png" style="width:700px;">

### 4. read 2nd~4th newest members
command line
```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
results

<img src="pics/task3_time_2to4.png" style="width:700px;">

### 5. read 'test' user
command line
```
SELECT * FROM member WHERE username = 'test';
```
results

<img src="pics/task3_user_test.png" style="width:700px;">

### 6. read 'test' user whose password is 'test'
command line
```
SELECT * FROM member WHERE username = 'test' and password = 'test';
```
results

<img src="pics/task3_user_pwd_test.png" style="width:700px;">

### 7. update name for 'test' user
command line
```
SET SQL_SAFE_UPDATES = 0;
UPDATE member SET name = 'test2' WHERE username='test';
```
results

<img src="pics/task3_update_name.png" style="width:500px;">

## 要求四:SQL Aggregate Functions 
### 1. get total number of members
command line
```
SELECT count(*) FROM member;
```
results

<img src="pics/task4_count.png" style="width:500px;">

### 2. get sum of follower count of all members
command line
```
SELECT SUM(follower_count) FROM member;
```
results

<img src="pics/task4_sum.png" style="width:500px;">

### 3. get average of follower count of all members
command line
```
SELECT AVG(follower_count) FROM member;
```
results

<img src="pics/task4_avg.png" style="width:500px;">

## 要求五:SQL JOIN
### 1. create message and add some messages
command line
```
CREATE TABLE message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    FOREIGN KEY(member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT NOW()
);

INSERT INTO message(member_id, content, like_count) VALUES(1, 'GOOD :)', 2);
INSERT INTO message(member_id, content, like_count) VALUES(1, '讚讚！', 3);
INSERT INTO message(member_id, content, like_count) VALUES(3, 'XD', 5);
INSERT INTO message(member_id, content, like_count) VALUES(4, '平安喜樂', 0);
```
results

<img src="pics/task5_create_message_table.png" style="width:500px;">
<img src="pics/task5_create_message.png" style="width:500px;">

### 2. show all message with member's name
command line
```
SELECT message.*, member.name FROM message INNER JOIN member ON member.id = message.member_id;
```
results

<img src="pics/task5_all_msg_with_name.png" style="width:500px;">


### 3. show all messages of username 'test' with member's name
command line
```
SELECT message.*, member.name, member.username FROM message INNER JOIN member ON member.id = message.member_id WHERE username = 'test';
```
results

<img src="pics/task5_usr_test_msg_with_name.png" style="width:800px;">

### 4. show average like counts of all messages of username 'test'
command line
```
SELECT AVG(like_count) FROM message INNER JOIN member ON member.id = message.member_id WHERE username = 'test';
```
results

<img src="pics/task5_usr_test_avg_like_cnt.png" style="width:500px;">
