# librnr-experiments

## Before opening Quest Link
1. Connect Quest to PC via cable.
2. In a terminal, run `adb devices` to verify that Quest is connected.
3. Install the BatteryManager app on Quest by running `adb install -g <path-to-apk>`.
4. Start the BatteryManager app on Quest via
```bash
adb shell am start -n "com.example.batterymanager_utility/com.example.batterymanager_utility.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER
```
5. After the app starts, you can now connect the VR headset via adb wifi.
6. Run `adb tcpip 5555` to enable adb wifi.
7. Run `adb connect <ip-address-of-quest>:5555` to connect to Quest via adb wifi. The IP address can be found in the Quest settings > Wifi > `<Your Network>` > Scroll down until you see the IP address.
8. Run `adb devices` to verify that Quest is connected via adb wifi.
9. Disconnect the cable from the Quest.
10. Launch Quest Link.

## Using vr_runner.py
### Before running the script
* Add the steam folder to the environment variable `Path`. (`C:\Program Files (x86)\Steam`)
* Clone Vlad's [traffic shaper repo](https://github.com/Vlad2000Andrei/DistributedSystems-Traffic-Shaper)
* Install clumsy as per [his instructions](https://github.com/Vlad2000Andrei/DistributedSystems-Traffic-Shaper/blob/main/README.md).
* Configure the `config.json` file.

### Configuring the `config.json` file
* `experiment_name`: The name of the experiment. This will be used to create a directory with the same name as the experiment and all results will be stored there under the same file conventions as before.
* `clumsy`
  * `clumsy_scripts_path`: The path to the folder containing the clumsy scripts in Vlad's traffic shaper.
  * `clumsy_path`: Path to the clumsy executable.
  * `delay`, `delay_chance`, `bandwidth_KBps`, `drop_chance`: The values for the clumsy script. `-1` means disabled.
* `apps`
  * `name`: The name of the app. This will be used to create a directory with the same name as the app and all results will be stored there under the same file conventions as before.
  * `exe_name`: The name of the executable for the app. This is used by the `runbench.ps1` script to stop the app.
  * `steam_app_id`: ID of the app on Steam. This is used by the `runbench.ps1` script to start the app. The ID can be found on the app's Steam page >> Settings (Cog wheel) >> Properties >> Updates >> AppID (Below Background downloads).
  * `startup_time`: The time in seconds to wait for the app to start.


### Running the script
1. Open PowerShell with admin privileges.
2. Find the `python.exe` path for your python version Run `<your-python.exe-path> vr_runner.py` to start the script.
3. The script will use the `config.json` file to determine which experiments to run.
4. First the script will launch `clumsy` with the specified parameters, then `runbench.ps1`. The application should start shortly after the `Sleep 5 seconds...BatteryManager`. When the trace is done replaying, the app will automatically close (be patient). After all the iterations are done, the script will close `clumsy` and copy the config file to the experiment directory.