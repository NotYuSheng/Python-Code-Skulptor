# http://www.codeskulptor.org/#user45_boUV3WSIyL_4.py

# Yu Sheng 18/09/18
import simplegui
second = 0
minute = 0
hour = 0

# Update timer
def update_timer():
    global second
    second += 1

# Clock Format
def clock_format():
    global second
    global minute
    global hour
    global part3
    if(second > 59):
        minute += 1
        second = 0
    if(minute > 59):
        hour += 1
        minute = 0
    if(hour > 23):
        hour = 0
    if(hour < 10):
        part1 = "0" + str(hour);
    elif(hour < 24):
        part1 = str(hour);
    if(minute < 10):
        part2 = "0" + str(minute);
    elif(minute < 60):
        part2 = str(minute);
    if(second < 10):
        part3 = "0" + str(second);
    elif(second < 60):
        part3 = str(second);
    return part1 + ":"+ part2;

# Set Hour
def set_hour():
    global hour
    hour += 1;
    
# Set Minute
def set_minute():
    global minute
    minute += 1;
    
# Reset Second
def reset_second():
    global second
    second = 0;
    timer.stop()
    timer.start()

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(clock_format(), [90,112], 48, "White")
    canvas.draw_text(part3, [200,112], 20, "White")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Set Hour", set_hour)
frame.add_button("Set Minute", set_minute)
frame.add_button("Reset Second", reset_second)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000, update_timer)
# Every 1000 mili sec call timer_handler

# Start the frame animation
frame.start()
timer.start()
