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
