# Covert Storage Channel Exploiting Protocol Field Manipulation Using QR Flag in DNS

We implemented a covert channel utilizing the DNS headers in packets. For this purpose, we used the **QR flag field** in the DNS header, which is only one bit long. 

To enhance security and encryption, we encoded the message using its **transition state** in each bit. The encoding works as follows:

1. The very first bit of the message is directly placed into the DNS QR bit of the first packet.
2. Subsequent bits are updated based on the **previous bit** of the message, following these rules:
   - If the **previous bit** and the **current bit** are the **same**, we send **0** in the QR bit, implying the bit has **not changed** in this message.
   - If the **previous bit** and the **current bit** are **different** (e.g., `01` or `10`), we send **1** in the QR bit, implying the bit has **changed**, and the **next bit must be toggled**.



This convention is implemented in both the sender and the receiver to ensure that they encode and decode in the same manner.
