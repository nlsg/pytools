#!/usr/bin/python
import pyautogui as auto

def init():
    auto.failsafe = False

def change_win(win):
    auto.moveto(0,0)
    if (win <= 2):
        auto.moveto(18,300*win)
    elif (win <= 4):
        auto.moveto(900,300*(win-2))

def copy_to_clip(to_clip):
    import pyperclip as clip
    clip.copy(to_clip)
    # var = clip.paste()

def auto_paste_var(var, **kwargs):
    copy_to_clip(var)
    if "click" in kwargs:
        auto.click(kwargs["click"])
    auto.hotkey("ctrl","a")
    auto.hotkey("ctrl","v")

def read_part_file(part_file):
    item_num = {}
    item_amount = {}
    with open(part_file) as f:
        lines = f.readlines()
        it, it_ = 0, 0
        for ln in lines:
            if not (it % 2 ):
                item_num[it_] = ln[:-1]
            else:
                item_amount[it_] = ln[:-1]
                it_ += 1
            it += 1
    return item_num, item_amount

def get_args():
    import sys
    part_file = ""
    w_num = 0
    try:
        for i in range(1,len(sys.argv)):
            if (sys.argv[i] == "-p"):
                part_file = sys.argv[i+1]
            elif (sys.argv[i] == "-w"):
                w_num = int(sys.argv[i+1])
    except ValueError:
        if w_num == 0:
            while True:
                try:
                    w_num = int(input("input w-number: "))
                    break
                except ValueError:
                    print("must be a number, 'w' must not be contained")
                    continue
        if part_file == "":
            while True:
                part_file = input("path to a file with part info: ")
                if " " in part_file:
                    print("file path can not contain a space ' '")
                    continue
                if ".txt" in part_file:
                    break
                print("file must have a \".txt\" extantion")

    if w_num != 0 and part_file != "":
        return w_num, part_file

def main():
    ITEM_NUM_FIELD = (1239,596)
    COMMIT_FIELD = (1670,595) 
    w_num , part_file = get_args()
    item_num, item_amount = read_part_file(part_file)

    for i in range(0,len(item_num)):#iterate thru parts
        auto_paste_var(item_num[i],click = ITEM_NUM_FIELD)

        auto_paste_var(item_amount[i])

        print(f"in iterration item {item_num[i]} [{item_amount[i]}]")

        for i_ in range(0,5):
            auto.hotkey("tab") 
        auto.press("enter")
        auto.click(*COMMIT_FIELD)
        if i != len(item_num)-1:
            input()

if __name__ == "__main__":
    init()
    main()
