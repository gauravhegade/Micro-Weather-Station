import csv
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

# Ultrasonic sensor pins
TRIG_PIN = 23
ECHO_PIN = 24

# Temperature/Humidity sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# CSV file path
CSV_FILE = "sensor_data.csv"


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)


def measure_distance():
    # Send ultrasonic signal
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Measure echo duration
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate distance based on speed of sound
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound (343 m/s) / 2

    return distance


def measure_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature


def save_to_csv(distance, temperature, humidity):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([distance, temperature, humidity])


def main():
    setup()

    try:
        while True:
            distance = measure_distance()
            humidity, temperature = measure_temperature_humidity()

            print(f"Distance: {distance:.2f} cm")
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Humidity: {humidity:.2f}%")

            save_to_csv(distance, temperature, humidity)

            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
