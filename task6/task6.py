ticket = input("введите номер билета из 6 символов:")
if len(ticket) == 6:
    if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[-1])+int(ticket[-2])+int(ticket[-3]):
        print(f" {ticket} ->  счастливый")
    else:
        print(f" {ticket} ->  не счастливый")
