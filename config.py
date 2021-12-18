import os
ENV = "DEV" if os.environ['ENV'] == "DEV" else "PROD"
