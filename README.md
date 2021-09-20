# Python Wrapper for Smitch APIs

Step 1:-
Register at : https://developer.mysmitch.com/

Step 2:-
Get your API KEY

Step 3:-
Add your account with devices as the tester.

DONE!

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

or

device.on([r,g,b])

device.off()
```
