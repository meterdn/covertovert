# Covert Storage Channel that exploits Protocol Field Manipulation using QR Flag field in DNS

we implemented a covert channel utilizing the DNS headers in packets. For this purpose, we used the QR flag fields in the DNS header which is only one bit long. To enhance security and encryption, we encoded the message using its transition state in each bit. The encoding works as follows:
The very first bit of the message is directly put into the DNS QR bit of the first packet. Bits after that are updated according to the previous bit of the message such that:
If the previous bit and the current bit are the same, we send 0 in the QR bit implying the bit has not changed in this message.
If the previous bit and the current bit are different (for ex:01 or 10), we send 1 in the QR bit implying the bit has changed and so the next bit must be toggled.

This convention is implemented in both sender and the receiver to ensure they both encode and decode in the same manner.
