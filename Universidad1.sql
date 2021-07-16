create database Universidad1;

use Universidad1;

create table cursos1(
Codigo int not null,
Nombre varchar(30),
Creditos varchar(30)
);


insert into cursos1(Codigo, Nombre , Creditos)
values
	(100001, "Fisica General" , "5"),
    (100002, "Introducción a la ing." , "1"),
    (100003, "Matematica discreta" , "4"),
    (100004, "Programacion intermedia" , "6"),
    (100005, "Teoria de sistemas" , "3");

DELETE FROM personal WHERE nombre = 'Maria'

drop database prueba2
use prueba1
delete from personal where id=1
select * from personal