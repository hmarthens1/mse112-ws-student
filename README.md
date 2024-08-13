
git clone under the /home/pi directory the repo:

```
git clone https://github.com/hmarthens1/mse112-ws.git](https://github.com/hmarthens1/mse112-ws-student.git

```

go into the directory

```
cd ~/mse112-ws

```

And then follow the package installation procedures below 

# MasterPi Packages
install these packages

1. yaml handle
```
sudo pip install pyyaml
```

2.rpi_ws281x
```
sudo pip install rpi_ws281x
```

3. RPi.GPio
```
sudo pip install RPi.GPIO
```
4. smbus2
```
sudo pip install smbus2
```



# example for MasterPi

Now that all the required packages are installed, test an example:

go into the directory

```
cd ~/mse112-ws/MasterPi/HiwonderSDK

```
run the example for RGB light


```
sudo python RGBControlDemo.py
```

# MasterPC Software

```
sudo apt-get install python3-pyqt5.qtsql
```

# example for MasterPC Software
```
cd ~/mse112-ws/MasterPi_PC_Software
```


```
python Arm.py
```



