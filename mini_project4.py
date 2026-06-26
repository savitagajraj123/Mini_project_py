# generate code jo hame informed karega ki hr 2 ghante me pani pina he 

import time 
from plyer import notification

def water_reminder():
  while True :
    notification.notify(
      title="Water Reminder for Rubi",
      message="Time to drink water!",
      timeout=10
    )
    time.sleep(3600) # Wait for 1 hours 
    #   time.sleep(7200)
water_reminder()