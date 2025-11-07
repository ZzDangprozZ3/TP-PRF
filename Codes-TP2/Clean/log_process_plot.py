
import matplotlib.pyplot as plt

# TP2 et TP3
def process_trace(tracefile, timestep):
    # Dictionnaire pour stocker les métriques
    metrics = {}  # metrics[time][flow][metric_index]
    Arrival_times = {} 
    # Lire le fichier de traces
    with open(tracefile, 'r') as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            
            # Traitement de la ligne
            event_type = parts[0]
            timestamp = float(parts[1])
            flow_id = parts[2] + parts[3] + parts[4]  # ID de flux sous forme de chaîne
            packet_size = int(parts[5]) * 8 
            packet_id = int(parts[6])
            
            # Calcul du laps de temps
            time_slot = int(timestamp // timestep)

            # Initialisation des métriques pour le laps de temps et le flux
            if time_slot not in metrics:
                metrics[time_slot] = {}
            if flow_id not in metrics[time_slot]:
                metrics[time_slot][flow_id] = {
                    'tx': 0,           # Nombre de paquets envoyés
                    'rx': 0,           # Nombre de paquets reçus
                    'bytes_tx': 0,     # Nombre d'octets envoyés
                    'bytes_rx': 0,     # Nombre d'octets reçus
                    'avg_delay': 0,    # Délai moyen
                    'delay_count': 0   # Compteur pour le délai
                }

            # Gestion des événements
            if event_type == "EnqTx":
                Arrival_times[packet_id] = timestamp 
            elif event_type == "PhyTx":   
                metrics[time_slot][flow_id]['tx'] += 1
                metrics[time_slot][flow_id]['bytes_tx'] += packet_size
            elif event_type == "PhyRx":
                metrics[time_slot][flow_id]['rx'] += 1
                metrics[time_slot][flow_id]['bytes_rx'] += packet_size
                if packet_id in Arrival_times:
                    delay = timestamp - Arrival_times[packet_id]
                    metrics[time_slot][flow_id]['avg_delay'] += delay
                    metrics[time_slot][flow_id]['delay_count'] += 1

    # Calculer le délai moyen
    for time_slot in metrics:
        for flow_id in metrics[time_slot]:
            if metrics[time_slot][flow_id]['delay_count'] > 0:
                metrics[time_slot][flow_id]['avg_delay'] /= metrics[time_slot][flow_id]['delay_count']
                metrics[time_slot][flow_id]['avg_delay'] /= timestep
            metrics[time_slot][flow_id]['tx'] /= timestep
            metrics[time_slot][flow_id]['rx'] /= timestep
            metrics[time_slot][flow_id]['bytes_rx'] /= timestep
            metrics[time_slot][flow_id]['bytes_tx'] /= timestep

    return metrics

def plot_metrics(metrics, timestep):
    # Ici je trace débit_tx, débit_rx, délai_moyen mais il prévu de généraliser la fonction pour plotter des métriques passées en parmètres
    flows = set()
    for time_slot in metrics:
        flows.update(metrics[time_slot].keys())

    flows = list(flows)  # Convertir en liste pour itération

    # Préparer les graphiques
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    
    for flow_id in flows:
        time_values = []
        bytes_tx_values = []
        bytes_rx_values = []
        avg_delay_values = []
        
        for time_slot in sorted(metrics.keys()):
            if flow_id in metrics[time_slot]:
                time_values.append(time_slot * timestep)
                bytes_tx_values.append(metrics[time_slot][flow_id]['bytes_tx'])
                bytes_rx_values.append(metrics[time_slot][flow_id]['bytes_rx'])
                avg_delay_values.append(metrics[time_slot][flow_id]['avg_delay'])
            else:
                time_values.append(time_slot * timestep)
                bytes_tx_values.append(0)
                bytes_rx_values.append(0)
                avg_delay_values.append(0)

        # Tracer chaque métrique
        axs[0].plot(time_values, bytes_tx_values, label=flow_id)
        axs[1].plot(time_values, bytes_rx_values, label=flow_id)
        axs[2].plot(time_values, avg_delay_values, label=flow_id)

    # Configurer les sous-graphes
    axs[0].set_title('Bytes Sent')
    axs[0].set_ylabel('Tx Throughput (bps)')
    axs[0].set_ylim(bottom=0)  # 
    axs[0].grid()
    
    axs[1].set_title('Throughput at Reception')
    axs[1].set_ylabel('Rx Throughput (bps)')
    axs[1].set_ylim(bottom=0)  # 
    axs[1].grid()

    axs[2].set_title('Average Delay')
    axs[2].set_ylabel('AveragenDelay (s)')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylim(bottom=0)  # 
    axs[2].grid()

    # Ajouter la légende
    for ax in axs:
        ax.legend()
    
    plt.tight_layout()
    plt.show()

def process_and_plot_metrics(trace_file,timestep):
    # A compléter
    return 

# TP3
def plot_windows_by_flow(filename):
    # Dictionnaire pour stocker les données par flux
    data_by_flow = {}

    # Lecture du fichier texte
    with open(filename, 'r') as file:
          # Stocker les données par flux
        for line in file:
            parts = line.strip().split()
            time = float(parts[0])
            flow = parts[1]
            windows_value = float(parts[2])

            # Initialiser les listes pour chaque flux s'il n'est pas encore dans le dictionnaire
            if flow not in data_by_flow:
                data_by_flow[flow] = {'time': [], 'windows_value': []}

            # Ajouter les valeurs pour chaque flux
            data_by_flow[flow]['time'].append(time)
            data_by_flow[flow]['windows_value'].append(windows_value)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    # Tracer chaque flux avec une couleur différente
    for flow, data in data_by_flow.items():
        plt.plot(data['time'], data['windows_value'], label=f'Flow {flow}')

    # Ajouter des titres et légendes
    plt.xlabel('Time')
    plt.ylabel('Windows Value')
    plt.title('Windows Value en fonction du Time pour chaque Flow')
    plt.legend()
    plt.grid(True)

    # Afficher le graphique
    plt.show()



