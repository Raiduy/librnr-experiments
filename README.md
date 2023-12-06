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
1. Open PowerShell with admin privileges.
2. Find the `python.exe` path for your python version Run `<your-python.exe-path> vr_runner.py` to start the script.
3. The script will use the `config.json` file to determine which experiments to run. Since Beat Saber cannot be launched and stopped via the command line reliably yet, it is recommended to launch Beat Saber manually when the `Starting BatteryManager logging... Sleep for 5 seconds to allow BatteryManager to start.` output is shown, and stop Beat Saber when the `Stopping trace, please wait...` output is shown.
4. After the script is done, you will be able to find a copy of the `config.json` file in the directory with the same name as the `experiment_name` in the config file. The directory will also contain each run of the experiment along with all the data associated with it.