import os

antiguo = os.path.join("logs", "error.log")
nuevo = os.path.join("logs", "error.txt")
os.rename(antiguo, nuevo)