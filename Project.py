import shutil
def get_free_space(path):
    """Get the amount of free space in bytes on the given path."""
    try:
        free_space = shutil.disk_usage(path).free
        return free_space
    except Exception as e:
        return str(e)

def bytes_to_gb(bytes):
    """Convert bytes to gigabytes."""
    gb = bytes / (1024 ** 3)
    return gb

def main():
    drive = input("Enter the drive or directory path (e.g., C:/ or /home/user): ")
    free_space_bytes = get_free_space(drive)

    if isinstance(free_space_bytes, int):
        free_space_gb = bytes_to_gb(free_space_bytes)
        print(f"Free space on {drive}: {free_space_gb:.2f} GB")
    else:
        print(f"Error: {free_space_bytes}")

if __name__ == "__main__":
    main()
