#coding=utf-8
# from cookbook example,给定开始、结束日期，并holidays天数，每周去除的days_off，得到工作日天数
from dateutil import rrule
import datetime
def workdays(start, end, holidays=0, days_off=None):
	if days_off is None:
		days_off = 5, 6
	# 默认:周六和周日
	workdays = [x for x in range(7) if x not in days_off]
	days = rrule.rrule(rrule.DAILY, dtstart=start, until=end,
	byweekday=workdays)
	return days.count( ) - holidays
if __name__ == '__main__':
	# 主脚本运行时的测试代码
	testdates=[(datetime.date(2004,9,1),datetime.date(2004,11,14),2),
	(datetime.date(2003,2,28),datetime.date(2003,3,3),1),]
	def test(testdates, days_off=None):
		for s, e, h in testdates:
			print'total workdays from %s to %s is %s with %s holidays'%(s,e,workdays(s,e,h,days_off),h)
	test(testdates)
	test(testdates, days_off=[6])

