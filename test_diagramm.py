from main import Diagramm

diagram = Diagramm()





if __name__ == "__main__":
    diagram.x_time = 10
    diagram.x_time = 30
    diagram.x_time = 50
    assert diagram.x_time[0] == 10
    print("test 1 pass [+]")
    assert diagram.x_time[1] == 30
    print("test 2 pass [+]")
    assert diagram.x_time[2] == 50
    print("test 3 pass [+]")