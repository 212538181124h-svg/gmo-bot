import os
import sys

def diag():
    print("//////////////////////////////////////////////////")
    print("STARTING IMMEDIATE DIAGNOSTIC...")
    token = os.environ.get('PINTEREST_ACCESS_TOKEN')
    print(f"DEBUG: TOKEN STATUS -> {'FOUND' if token else 'NOT FOUND'}")
    print("SUCCESS: SYSTEM CHECK COMPLETE. EXITING.")
    print("//////////////////////////////////////////////////")
    sys.exit()

if __name__ == "__main__":
    diag()
