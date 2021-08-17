#!/usr/bin/python3

nat = "ip nat inside source interface GigabitEthernet0/1 overload"

new_nat = nat.replace("GigabitEthernet", "FastEthernet")
print(new_nat)
