import socket
import os
IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
DOWNLOAD_DIR = "downloaded_files"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        split_data = data.split("@")
        cmd, msg = split_data[0], '\n'.join(split_data[1:])

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT)) 
            break
        elif cmd == "DOWNLOAD":
            filename = data[1]
            client.send(f"{cmd}@{filename}".encode(FORMAT))
            response = client.recv(SIZE).decode(FORMAT)

            if response.startswith("Content of the downloaded file"):
                # Create the download directory if it doesn't exist
                if not os.path.exists(DOWNLOAD_DIR):
                    os.makedirs(DOWNLOAD_DIR)

                # Extract file content from the response
                file_content = response.split("\n", 1)[1]

                # Write file content to a new file in the download directory
                download_path = os.path.join(DOWNLOAD_DIR, filename)
                with open(download_path, "w") as f:
                    f.write(file_content)

                print(f"File downloaded and saved to: {download_path}")
                
            else:
                print(response)  # Print or handle the received file content

        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "UPLOAD":
            path = data[1]

            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
