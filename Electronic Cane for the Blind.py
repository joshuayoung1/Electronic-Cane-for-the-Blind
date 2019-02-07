
# Import required Python libraries
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice 
from time import sleep, time

trig_low = OutputDevice(4)
echo_low = InputDevice(17)
motor = PWMOutputDevice(18)
trig_mid = OutputDevice(27)
echo_mid = InputDevice(22)
trig_hi = OutputDevice(24)
echo_hi = InputDevice(23)
#motor_mid = PWMOutputDevice(18) 

sleep (2)

#Now we will send a pulse for 10us
def get_pulse_time_low():
    trig_low.on()
    sleep(0.00001)
    trig_low.off()
    
    while echo_low.is_active == False:
        pulse_start_low = time()
    
    while echo_low.is_active == True:
        pulse_end_low = time()
    
    sleep(0.06)

    try:
        return pulse_end_low - pulse_start_low

    except:
        return 0.02
    
def get_pulse_time_mid():
    trig_mid.on()
    sleep(0.00001)
    trig_mid.off()
    
    while echo_mid.is_active == False:
        pulse_start_mid = time()
    
    while echo_mid.is_active == True:
        pulse_end_mid = time()
    
    sleep(0.06)

    try:
        return pulse_end_mid - pulse_start_mid

    except:
        return 0.02


def get_pulse_time_hi():
    trig_hi.on()
    sleep(0.00001)
    trig_hi.off()
    
    while echo_hi.is_active == False:
        pulse_start_hi = time()
    
    while echo_hi.is_active == True:
        pulse_end_hi = time()
    
    sleep(0.06)

    try:
        return pulse_end_hi - pulse_start_hi

    except:
        return 0.02


#print(get_pulse_time())

def calculate_distance_low(duration_low):
    speed = 34300
    distance_low = speed*duration_low/2
    print ("The lower distance is: ",distance_low)
    return distance_low


def calculate_distance_mid(duration_mid):
    speed = 34300
    distance_mid = speed*duration_mid/2
    #print (distance_mid)
    print ("The mid distance is: ",distance_mid)
    return distance_mid

def calculate_distance_hi(duration_hi):
    speed = 34300
    distance_hi = speed*duration_hi/2
    print ("The higher distance is: ",distance_hi)
    return distance_hi


#while True:
 #       duration_low = get_pulse_time_low()
  #      duration_mid = get_pulse_time_mid()
   #     distance_low = calculate_distance_low(duration_low)
    #    distance_mid = calculate_distance_mid(duration_mid)
        

def Calculate_vibration(distance_low):
    vibration=(((distance_low-2)*-1)/(300-2))+1
    return vibration

while True:
    duration_low = get_pulse_time_low()
    duration_mid = get_pulse_time_mid()
    duration_hi = get_pulse_time_hi()
    distance_low = calculate_distance_low(duration_low)
    distance_mid = calculate_distance_mid(duration_mid)
    distance_mid = calculate_distance_hi(duration_hi)
    vibration = Calculate_vibration(distance_low)
    try:
        motor.value = vibration
    except:
        motor.value = 0
    
    


