from kansup import KantinAde, SotoLamongan, HajiBebek, KantinIndomie

foodade1 = KantinAde("Ayam Goreng", 10000)
foodade2 = KantinAde("Nasi Putih", 2000)
foodade3 = KantinAde("Tahu Goreng", 2000)
foodade4 = KantinAde("Tempe Goreng", 2000)

foodlamongan1 = SotoLamongan("Soto Betawi", 10000)
foodlamongan2 = SotoLamongan("Nasi Putih", 2000)
foodlamongan3 = SotoLamongan("Indomie Goreng", 5000)
foodlamongan4 = SotoLamongan("Perkedel", 3000)

foodhaji1 = HajiBebek("Bebek Goreng", 12000)
foodhaji2 = HajiBebek("Tempe Orek", 3000)
foodhaji3 = HajiBebek("Tahu Goreng", 2000)
foodhaji4 = HajiBebek("Nasi Putih", 2000)

foodindomie1 = KantinIndomie("Indomie Goreng", 5000)
foodindomie2 = KantinIndomie("Indomie Kuah", 5000)
foodindomie3 = KantinIndomie("Nutrisari", 2000)
foodindomie4 = KantinIndomie("Kopi", 3000)

print("Kansup Last Order Simulation")

c1 = []
c2 = []
c3 = []
c4 = []
all1 = []
all2 = []
all3 = []
all4 = []
title = input("Do You Want To Eat At Kansup ?")

if title == "yes":
        print("Warung Available:")
        print("1.Kantin Ade  2.Soto Lamongan  3.Haji Bebek  4.Kantin Indomie  5.Exit")

        try:
            x = int(input("Where Do You Want To Eat ?"))
            while True:
                if x == 1:
                    print("1.Ayam Goreng  2.Nasi Putih  3.Tahu Goreng  4.Tempe Goreng  5.Nevermind")
                    y = input("What Do You Want To Eat?")

                    if y == "1":
                        foodade1.print_info_ade()
                        food1 = 10000
                        c1.append(food1)
                        all1.append("Ayam Goreng")

                    if y == "2":
                        foodade2.print_info_ade()
                        food2 = 2000
                        c1.append(food2)
                        all1.append("Nasi Putih")

                    if y == "3":
                        foodade3.print_info_ade()
                        food3 = 2000
                        c1.append(food3)
                        all1.append("Tahu Goreng")

                    if y == "4":
                        foodade4.print_info_ade()
                        food4 = 2000
                        c1.append(food4)
                        all1.append("Tempe Goreng")

                    else:
                        print("")

                    z = input("Is There Anything Else ?")
                    if z == "yes":
                        continue

                    if z == "no":
                        t = sum(c1)
                        print("Total Food =", all1)
                        print("Total Price :", "Rp.", t)
                        print("Enjoy Your Meal....")
                        break


                    else:
                        print("Please Type In Only 'yes' or 'no'")


                if x == 2:
                    print("1.Soto Betawi  2.Nasi Putih  3.Indomie Goreng  4.Perkedel  5.Nevermind")
                    y = input("What Do You Want To Eat?")

                    if y == "1":
                        foodlamongan1.print_info_lamongan()
                        food1 = 10000
                        c2.append(food1)
                        all2.append("Soto Betawi")

                    if y == "2":
                        foodlamongan2.print_info_lamongan()
                        food2 = 2000
                        c2.append(food2)
                        all2.append("Nasi Putih")

                    if y == "3":
                        foodlamongan3.print_info_lamongan()
                        food3 = 5000
                        c2.append(food3)
                        all2.append("Tempe Goreng")

                    if y == "4":
                        foodlamongan4.print_info_lamongan()
                        food4 = 3000
                        c2.append(food4)
                        all2.append("Perkedel")

                    else:
                        print("")

                    z = input("Is There Anything Else ?")
                    if z == "yes":
                        continue

                    if z == "no":
                        t = sum(c2)
                        print("Total Food", all2)
                        print("Total Price :", "Rp.", t)
                        print("Enjoy Your Meal....")
                        break


                    else:
                        print("Please Type In Only 'yes' or 'no'")

                if x == 3:
                    print("1.Bebek Goreng  2.Tempe Orek  3.Tahu Goreng  4.Nasi Putih  5.Nevermind")
                    y = input("What Do You Want To Eat?")

                    if y == "1":
                        foodhaji1.print_info_haji()
                        food1 = 12000
                        c3.append(food1)
                        all3.append("Bebek Goreng")

                    if y == "2":
                        foodhaji2.print_info_haji()
                        food2 = 3000
                        c3.append(food2)
                        all3.append("Tempe Orek")

                    if y == "3":
                        foodhaji3.print_info_haji()
                        food3 = 2000
                        c3.append(food3)
                        all3.append("Tahu Goreng")

                    if y == "4":
                        foodhaji4.print_info_haji()
                        food4 = 3000
                        c3.append(food4)
                        all3.append("Nasi Putih")

                    else:
                        print("")

                    z = input("Is There Anything Else ?")
                    if z == "yes":
                        continue

                    if z == "no":
                        t = sum(c3)
                        print("Total Food =", all3)
                        print("Total Price :", "Rp.", t)
                        print("Enjoy Your Meal....")
                        break


                    else:
                        print("Please Type In Only 'yes' or 'no'")

                if x == 4:
                    print("1.Indomie Goreng  2.Indomie Kuah  3.Nutrisari  4.Kopi  5.Nevermind")
                    y = input("What Do You Want To Eat?")

                    if y == "1":
                        foodindomie1.print_info_indomie()
                        food1 = 5000
                        c4.append(food1)
                        all4.append("Indomie Goreng")

                    if y == "2":
                        foodindomie2.print_info_indomie()
                        food2 = 5000
                        c4.append(food2)
                        all4.append("Indomie Kuah")

                    if y == "3":
                        foodindomie3.print_info_indomie()
                        food3 = 2000
                        c4.append(food3)
                        all4.append("Nutrisari")

                    if y == "4":
                        foodindomie4.print_info_indomie()
                        food4 = 3000
                        c4.append(food4)
                        all4.append("Kopi")

                    else:
                        print("")

                    z = input("Is There Anything Else ?")
                    if z == "yes":
                        continue

                    if z == "no":
                        t = sum(c4)
                        print("Total Food =", all4)
                        print("Total Price :", "Rp.", t)
                        print("Enjoy Your Meal....")
                        break


                    else:
                        print("Please Type In Only 'yes' or 'no'")


                else:
                    tot = (c1 + c2 + c3 + c4)
                    print(all1 + all2 + all3 + all4)
                    print("Total Food Price You Bought At Kansup =", tot)
                    break

        except:
            print("Please Input In Integers")


j = input("Is Kansup Last Order Simulation Good ?")

if j == "yes":
    print("Please Rate Us (1-10):")

elif j == "no":
    print("Please Rate Us (1-10):")

dict = {"1.Understandable": "1-10",
        "2.Realistic": "1-10",
        "3.Warung Options(skip if you don't know)": "1-10",
        "4.Food List(skip if you don't know)": "1-10"}
print(dict)

for i in dict:
    j = input()
    if (j == "1") or (j == "2") or (j == "3") or (j == "4") or (j == "5") or (j == "6") or (j == "7") or (
        j == "8") or (j == "9") or (j == '10'):
        a = (i + " " + "=" + " " + j)
        print(a)

    else:
        print("You Can't Rate More Than 10 Or Less Than 0.... Whatever...")

if title == "no":
    print("")

else:
    print("Please Type In Either 'yes'/'no' Or In Numericals Next Time ")
    print("")

print("Thank You And Have A Nice Day.....")