import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done|delete]")
        return
    
    command = sys.argv[1]
    print(f"Command received: {command}")

if __name__ == "__main__":
    main()