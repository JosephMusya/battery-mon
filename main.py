import psutil
import datetime
import subprocess as s
import os
import threading
import time
MAX_BATT = 100
MIN_BATT = 5
PROG_DELAY = 10
class BatteryThread(threading.Thread):
    
    def run(self):
        while True:
            battery = self.get_battery()
            battery_info = ''
            if battery:
                battery_info = str(self.log_battery_info(battery))

            else:
                raise BaseException("Battery not found!")  
            
            # print("---------------")                         
            # print(battery_info)               
            # print("---------------")             
                        
            time.sleep(PROG_DELAY)
                  
    def get_time(self, hrs=True):
        if hrs:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%H:%M")
            return formatted_time   + ' HRS'  
        else:
            return datetime.datetime.now()  

    def log_battery_info(self, battery):
        
        notif_send = False

        percent = int(battery.percent)
        charging = battery.power_plugged
        
        msg = ''
        if charging:
            msg = "Charging"
        if not charging:
            msg = "Not Charging"
        
        local_time = self.get_time(hrs=False)
            
        
        current_dir = os.path.dirname(os.path.realpath(__name__))
        notif_icon = os.path.join(current_dir, 'bat-mon.png')
        
        app_name = "BattMon"
        
        time = self.get_time()  
        
        if (percent == MAX_BATT) and charging and  (not notif_send):
            s.call(["notify-send", "-u", "critical", "-i", notif_icon, "-a", app_name, f'Battery fully charged - {percent}%', f'Unplug your PC!   {time}',])        
            notif_send = True
            return f'Battery: {percent}% \n{msg} \nTime: {local_time}'
        
        elif (percent == MAX_BATT) and not charging:
            return
        
        elif (percent < MIN_BATT )and not charging and (not notif_send):
            s.call(["notify-send", "-u", "critical", "-i", notif_icon, "-a", app_name, f'Battery critically low - {percent}%', f'Plug in your PC!   {time}',])        
            notif_send = True
            return f'Battery: {percent}% \n{msg} \nTime: {local_time}'
        
        elif (percent >= MIN_BATT) and percent < MAX_BATT:
            # s.call(["notify-send", "-u", "critical", "-i", notif_icon, "-a", app_name, f'Battery fully charged - {percent}%', f'Unplug your PC!   {time}',])
            notif_send = False
            return f'Battery: {percent}% \n{msg} \nTime: {local_time}'
        
        else:
            raise BaseException("Battery not configured!")
    
    def get_battery(self):
        battery = psutil.sensors_battery()
        return battery

def main():

    batt_thread = BatteryThread()
    batt_thread.start()

if __name__ == '__main__':
    main()