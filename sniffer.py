from scapy.all import sniff 
def packet_callback(packet):
   print("/n---Packet-captured ---")

   if packet.haslayer("IP"):
      print("Source IP:", packet["IP"].src)
      print("Desination IP:" , packet["IP"].dst)
   print("Protocol:", packet.summary())

   if packet.haslayer("Raw"):
      print("Payload:")
      print(packet["Raw"].load)
sniff (prn=packet_callback, count=10)

