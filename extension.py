def main():
    file_name = input("File name: ").lower()
    return extensions(file_name)

def extensions(file):
    if ".jpeg" in file or ".jpg" in file:
        print("image/jpeg")
    elif ".gif" in file:
        print("image/gif")
    elif ".png" in file:
        print("image/png")
    elif ".pdf" in file:
        print("application/pdf")
    elif ".txt" in file:
        print("text/plain")
    elif ".zip" in file:
        print("application/zip")
    else:
        print("application/octet-stream")

main()