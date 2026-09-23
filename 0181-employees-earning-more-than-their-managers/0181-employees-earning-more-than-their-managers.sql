select e.name as `Employee`
from Employee e
left join Employee m on m.id = e.managerId
where m.salary < e.salary;