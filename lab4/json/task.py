import json as js


with open(r"C:\Users\bajge\OneDrive\PP2\lab4\json\s-d.json", 'r') as file:
    data = js.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<30} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)


interface = data['imdata']

for i in interface:
    dn = i.get("dn", "none")  # Получаем "dn", если нет — "none"
    description = i.get("description", "N/A")
    speed = i.get("speed", "N/A")
    mtu = i.get("mtu", "N/A")
    
    print(f"{dn:<30} {description:<20} {speed:<7} {mtu:<5}")
