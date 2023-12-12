# Python Wrapper for Smitch APIs Documentation

## Overview
This Python wrapper allows you to interact with Smitch APIs, enabling control over various smart devices. 

## Getting Started

### Step 1: Register
First, register at [Smitch Developer Portal](https://developer.mysmitch.com/).

### Step 2: API Key
Obtain your unique API key after registration.

### Step 3: Add Tester
Add your account and link devices to it as a tester.

## Installation

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## Usage

### Setting Up
To begin, import the necessary module and instantiate the Smitch class:

```python
import requests
import functools
from smitch_api_wrapper import Smitch  # Ensure to import the correct class from your module

API_KEY = "Your_API_Key_Here"
smitch = Smitch(API_KEY)
```

### Listing Users
List all the users added to your app:

```python
print(smitch.users())
```

### Handling Users and Devices
Instantiate a User object and Device object as follows:

```python
user_id = "Your_User_Id"
user = smitch.user(user_id)

device_id = "Your_Device_Id"
device = user.device(device_id)
```

### Device Control
You can control your smart bulb using the following methods:

- Turn on the bulb:

  ```python
  device.on()
  ```

- Turn on the bulb with RGB color values:

  ```python
  device.on([r, g, b])  # Replace r, g, b with color values
  ```

- Turn off the bulb:

  ```python
  device.off()
  ```

### Error Handling
The wrapper includes custom exceptions for handling common errors like invalid API keys.

```python
class InvalidAPIKeyError(Exception):
    def __init__(self):
        super().__init__('The API Key you passed is invalid!')
```

## Advanced Features

- Retrieve detailed user information and device details.
- Control device traits like brightness, temperature.
- Manage scenes and automations.

Refer to the complete class definitions in the wrapper for more details on these features.

## Support

For issues, questions, or contributions, please refer to the repository's issue tracker or contact support at [support@mysmitch.com](mailto:support@mysmitch.com).
