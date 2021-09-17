# Python Wrapper for Smitch APIs

```
# Instantiate the Class Object like this :- 
smitch = Smitch(API_KEY)

# List all the users added to your app like :-
print(smitch.users())

# Instantiate the User Object Like :-
user = smitch.user(user_id)

# Instantiate the Device Object Like :-
device = user.device(device_id)

3 methods to control your bulb :-
device.on()
device.off()
device.change_state(boolean_state_of_desired_result, [r,g,b]) 
```
