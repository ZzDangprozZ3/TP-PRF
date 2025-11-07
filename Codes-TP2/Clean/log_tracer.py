from ns import ns

def App_tx_packet_tracer(packet: ns.Packet, src_address: ns.Address, dst_address: ns.Address) -> None:
    # Convertir les adresses pour obtenir IP et port
    src_ip = ns.network.InetSocketAddress.ConvertFrom(src_address).GetIpv4()
    src_port = ns.network.InetSocketAddress.ConvertFrom(src_address).GetPort()
    dst_ip = ns.network.InetSocketAddress.ConvertFrom(dst_address).GetIpv4()
    dst_port = ns.network.InetSocketAddress.ConvertFrom(dst_address).GetPort()
    
    # Création de l'entrée de log avec adresses IP et ports
    log_entry = (f"AppTx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)

      
def App_rx_packet_tracer(packet: ns.Packet, src_address: ns.Address, dst_address: ns.Address) -> None:
   # Convertir les adresses pour obtenir IP et port
    src_ip = ns.network.InetSocketAddress.ConvertFrom(src_address).GetIpv4()
    src_port = ns.network.InetSocketAddress.ConvertFrom(src_address).GetPort()
    dst_ip = ns.network.InetSocketAddress.ConvertFrom(dst_address).GetIpv4()
    dst_port = ns.network.InetSocketAddress.ConvertFrom(dst_address).GetPort()
    
    # Création de l'entrée de log avec adresses IP et ports
    log_entry = (f"AppRx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)

def Enqueue_packet_tracer(packet: ns.Packet) -> None:
    packet_copy = packet.Copy()
	#print(packet_copy.ToString())
    
    # Attention à retirer les entete PPP
    ppp_header = ns.network.PppHeader()
    packet_copy.RemoveHeader(ppp_header)
    ipv4_header = ns.network.Ipv4Header()
    src_ip = dst_ip = "N/A"
    if packet_copy.RemoveHeader(ipv4_header):     
        src_ip = ipv4_header.GetSource()
        dst_ip = ipv4_header.GetDestination()

    udp_header = ns.network.UdpHeader()  # Pour UDP; changez pour TcpHeader si nécessaire
    src_port = dst_port = "N/A"
    if packet_copy.RemoveHeader(udp_header):
        src_port = udp_header.GetSourcePort()
        dst_port = udp_header.GetDestinationPort()
    
    # Création de l'entrée de log avec les informations disponibles
    log_entry = (f"EnqTx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)

      
def Dequeue_packet_tracer(packet: ns.Packet) -> None:
    packet_copy = packet.Copy()
	#print(packet_copy.ToString())
    
    # Attention à retirer les entete PPP
    ppp_header = ns.network.PppHeader()
    packet_copy.RemoveHeader(ppp_header)
    ipv4_header = ns.network.Ipv4Header()
    src_ip = dst_ip = "N/A"
    if packet_copy.RemoveHeader(ipv4_header):     
        src_ip = ipv4_header.GetSource()
        dst_ip = ipv4_header.GetDestination()

    udp_header = ns.network.UdpHeader()  # Pour UDP; changez pour TcpHeader si nécessaire
    src_port = dst_port = "N/A"
    if packet_copy.RemoveHeader(udp_header):
        src_port = udp_header.GetSourcePort()
        dst_port = udp_header.GetDestinationPort()
    
    # Création de l'entrée de log avec les informations disponibles
    log_entry = (f"DeqTx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)


def Phy_tx_packet_tracer(packet: ns.Packet) -> None:
    packet_copy = packet.Copy()
	#print(packet_copy.ToString())
    
     # Attention à retirer les entete PPP
    ppp_header = ns.network.PppHeader()
    packet_copy.RemoveHeader(ppp_header)
    ipv4_header = ns.network.Ipv4Header()
    src_ip = dst_ip = "N/A"
    if packet_copy.RemoveHeader(ipv4_header):     
        src_ip = ipv4_header.GetSource()
        dst_ip = ipv4_header.GetDestination()

    udp_header = ns.network.UdpHeader()  # Pour UDP; changez pour TcpHeader si nécessaire
    src_port = dst_port = "N/A"
    if packet_copy.RemoveHeader(udp_header):
        src_port = udp_header.GetSourcePort()
        dst_port = udp_header.GetDestinationPort()
    
    # Création de l'entrée de log avec les informations disponibles
    log_entry = (f"PhyTx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)


def Phy_rx_packet_tracer(packet: ns.Packet) -> None:
    packet_copy = packet.Copy()
	#print(packet_copy.ToString())
    
    # Attention à retirer les entete PPP
    ppp_header = ns.network.PppHeader()
    packet_copy.RemoveHeader(ppp_header)
    ipv4_header = ns.network.Ipv4Header()
    src_ip = dst_ip = "N/A"
    if packet_copy.RemoveHeader(ipv4_header):     
        src_ip = ipv4_header.GetSource()
        dst_ip = ipv4_header.GetDestination()

    udp_header = ns.network.UdpHeader()  # Pour UDP; changez pour TcpHeader si nécessaire
    src_port = dst_port = "N/A"
    if packet_copy.RemoveHeader(udp_header):
        src_port = udp_header.GetSourcePort()
        dst_port = udp_header.GetDestinationPort()
    
    # Création de l'entrée de log avec les informations disponibles
    log_entry = (f"PhyRx \t {ns.Simulator.Now().GetSeconds():.5f} \t"
                 f" {src_ip}:{src_port} --> {dst_ip}:{dst_port} \t"
                 f" {packet.GetSize()} \t {packet.GetUid()}")
    print(log_entry)

def Init_pkt_tracer_functions(): # for tp2 and tp3

    ns.cppyy.cppdef("""
        using namespace ns3;
        Callback<void, Ptr<const Packet>> make_Phy_packet_callback(void(*func)(Ptr<const Packet>))
        {
            return MakeCallback(func);
        }
    """)

    ns.cppyy.cppdef("""
            using namespace ns3;
        Callback<void, Ptr<const Packet>, const Address &, const Address &> make_upper_packet_callback(void(*func)(Ptr<const Packet>, const Address &, const Address &))
        {
        return MakeCallback(func);
        }
        """)
    
    
def Init_cwnd_tracer_functions(): # for tp3
    ns.cppyy.cppdef("""
    #include "CPyCppyy/API.h"
    #include <fstream>
	#include <ns3/simulator.h>
 
    using namespace ns3;
 
	void CwndChange2(std::string filename, std::string tag, uint32_t oldCwnd, uint32_t newCwnd) {
    // Ouvre le fichier en mode ajout (append)
    std::ofstream wnd_file(filename, std::ios_base::app);
    if (wnd_file.is_open()) {
        // Écrit le temps actuel de la simulation et la nouvelle valeur de la fenêtre de congestion
        wnd_file << ns3::Simulator::Now().GetSeconds() << tag << newCwnd << std::endl;
        wnd_file.close();
    } else {
        std::cerr << "Erreur lors de l'ouverture du fichier windows_trace.txt" << std::endl;
    }
	}
                
    void CwndFunction(Ptr<Application> model, std::string filename, std::string tag ){
    Ptr<Socket> socket = DynamicCast<OnOffApplication>(model)-> GetSocket();    
    socket->TraceConnectWithoutContext("CongestionWindow",MakeBoundCallback (&CwndChange2, filename,tag));
                
    }
 
    EventImpl* CwndFunctionEvent(Ptr<Application> model, std::string filename, std::string tag)
    {
        return MakeEvent(&CwndFunction, model, filename,tag);
    }
 
   """)