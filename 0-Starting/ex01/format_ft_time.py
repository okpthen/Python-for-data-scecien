import datetime
import time

time = time.time()
dt_now = datetime.datetime.today()
strdt = dt_now.strftime('%b %d %Y')
print(f"Seconds since January 1, 1970: {time:,.4f} or {time:.2e} int scientific notion")
print(strdt)