while True:
    player = str(input("ถามธาตุอะไร - ")).lower()

    types = {
        "Normal": "ปกติ",
        "Fire": "ไฟ",
        "Water": "น้ำ",
        "Electric": "ไฟฟ้า",
        "Grass": "พืช",
        "Ice": "น้ำแข็ง",
        "Fighting": "ต่อสู้",
        "Poison": "พิษ",
        "Ground": "ดิน",
        "Flying": "บิน",
        "Psychic": "พลังจิต",
        "Bug": "แมลง",
        "Rock": "หิน",
        "Ghost": "ผี",
        "Dragon": "มังกร",
        "Dark": "มืด",
        "Steel": "เหล็ก",
        "Fairy": "แฟรี่",
    }

    if player == "normal":
        print(f"ชนะ : ไม่มี")
        print(f"แพ้ : {types['Fighting']}")
        print(f"ปล.'ผี' ตีไม่เข้า และตี 'ผี' ไม่ได้")
    elif player == "fire":
        print(f"ชนะ : {types['Grass']} {types['Ice']} {types['Bug']} {types['Steel']}")
        print(f"แพ้ : {types['Water']} {types['Ground']} {types['Rock']}")
    elif player == "water":
        print(f"ชนะ : {types['Fire']} {types['Ground']} {types['Rock']}")
        print(f"แพ้ : {types['Electric']} {types['Grass']}")
    elif player == "electric":
        print(f"ชนะ : {types['Water']} {types['Flying']}")
        print(f"แพ้ : {types['Ground']}")
        print("ปล.ตีดินไม่ได้")
    elif player == "grass":
        print(f"ชนะ : {types['Water']} {types['Ground']} {types['Rock']}")
        print(f"แพ้ : {types['Fire']} {types['Ice']} {types['Poison']} {types['Flying']} {types['Bug']}")
    elif player == "ice":
        print(f"ชนะ : {types['Grass']} {types['Ground']} {types['Flying']} {types['Dragon']}")
        print(f"แพ้ : {types['Fire']} {types['Fighting']} {types['Rock']} {types['Steel']}")
    elif player == "fighting":
        print(f"ชนะ : {types['Normal']} {types['Ice']} {types['Rock']} {types['Dark']} {types['Steel']}")
        print(f"แพ้ : {types['Flying']} {types['Psychic']} {types['Fairy']}")
    elif player == "poison":
        print(f"ชนะ : {types['Grass']} {types['Fairy']}")
        print(f"แพ้ : {types['Ground']} {types['Psychic']}")
    elif player == "bug":
        print(f"ชนะ : {types['Grass']} {types['Psychic']} {types['Dark']}")
        print(f"แพ้ : {types['Fire']} {types['Flying']} {types['Rock']}")
    elif player == "rock":
        print(f"ชนะ : {types['Fire']} {types['Ice']} {types['Flying']} {types['Bug']}")
        print(f"แพ้ : {types['Water']} {types['Grass']} {types['Fighting']} {types['Ground']} {types['Steel']}")
    elif player == "ghost":
        print(f"ชนะ : {types['Psychic']} {types['Ghost']}")
        print(f"แพ้ : {types['Ghost']} {types['Dark']}")
    elif player == "dragon":
        print(f"ชนะ : {types['Dragon']} (จริงๆเกือบทุกธาตุ)")
        print(f"แพ้ : {types['Ice']} {types['Dragon']} {types['Fairy']}")
        print("ปล.ตีแฟรี่ไม่เข้า")
    elif player == "dark":
        print(f"ชนะ : {types['Psychic']} {types['Ghost']}")
        print(f"แพ้ : {types['Fighting']} {types['Bug']} {types['Fairy']}")
    elif player == "steel":
        print(f"ชนะ : {types['Ice']} {types['Rock']} {types['Fairy']}")
        print(f"แพ้ : {types['Fire']} {types['Fighting']} {types['Ground']}")
        print("ปล.กันได้เกือบทุกธาตุ")
    elif player == "fairy":
        print(f"ชนะ : {types['Fighting']} {types['Dragon']} {types['Dark']}")
        print(f"แพ้ : {types['Poison']} {types['Steel']}")
    elif player == "psychic":
        print(f"ชนะ : {types['Fighting']} {types['Poison']}")
        print(f"แพ้ : {types['Bug']} {types['Ghost']} {types['Dark']}")
    elif player == "ground":
        print(f"ชนะ : {types['Fire']} {types['Electric']} {types['Poison']} {types['Rock']} {types['Steel']}")
        print(f"แพ้ : {types['Water']} {types['Grass']} {types['Ice']}")
    elif player == "flying":
        print(f"ชนะ : {types['Grass']} {types['Fighting']} {types['Bug']}")
        print(f"แพ้ : {types['Electric']} {types['Ice']} {types['Rock']}")
    elif player == "out":
        break
    else:
        print("ธาตุนี้ไม่มีนะ")
    print("ถ้าจะออกให้พิมพ์ 'Out'")