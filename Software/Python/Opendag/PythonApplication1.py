import grovepi
import grove_rgb_lcd
import time

# Set the pin for the Ultrasonic Ranger
ultrasonic_ranger = 4
buzzer_pin = 7
led = 3

#set Pin mode Led to output
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)


#Initialize the LCD
grove_rgb_lcd.setRGB(0, 255, 0)  # Set the initial color to green

grovepi.pinMode(buzzer_pin, "OUTPUT")

def get_distance():
    try:
        # Read the distance in centimeters
        distance = grovepi.ultrasonicRead(ultrasonic_ranger)
        return distance
    except Exception as e:
        print("Error:", e)
        return None

try:
    while True:
        distance = get_distance()
        if distance is not None:
            print("Distance:", distance, "cm")
            if distance < 100:
                # Change the LCD color to red
                message = f"Afstand is      teklein {distance}cm"

                grove_rgb_lcd.setText(message)
                grove_rgb_lcd.setRGB(255, 0, 0)
                grovepi.digitalWrite(buzzer_pin, 1)
                time.sleep(0.1)  # Wait for 0.2 second
                grovepi.digitalWrite(buzzer_pin, 0)

                grovepi.analogWrite(led,255)        # Send HIGH to switch on LED
                print ("LED ON!")
                time.sleep(0.1)

                grovepi.analogWrite(led,0)        # Send LOW to switch off LED
                print ("LED OFF!")
                time.sleep(0.1)
            else:
                # Change the LCD color to green
                messageB = f"Afstand is Groot {distance}cm"
                grove_rgb_lcd.setText(messageB)
                grove_rgb_lcd.setRGB(0, 255, 0)
        time.sleep(1)  # Delay for 1 second
except KeyboardInterrupt:
    print("Program terminated by user")
