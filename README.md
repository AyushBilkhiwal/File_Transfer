# File_Transfer
File Transfer System: Client-Server Architecture 
Report by Ayush Bilkhiwal [CS23M119] 
1. ROLE OF CLIENT: 

The client in the file transfer system plays a crucial role in interacting with the server 
to perform various file operations. Its primary responsibilities include: 

• Establishing Connection: The client initiates a connection request to the server using 
the server's IP address and port number. 

• Sending Commands: It sends commands to the server based on user input. These 
commands include requesting a list of files, uploading files, downloading files, deleting 
files, logging out, and requesting help information. 

• Receiving Responses: The client receives responses from the server, which include 
acknowledgments, file content, error messages, and help information. 

• Displaying Information: It displays information received from the server to the user, 
facilitating user interaction and providing feedback on the status of file operations. 
# 2. ROLE OF SERVER: 
The server acts as the central component in the file transfer system, responsible for 
managing client connections and handling file operations. Its main functions include: 
• Listening for Connections: The server listens for incoming connection requests from 
clients on a specified IP address and port. 

• Handling Client Requests: Upon establishing a connection, the server receives 
commands from the client, interprets them, and performs corresponding file operations 
such as listing files, uploading files, downloading files, deleting files, logging out clients, 
and providing help information. 

• Multithreading: To handle multiple client connections simultaneously, the server 
employs multithreading. Each client connection is assigned to a separate thread, allowing 
concurrent execution of client requests and preventing blocking of other clients. 

• Managing File Operations: The server manages file operations, including reading, 
writing, listing, and deleting files in the server's directory based on client requests. 
# 4. JUSTIFICATION OF MULTITHREADS: 
Here's how multithreading is used in the project: 
• Thread Creation: When a new client connection is accepted (server.accept()), a new 
thread is created using threading.Thread. This thread is responsible for handling the client's 
requests. 

• Thread Execution: Each thread executes the handle_client function, passing the 
connection socket and client address as arguments. This function handles all communication 
with the client. 

• Concurrency: As multiple threads are created, each handles a separate client connection 
independently. This allows the server to handle multiple clients simultaneously without 
blocking. 

• Scalability: By employing multithreading, the server can scale to accommodate more client 
connections as needed. Each new connection is handled in its own thread, ensuring that the 
server can efficiently manage multiple concurrent clients. 
Overall, multithreading is utilized in the server component of the project to enable 
concurrent handling of client connections, improving responsiveness and scalability of the 
file transfer system. 
# 5. Demonstration of the Project 
Sending Files (Client Perspective): 

• Connect to the Server: Run the client.py script to connect to the server.From the HELP 
command you can get the list of features and how to use them 
"LIST: List all the files from the server.\n" 
"UPLOAD <path>: Upload a file to the server.\n" 
"DELETE <filename>: Delete a file from the server.\n" 
"LOGOUT: Disconnect from the server.\n" 
"DOWNLOAD <filename>: Send the file from the server to the requesting client.\n" 
"HELP: List all the commands." 
# Downloading Files (Client Perspective): 
• Connect to the Server: Ensure that you're connected to the server by running the client.py 
script. 
• Request File List: Enter the command LIST to request a list of files available on the server 
and download the file from the server side. 
> LIST 
"DOWNLOAD <filename>: Send the file from the server to the requesting client.\n" 
Other Features (Client Perspective): 

• List Files: Enter the command LIST to request a list of files available on the server. 

• Delete File: Enter the command DELETE <filename> where <filename> is the name of the 
file you want to delete. 

• Log Out: Enter the command LOGOUT to disconnect from the server and exit the client 
application.

• Help: Enter the command HELP to request help information about available commands. 
Handling Requests (Server Perspective): 

• Accept Connection: The server listens for incoming connections from clients. 

• Handle Client Requests: Upon accepting a connection, the server receives commands from 
the client and executes corresponding operations such as uploading files, downloading files, 
listing files, deleting files, etc. 

• Multithreading: Each client connection is handled in a separate thread to allow concurrent 
processing of client requests and prevent blocking. 

• Respond to Client: The server sends responses back to the client indicating the status of the 
requested operation, file content, error messages, or help information. 
By following these steps, users can effectively upload files to the server, download files from 
the server, and utilize other features of the file transfer system both from the client's and 
server's perspective. 
