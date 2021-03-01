# 0x0D. SQL - Introduction

## General

    What’s a database
    What’s a relational database
    What does SQL stand for
    What’s MySQL
    How to create a database in MySQL
    What does DDL and DML stand for
    How to CREATE or ALTER a table
    How to SELECT data from a table
    How to INSERT, UPDATE or DELETE data
    What are subqueries
    How to use MySQL functions

## Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

nstall MySQL 5.7 on Ubuntu 14.04 LTS

        $ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
        $ sudo apt-get update
        $ sudo apt-get install mysql-server-5.7
        ...
        $ mysql --version
        mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
        $

Don’t forget your root password

Connect to your MySQL server:

        $ mysql -hlocalhost -uroot -p
        Password: 
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 42
        Server version: 5.7.8-rc MySQL Community Server (GPL)

        Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> 
        mysql> quit
        Bye
        $

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common

