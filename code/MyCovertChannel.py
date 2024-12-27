import time
from CovertChannelBase import send, CovertChannelBase
from scapy.all import IP, UDP, DNS, DNSQR, sniff

class MyCovertChannel(CovertChannelBase):
    """
    - You are not allowed to change the file name and class name.
    - You can edit the class in any way you want (e.g., adding helper functions); however, there must be a "send" and a "receive" function, 
    the covert channel will be triggered by calling these functions.
    """
 

    def init(self):
        super().__init__()
        

    def send(self, log_file_name, destination_ip, source_ip):
        
        """
        - In this function, you are expected to create a random message (using function/s in CovertChannelBase) and send it to the receiver container. 
        - This implementation sends the length of the message first and then the actual message, bit by bit.
        """
        binary_message = self.generate_random_binary_message_with_logging(log_file_name, 2, 2)
        counter = True
        #make the class variable start to be able to calculate the time
        for i,current_bit in enumerate(binary_message):
            if counter:  
                if current_bit == '1':
                    qr_flag = 1
                else:
                    qr_flag = 0
                counter = False
                prev = current_bit
            else:
                if current_bit == prev:
                    qr_flag = 0
                else:
                    qr_flag = 1
                    prev = current_bit
            packet = IP(src = source_ip, dst=destination_ip, id = i) / UDP(dport=53) / DNS(qr=qr_flag, qd=DNSQR(qname="google.com"))
            print("Sending: " + str(qr_flag)) 
            send(packet)

    def receive(self, log_file_name, parameter1, parameter2):
        received_message = ''
        received_bits = []
        stop_bit_pattern1 = '00111001'
        stop_bit_pattern2 = '10111001'

        def stop_filter(packet):
            if packet.haslayer(DNS):
                # "." ascii code is 46 and 46 in binary is 00101110 
                qr_bit = str(packet[DNS].qr)
                received_bits.append(qr_bit)
                if len(received_bits) >= 8 and len(received_bits)%8 == 0 and (''.join(received_bits[-8:]) == stop_bit_pattern1 or ''.join(received_bits[-8:]) == stop_bit_pattern2):
                        return True
            return False
    
        message = sniff(filter="udp port 53", stop_filter=stop_filter)

        counter = True
        prev = ''

        for current_packet in message:
            if current_packet.haslayer(DNS):
                if counter:
                    counter = False
                    prev = str(current_packet[DNS].qr)
                    received_message += prev
                else:
                    if current_packet[DNS].qr == 0:
                        received_message += prev
                    else:
                        received_message += str(1 - int(prev))
                        prev = str(1 - int(prev))
        
        received_message = ''.join([self.convert_eight_bits_to_character(received_message[i:i+8]) for i in range(0, len(received_message), 8)])
        self.log_message(received_message, log_file_name)


        print("Received message: " + received_message)

        