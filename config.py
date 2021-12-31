import os
ENV = "PROD" if os.environ.get('ENV') == "PROD" else "DEV"
print("ENV------------->",ENV)
