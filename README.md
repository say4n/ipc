# IPC 
InterProcess Communication

## comparison

Method	Used	| Merits 			| Demerits
----------------|-------------------|---------------
Named Pipes 	| Used in Unix for a lot of things. Fast too.| Locks execution.
TCP Sockets (with ZeroMQ) | Very easy to implement. | Fast but has extra overhead for the protocol.
Producer Consumer Queue | Very easy to implement, faster than TCP Sockets | Keyboard Interrupts aren't gracefully handled.   



