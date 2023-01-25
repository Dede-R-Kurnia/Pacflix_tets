from datetime import datetime
from dateutil import relativedelta
from dataclasses import dataclass

from plan import Plan

@dataclass
class User:
  username: str
  plan: Plan
  start_subs_time: datetime
  refferal_code: str=None

  def __post_init__(self):
    self.invoice = self.plan.price

  def upgrade_plan(self, new_plan):

    if new_plan.level <= self.plan.level:
      print("Plan tidak bisa downgrade!")
      return

    discount = 1
    difference = relativedelta.relativedelta(datetime.now(), self.start_subs_time)
    if difference.years > 1:
      discount = 0.95


    self.plan = new_plan
    self.start_subs_time = datetime.now()
    self.invoice = self.plan.price * discount