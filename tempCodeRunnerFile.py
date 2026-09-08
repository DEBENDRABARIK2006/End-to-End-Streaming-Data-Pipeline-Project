
print("Connection string exists:",
      os.getenv("CONNECTION_STRING") is not None)

print("Event Hub name:",
      os.getenv("EVENT_HUBNAME"))