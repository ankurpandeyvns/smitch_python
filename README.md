# Python Wrapper for Smitch APIs Documentation

## Overview
This Python wrapper facilitates interaction with Smitch APIs, enabling control over various smart devices such as lights, thermostats, and more.

## Getting Started

### Step 1: Register
Sign up at the [Smitch Developer Portal](https://developer.mysmitch.com/) to access the API services.

### Step 2: API Key
After registration, obtain your unique API key, which is essential for authenticating API requests.

### Step 3: Add Tester
Link your Smitch account and devices as a tester to enable direct API interactions with your devices.

## Installation

Before proceeding, ensure Python is installed on your system. Download it from [python.org](https://www.python.org/). Then, install the `requests` package:

```bash
pip install requests
```

## Usage

### Initial Setup
Begin by importing the necessary modules and initializing the Smitch class with your API key:

```python
import requests
import functools
from your_module import Smitch  # Replace 'your_module' with the actual module name

API_KEY = "Your_API_Key_Here"
smitch = Smitch(API_KEY)
```

### Listing Users
Retrieve a list of all users associated with your app:

```python
users = smitch.users()
print(users)
```

### Managing Users and Devices
Interact with specific users and their devices:

#### Instantiate User Object

```python
user_id = "Your_User_Id"  # Replace with an actual user ID
user = smitch.user(user_id)
```

#### Retrieve and Manage Devices

```python
# Get the list of devices associated with the user
devices = user.devices()

# Select a device by its ID
device_id = devices[0]['device_id']  # Adjust index based on your device list
device = user.device(device_id)
```

### Device Control
Control your smart devices using these methods:

#### Turn on the Device

```python
device.on()  # Turns on the device
```

#### Turn on the Device with RGB Values

```python
r, g, b = 255, 0, 0  # Example RGB values for red color
device.on([r, g, b])
```

#### Turn off the Device

```python
device.off()  # Turns off the device
```
