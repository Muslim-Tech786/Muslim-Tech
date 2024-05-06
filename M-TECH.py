import os,platform
platForm=platform.machine()
if '64' in platForm:import main64
elif '32' in platForm:import main32
else:print('Your device can\'t support our tool');exit()