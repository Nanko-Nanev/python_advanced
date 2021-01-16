n = int(input())
guest_list = set([])
vip_guests = set([])
guest_that_did_not_show = set([])

for _ in range(n):
    guest_list.add(input())

command = input()

while not command == "END":
    guest_list.remove(command)
    command = input()

print(len(guest_list))

for guest in guest_list:
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        guest_that_did_not_show.add(guest)

vip_guests = sorted(vip_guests)
guest_that_did_not_show = sorted(guest_that_did_not_show)

for vip in vip_guests:
    print(vip)
for guest in guest_that_did_not_show:
    print(guest)