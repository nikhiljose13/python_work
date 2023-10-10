create database cakehub;
use cakehub;

create table cake(
		id int auto_increment primary key,
        name varchar(200) unique,
        shape enum('rectangle','circle','square','heart','star') default 'circle'
        
        );

INSERT INTO cake (name)
VALUES
  ('Chocolate Cake'),
  ('Vanilla Cake'),
  ('Strawberry Cake'),
  ('Red Velvet Cake'),
  ('Carrot Cake');



create table cakevarient(
id int auto_increment primary key,
weight varchar(100) default '1kg',
price int not null,
cake_id int,
foreign key(cake_id) references cake(id) on delete cascade

);
select * from cake;
insert into cakevarient(price,weight,cake_id) values(2000,'1kg',4);
select * from cakevarient;

delete from cakevarient where cake_id=4 and pricr=1900;

alter table cakevarient add constraint unique(weight,price,cake_id);

select c.name,v.weight,v.price from cake as c,cakevarient as v where c.id=v.cake_id;


create table reviews(
					id int auto_increment primary key,
					user varchar(200) not null,
                    comment varchar(200) not null,
                    rating int not null check(rating<6),
                    cake_id int,
                    foreign key(cake_id) references cake(id) on delete cascade
					);
insert into reviews(user,comment,rating,cake_id) values("vinu","awsome",8,3);

select* from reviews;

desc cake;
select c.name,r.comment,r.rating,r.user  from cake as c ,reviews as r where c.id=r.cake_id;

select cake.name,reviews.rating,reviews.comment from cake left join reviews on cake.id=reviews.cake_id;

select cake.name,reviews.rating,reviews.comment from cake right join reviews on cake.id=reviews.cake_id;

select name  from cake where id in (select distinct (r1.cake_id) from reviews as r1,reviews as r2 where r1.cake_id=r2.cake_id and r1.id!=r2.id);
