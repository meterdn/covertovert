# What is a Covert Channel?
A covert channel is a method of communication that uses different ways to transmit information. It is often used to send data secretly, bypassing normal communication mechanisms. Instead of explicitly using a dedicated protocol or channel for data transfer, a covert channel manipulates existing protocol fields, timings, or other mechanisms to secretly embed information.


# Covert Storage Channel that exploits Protocol Field Manipulation using QR Flag field in DNS [Code: CSC-PSV-DNS-QRF]

Our implementation in this homework uses a Covert Storage Channel that exploits the QR (Query/Response) flag field in the DNS (Domain Name System) header. The QR field is a single bit typically used to indicate whether a DNS packet is a query (0) or a response (1). In this channel, we repurpose this bit to encode binary information covertly.

To enhance security and encryption, we encoded the message using its **transition state** in each bit. The encoding works as follows in the receiver:

1. The very first bit of the message is directly placed into the DNS QR bit of the first packet.
2. Subsequent bits are updated based on the **previous bit** of the message, following these rules:
   - If the **previous bit** and the **current bit** are the **same**, we send **0** in the QR bit, implying the bit has **not changed** in this message.
   - If the **previous bit** and the **current bit** are **different** (e.g., `01` or `10`), we send **1** in the QR bit, implying the bit has **changed**, and the **next bit must be toggled**.

Receiver decodes them as follows:

1. The very first bit of the message is directly the DNS QR bit of the first packet.
2. Subsequent bits are updated based on the **previous bit** of the message, following these rules:
   - If the QR bit is **0**, **previous bit** and the **current bit** are the **same**, implying the bit has **not changed** in this message.
   - If the QR bit is **1**, **previous bit** and the **current bit** are **different** (e.g., `01` or `10`), , implying the bit has **changed**, and the **next bit must be toggled** while writing message.

# Parameters
We don't have any limit on any parameters, since we only have destination and source ip adresses of sender and receiver, and the log file name.

# Capacity of the Link
Our bandwith is 10.112013655291877 bits/seconds for a message length given in the homework pdf (128 bits). 


