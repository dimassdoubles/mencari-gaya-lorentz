from prettytable import PrettyTable


# Start Point ----------------------------------------------------
v_list = []
b_list = []
# list = [{"val": 10, "dir": "i"}]
# val = value
# dir = direction
double_v = False
double_b = False
valid = True
f_direction = ""


# Input Mechanism ------------------------------------------------
def make_dict(x: int, y: str):
    return {"val": x, "dir": y}


def velocity(V: str):
    V = V.split()
    if len(V) > 1:
        global double_v
        double_v = True
        for v in V:
            value = int(v[:-1])
            direction = v[-1]
            v_dict = make_dict(value, direction)
            v_list.append(v_dict)

    else:
        value = int(V[0][:-1])
        direction = V[0][-1]
        v_dict = make_dict(value, direction)
        v_list.append(v_dict)


def medan_magnet(B: str):
    B = B.split()
    if len(B) > 1:
        global double_b
        double_b = True
        for b in B:
            value = int(b[:-1])
            direction = b[-1]
            b_dict = make_dict(value, direction)
            b_list.append(b_dict)
    else:
        value = int(B[0][:-1])
        direction = B[0][-1]
        b_dict = make_dict(value, direction)
        b_list.append(b_dict)


# Output Mechanism -----------------------------------------------
def make_table():
    table_element = {
        "i": "F",
        "j": "F",
        "k": "F",
    }
    different_direction = v_list[0]["dir"] != b_list[0]["dir"]
    global valid
    if different_direction:
        valid = True
        # velocity
        table_element[v_list[0]["dir"]] = f"v = {v_list[0]['val']} m/s"
        # medan magnet
        table_element[b_list[0]["dir"]] = f"B = {b_list[0]['val']} T"
        # find f_direction
        for (key, value) in table_element.items():
            if value == "F":
                global f_direction
                f_direction = key
        # print(table)
        directions_table = PrettyTable()
        for (key, value) in table_element.items():
            directions_table.add_column(key, [value])
        print(directions_table)

    else:
        valid = False
    

# Reset Mechanism ----------------------------------------------
def reset():
    global v_list, b_list, double_v, double_b, valid, f_direction

    v_list = []
    b_list = []
    double_v = False
    double_b = False
    valid = True
    f_direction = ""


def find_answer(q: int, V: list, B: list):
    print("\nPenyelesaian: ")
    global valid

    def find_f(x="unknown"):
        # x = diisi v/B
        if valid:
            v = V[0]["val"]
            b = B[0]["val"]
            F = q * v * b
            print("F = q x v x B")
            print(f"F = {q} x {v} x {b}")
            print(f"F = {F} N ({f_direction})")
        else:
            if x == "v":
                print(f"Nilai v = {V[0]['val']} m/s tidak valid")
            if x == "B":
                print(f"Nilai B = {B[0]['val']} T tidak valid")

    # akan ada 3 kemungkinan,
    # 1.double velocity
    if double_v:
        print("* f1")
        make_table()
        find_f("v")
        del v_list[0]
        print("\n* f2")
        make_table()
        find_f("v")
    # 2.double medan magnet
    elif double_b:
        print("* f1")
        make_table()
        find_f("B")
        del b_list[0]
        print("\n* f2")
        make_table()
        find_f("B")
    # 3.tidak ada yang double
    else:
        make_table()
        find_f()


# Main Program ---------------------------------------------------
def main():
    # diketahui
    print("Diketahui")
    q = int(input("q = "))
    v = input("v = ")
    B = input("B = ")

    # ditanya
    print("\nDitanya\nF = .... ?")

    # dijawab
    velocity(v)
    medan_magnet(B)
    find_answer(q, v_list, b_list)
    reset()
    print("=====================================================\n")

    # looping
    main()


if __name__ == "__main__":
    main()
