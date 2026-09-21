select w.id
from weather w
inner join weather w2
where datediff(w.recorddate, w2.recorddate) = 1
and w.temperature > w2.temperature