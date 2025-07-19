from scripts import mobile_data_generate

import schedule
import time 

def data_gen_5_min():
    mobile_data_generate.main()
    

schedule.every(5).minutes.do(data_gen_5_min)

if __name__ == "__main__":
    
    while True:
        schedule.run_pending()
        time.sleep(1)