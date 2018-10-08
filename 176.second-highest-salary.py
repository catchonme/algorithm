#!/usr/bin/python3

# 思路1
select Salary SecondHighestSalary from Emplyee
union
select null
order by SecondHighestSalary desc limit 1, 1

# 思路2
select (
    select distinct Salary from Employee order by Salary Desc limit 1, 1
) as SecondHighestSalary