# module to get cpu and memory metric
import psutil 

# app created with flask
from flask import Flask
app = Flask(__name__) 

# ran on home path
@app.route("/") 

# function to display cpu and memory utilization
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = "Live System Information"
    if cpu_percent > 80: 
        Message = "HIGH CPU UTILIZATION DETECTED. PLEASE SCALE UP"
    if mem_percent > 80:
        Message = "HIGH MEMORY UTILIZATION DETECTED. PLEASE SCALE UP"
    return f"{Message}: CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"

# run app on local machine
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')