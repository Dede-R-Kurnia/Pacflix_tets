from datetime import datetime
from dateutil import relativedelta

from plan import basic_plan, standard_plan, premium_plan
from user import User

user_1 = User("Chi Ming", basic_plan, datetime.strptime('2011-08-15 12:00:00', '%Y-%m-%d %H:%M:%S'))

user_1.invoice

date1 = datetime.strptime('2011-08-15 12:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
r = relativedelta.relativedelta(date2, date1)
r

user_1.upgrade_plan(standard_plan)

user_1.invoice