show databases;
create database olx;
use olx;
create table vehicle (id int unique,
                     Name varchar(100),
                     km int not null,
                     price int not null,
                     woner_type varchar(100) not null,
                     model varchar(100) not null);
show tables;

insert into vehicle(id,name,km,price,woner_type, model)values(1,"cb350",25000,67000,"single",2020);
insert into vehicle(id,name,km,price,woner_type, model)values(2,"duke200",15000,69000,"third",2018);
insert into vehicle(id,name,km,price,woner_type, model)values(3,"hyness",25000,65000,"second",2023);
insert into vehicle(id,name,km,price,woner_type, model)values(4,"duke390",5000,120000,"single",2009);
insert into vehicle(id,name,km,price,woner_type, model)values(5,"unicorn",29000,62000,"single",2021);

select * from vehicle;

alter table vehicle add column location varchar(120) default "Kerala";

insert into vehicle(id,v_name,km,price,woner_type, model, location)values(6,"Activa",2000,32000,"single",2001,"TN");
insert into vehicle(id,v_name,km,price,woner_type, model, location)values(7,"Mastero",32000,28000,"single",2021,"Calicut");

select v_name,price from vehicle;

select * from vehicle where model>2020 and price>63000;

select * from vehicle where price>20000 and price<50000;
-- or
select * from vehicle where price between 20000 and 50000;

select * from vehicle where location ="Kerala";
select * from vehicle where location !="Kerala";

select max(price) from vehicle ;
select min(kms) from vehicle ;

select * from vehicle where price =(select max(price) from vehicle);
select * from vehicle where km =(select min(km) from vehicle);

select * from vehicle where km =(select min(kms) from vehicle) and location !="Kerala";

select * from vehicle order by price ASC ;
select * from vehicle order by price ASC limit 2;

update vehicle set price=140000 where id=4;
update vehicle set v_name="Honda Activa" where id=6;
update vehicle set location="TVM" where id=5;

delete from vehicle where id=4;

select * from vehicle;

drop table vehicle;