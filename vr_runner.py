import os
import sys
import json
from time import sleep

STEAM_HOME = "steam\\test\\"
TRACES_HOME = "traces\\test\\"

def main():
    config_file = "./config.json"

    # open config.json file
    with open(config_file) as f:
        config = json.load(f)
    # create directory for output
    if not os.path.exists(config["experiment_name"]):
        os.makedirs(config["experiment_name"])

    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_main_dir = os.path.join(current_dir, config["experiment_name"])

    for app in config["apps"]:
        for i in range(config["repetitions"]):
            command = '.\\runbench.ps1 -Mode "replay" ' + \
                      '-TraceFile "' + TRACES_HOME + app['trace_path'] + '" ' + \
                      '-OutDir "' + os.path.join(output_main_dir, app['name']) + str(i) + '" '\
                      '-App "' + STEAM_HOME + app['exe_path'] + '" ' + \
                      '-BMSampleRate "' + config['metrics']['BMSampleRate'] + '" ' + \
                      '-BMMetrics "' + ','.join(config['metrics']['BMMetrics']) + '" ' + \
                      '-OVRGPUMetrics "' + ','.join(config['metrics']['OVRGPUMetrics']) + '" '
            print(command)
            print()
            sleep(config["time_between_repetitions"])
        sleep(config["time_between_apps"])
        

if __name__ == "__main__":
    main()