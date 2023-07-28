# Sensor Data Logger and Visualization Dashboard

This Project provides a solution for logging data from an ultrasonic sensor and a DHT11 temperature/humidity sensor, as well as visualizing the collected data in an interactive dashboard. The script runs on a Raspberry Pi and uses the RPi.GPIO, Adafruit_DHT, pandas, plotly.graph_objects, and Dash libraries.

## Prerequisites

Before running the script, ensure you have the following components and libraries installed:

-   Raspberry Pi with RPi.GPIO library installed.
-   DHT11 temperature/humidity sensor and an ultrasonic sensor connected to the Raspberry Pi GPIO pins.
-   Adafruit_DHT, pandas, plotly.graph_objects, and Dash libraries installed.

## How to Use

1. Upload the script to your Raspberry Pi or clone the repository from GitHub.

2. Connect the DHT11 temperature/humidity sensor to GPIO 4 and the ultrasonic sensor to GPIO 23 (TRIG_PIN) and GPIO 24 (ECHO_PIN).

3. Install the required libraries:

    ```
    pip install RPi.GPIO
    pip install Adafruit_DHT
    pip install pandas
    pip install plotly
    pip install dash
    ```

4. Run the script to start logging sensor data to the `sensor_data.csv` file:

    ```
    python rpi.py
    ```

5. Run the script to Launch and Access the dashboard on your web browser:

    ```
    python visualize.py
    ```

## Sensor Data Logger

-   Collects data from the ultrasonic sensor (distance) and the DHT11 sensor (temperature and humidity).

-   Data is saved to the CSV file `sensor_data.csv` with columns for distance (cm), temperature (°C), humidity (%), and date/time.

-   Press `Ctrl+C` to stop the data logging.

## Visualization Dashboard

-   The dashboard displays real-time updates of the temperature, humidity, and distance values from the logged data.

-   It includes gauge charts showing the current temperature, humidity, and distance values.

-   Scatter plots visualize the variation of temperature, humidity, and distance over time.

-   The dashboard updates every 10 seconds to provide near real-time visualization.

## Customize and Extend

Feel free to modify the script to suit your specific project requirements. You can add more sensors, customize the visualization, or implement additional features based on your needs.

**Note:** Ensure that you have write permissions in the directory where the script is located to save the CSV file successfully.
