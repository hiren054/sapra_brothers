import os
ENV = "PROD" if os.environ.get('ENV') == "PROD" else "DEV"
