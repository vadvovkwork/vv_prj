def work_files():
    f=open("test.txt", "w+")

    integers = [2, 5, 9, 20, 27]
    integers[1] = 10
    print(integers)



    v1= range(10,15)




    vvlist=[v1]
    print(v1)
    v2 = range(20, 55)
    list=[[x, v2[y]] for x, y in enumerate(v1)]
    print(list)



work_files()