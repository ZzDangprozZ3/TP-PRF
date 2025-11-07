import sys,os
from ns import ns
from log_process_plot import *
from log_tracer import *

def experiment(buffer_size, bandwith , delay, app_data_rate, app_packet_size, app_start_time, app_duration_time, pcap_file, aggreg_res_file): 
     
    nodes= ns.NodeContainer()
    nodes.Create(2)
    pointToPoint = ns.PointToPointHelper() 
    pointToPoint.SetQueue("ns3::DropTailQueue<Packet>", "MaxSize", ns.StringValue(str(buffer_size)+"p")) 
    pointToPoint.SetDeviceAttribute("DataRate", ns.StringValue(str( bandwith)+"Kbps")) 
    pointToPoint.SetChannelAttribute("Delay", ns.StringValue(str( delay)+"ms"))

    devices = pointToPoint.Install(nodes)

    stack = ns.InternetStackHelper() 
    stack.Install(nodes) 
    address = ns.Ipv4AddressHelper() 
    address.SetBase("192.168.1.0", "255.255.255.0") 
    IPv4interfaces = address.Assign(devices)

    traffic_control_helper = ns.TrafficControlHelper() 
    traffic_control_helper.Uninstall(devices)

    server_ip = IPv4interfaces.GetAddress(1) 
    udpServer = ns.PacketSinkHelper("ns3::UdpSocketFactory", ns.InetSocketAddress(server_ip, 9).ConvertTo()) 
    serverApps = udpServer.Install(nodes.Get(1)) 
    serverApps.Start(ns.Seconds(0)) 
    serverApps.Stop(ns.Seconds(200))

    client_ip = IPv4interfaces.GetAddress(0) 
    clientApps = [] 
    echoClient = [] 
    for i in range(len(app_data_rate)): 
        echoClient.append(ns.OnOffHelper("ns3:: UdpSocketFactory", ns.InetSocketAddress(server_ip, 9).ConvertTo())) 
        echoClient[i].SetAttribute("Local", ns.AddressValue(ns.InetSocketAddress(client_ip, 2025 + i).ConvertTo())) 
        echoClient[i].SetAttribute("OnTime", ns.StringValue("ns3:: ConstantRandomVariable[Constant=1]")) 
        echoClient[i].SetAttribute("OffTime", ns.StringValue("ns3:: ConstantRandomVariable[Constant=0]")) 
        echoClient[i].SetAttribute("DataRate", ns.StringValue(str( app_data_rate[i]) + "kbps")) 
        echoClient[i].SetAttribute("PacketSize", ns.UintegerValue( app_packet_size[i]))
        clientApps.append(echoClient[i].Install(nodes.Get(0))) 
        clientApps[i].Start(ns.Seconds(app_start_time[i])) 
        clientApps[i].Stop(ns.Seconds(app_start_time[i] + app_duration_time[i]))

    ns.PacketMetadata.Enable()
    pointToPoint.EnablePcap(pcap_file, devices.Get(0), True)
    ns.Simulator.Stop(ns.Seconds(200)) 
    ns.Simulator.Run() 
    ns.Simulator.Destroy()
	# A compléter en TP2
    return
	
def main(argv):
    BufSize=100
    Bandwidh=10000
    Delay= 10 

    DataRates=[5000]
    PktSizes=[970]
    AppStartTime=[1]
    AppDurationTime=[15]

    direct_results = 'results_udp_p2p'
    if not os.path.exists(direct_results):
        os.makedirs(direct_results)
    SumFileName="./"+direct_results+"/aggregatd_results.txt"
    open(SumFileName, 'w')

    app_data_rate_str = '_'.join(map(str, DataRates))
    all_data_file = f"./{direct_results}/K_{BufSize}_mu_{Bandwidh}_lambda_{app_data_rate_str}_D_{Delay}"

    Init_pkt_tracer_functions()
    sys.stdout = open(all_data_file+".txt", 'w')
    experiment (BufSize,Bandwidh,Delay,DataRates, PktSizes,AppStartTime,AppDurationTime, all_data_file, SumFileName)
    sys.stdout.close()
    sys.stdout = sys.__stdout__

    #process_and_plot_metrics(all_data_file+".txt", 0.1)

if __name__ == '__main__':
    sys.exit (main (sys.argv))
    