# Overview

I made a Client/Server program where the client can send some options over to the server through the local area Network. It can also work over the internet if you replace the SERVER variable with your public IP address. What you do is run the server code and then run the client code on any computer with a connection to the server. Once you do, you can type in the options to get different Encouragements, Advice, or Comebacks.

I wrote this software to learn more about networks, how they work, and how to make them. Now that I understand hoe the work and how to connect them to other objects in the network, I want to use this with future projects. For instance, I would love to make a game and then share the client code with my friends so they could play over my server!

[Software Demo Video](https://youtu.be/I4q4AjM2NXQ)

# Network Communication

I used a Client/Server architecture that allows multiple clients to connect to a single server.

I am using utf-8 as my format to encode my messages between the client and server.

# Development Environment

Describe the tools that you used to develop the software
I used Visual Studio as my IDE and Windows Powershell.

I used python 3.10.2 as my programming language and these modules to make the code work: import socket, import threading, and import random.

# Useful Websites


* [Python Docs](https://docs.python.org/3.6/library/socket.html)
* [Youtube](https://www.youtube.com/)
* [Stack Overflow](https://stackoverflow.com/)

# Future Work

* I need to add more options and make it more robust, perhaps adding a website scraper to have it fill in the advice, comeback, and encouragement lists.
* I need to make sure that it works with a bunch of clients at once and how it handles it.
* I want to make it so that the user can add their own custom pieces of advice, comebacks, and encouragement that can be shared with other users.