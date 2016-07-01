def count():
    fs = []
    for i in range(1,4):
        def f(i=i):#用i=i绑定循环变量的传值
            return i*i
        fs.append(f)
    return fs