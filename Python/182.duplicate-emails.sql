

select Email
from Person
group by Email
having count(1) > 1

--  或者
select Email from Person group by Email having count(Email) > 1