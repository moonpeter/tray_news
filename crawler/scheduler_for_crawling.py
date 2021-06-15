import time

import schedule

from crawler.parser_cnet import get_list

# 5초마다 실행
schedule.every(5).seconds.do(get_list)
# 5분마다 실행
# schedule.every(5).minutes.do(get_list)

while True:
    schedule.run_pending()
    time.sleep(1)
