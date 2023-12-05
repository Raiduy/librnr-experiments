import os
import sys
import json
import subprocess
from time import sleep

STEAM_HOME = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
TRACES_HOME = "C:\\Users\\radua\\VU_Ams\\MSc\\P2\\DS\\LabProject\\librnr\\scripts"
RUN_BENCH = "C:\\Users\\radua\\VU_Ams\\MSc\\P2\\DS\\LabProject\\librnr-experiments\\runbench.ps1"

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

    # copy config.json to output directory
    with open(os.path.join(output_main_dir, "config.json"), 'w') as outfile:
        json.dump(config, outfile, indent=4)

    for app in config["apps"]:
        for i in range(config["repetitions"]):
            command = RUN_BENCH + ' -Mode "replay" ' + \
                      '-TraceFile "' + TRACES_HOME + app['trace_path'] + '" ' + \
                      '-OutDir "' + os.path.join(output_main_dir, app['name']) + str(i) + '" '\
                      '-BMSampleRate "' + config['metrics']['BMSampleRate'] + '" ' + \
                      '-BMMetrics "' + ','.join(config['metrics']['BMMetrics']) + '" ' + \
                      '-OVRGPUMetrics "' + ','.join(config['metrics']['OVRGPUMetrics']) + '" '
                      # '-App "' + STEAM_HOME + app['exe_path'] + '" ' + \
            print(command)
            p = subprocess.Popen(['powershell.exe', command], stdout=sys.stdout)
            p.communicate()
            print("Stop app")
            sleep(config["time_between_repetitions"])
        sleep(config["time_between_apps"])
        

if __name__ == "__main__":
    main()