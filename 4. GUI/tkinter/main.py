import tkinter

# args, kwargs
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# tkinter
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label 생성
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# 컴포넌트 배치
my_label.pack()
my_label["text"] = "New Text"


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# my_label.pach(side="left")

input = tkinter.Entry(width=10)
input.pack()


# 마지막에 가 있어야 한다. 해당 코드가 없으면 창이 뜨지 않는다.
window.mainloop()
