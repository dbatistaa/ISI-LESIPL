import random
from datetime import datetime, timedelta

ips_maliciosos = ["185.220.101.5", "45.33.32.156", "103.203.57.10", "194.26.29.112", "91.240.118.243"]
ips_legitimos = ["193.136.12.45", "85.240.10.12"]

utilizadores_invalidos = ["admin", "root", "guest", "test", "oracle", "support", "ubuntu"]
utilizadores_validos = ["tiago", "backup_user", "deploy"]

base_time = datetime.now() - timedelta(hours=6)

with open("data/auth.log", "w") as f:
    for i in range(250):
        current_time = base_time + timedelta(seconds=i * 60)
        timestamp = current_time.strftime("%b %d %H:%M:%S")
        
        # 80% ataques/falhas, 20% logins legitimos
        if random.random() < 0.8:
            ip = random.choice(ips_maliciosos)
            user = random.choice(utilizadores_invalidos)
            port = random.randint(35000, 65000)
            f.write(f"{timestamp} srv-core-01 sshd[{random.randint(1000, 9999)}]: Failed password for invalid user {user} from {ip} port {port} ssh2\n")
        else:
            ip = random.choice(ips_legitimos)
            user = random.choice(utilizadores_validos)
            port = random.randint(35000, 65000)
            f.write(f"{timestamp} srv-core-01 sshd[{random.randint(1000, 9999)}]: Accepted password for {user} from {ip} port {port} ssh2\n")

print("Ficheiro data/auth.log criado com sucesso!")
