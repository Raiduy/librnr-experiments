import os
import sys
import json
import subprocess
from time import sleep

STEAM_HOME = "C:\\Program Files (x86)\\Steam\\steamapps\\common"

def main():
    # get full path of current folder
    current_dir = os.path.dirname(os.path.realpath(__file__))

    config_file = "./config.json"
    with open(config_file) as f:
        config = json.load(f)

    OUTPUT_DIR = os.path.join(current_dir, config["device"])
    RUN_BENCH = os.path.join(current_dir, "runbench.ps1")
    
    for app in config["apps"]:
        TRACE_PATH = os.path.join(current_dir, config["device"], app["trace_path"])
        for i in range(config["repetitions"]):
            OUTPUT_DIR = os.path.join(OUTPUT_DIR, TRACE_PATH.split("record")[0] + "replay" +  TRACE_PATH.split("record")[1][0] + ".")
            # if not os.path.exists(OUTPUT_DIR):
            #     os.makedirs(OUTPUT_DIR)

            command = RUN_BENCH + ' -Mode "replay" ' + \
                      '-TraceFile "' + TRACE_PATH + '" ' + \
                      '-App "' + STEAM_HOME + app['exe_path'] + '" ' + \
                      '-OutDir "' + OUTPUT_DIR + str(i) + '"'
            
            print(command)
            p = subprocess.Popen(['powershell.exe', command], stdout=sys.stdout)
            p.communicate()
            # copy config.json to output directory
            # with open(os.path.join(OUTPUT_DIR + str(i), "config.json"), 'w') as outfile:
            #     json.dump(config, outfile, indent=4)
            print("Stop app")
            sleep(config["time_between_repetitions"])
        sleep(config["time_between_apps"])


if __name__ == "__main__":
    main()