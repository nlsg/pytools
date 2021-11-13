#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests, re, sys
import nls_util as nut

'''Parser Class'''
class Parser():
    @nut.func_info
    def  __init__(self,domain, site = ""):
        self.res = {}
        self.url = ""
        self.load_doc(site, domain)
        self.search_links(".")

    @nut.func_info
    def load_doc(self, site, domain = "", url = ""):
        if domain != "":
            self.domain = ("https://" if domain[0:8] != "https://" else "")
            self.domain += domain + ("/" if (domain[-1] != "/") else "")
        self.url_ = self.url
        self.url = ((self.domain + site) if url == "" else url)
        try:
            self.req = requests.get(self.url)
        except requests.exceptions.ConnectionError as e:
            print(nut.cli["RED"] + f"[load_doc] > connection Error" + nut.cli["RESET"])
            return
        self.doc = BeautifulSoup(self.req.text, "html.parser")
        return self.url

    @nut.func_info
    def load_ref(self, index):
        try:
            self.load_doc(self.res[index][1])
        except KeyError as ke:
            print(nut.cli["RED"] + f"[load_ref] -> KeyError: {ke}" + nut.cli["RESET"])
        return self.url

    @nut.func_info
    def search_links(self, regex):
        it = 0
        self.res = {}
        for a in self.doc.find_all("a",href=re.compile(regex)):
            try:
                self.res[it] = [a, str(a["href"])]
            except TypeError:
                self.res[it] = [a]
            it += 1
        return it

    @nut.func_info
    def search_img(self, regex = "\.jpg"):
        it = 0
        self.res = {}
        for a in self.doc.find_all("img", src=re.compile(regex)):
            try:
                self.res[it] = [a, str(a["src"])]
            except TypeError:
                self.res[it] = [a]
            it += 1
        return it

    def count_links(self, regex = "."):
        buff = self.res
        it = self.search_links(regex)
        self.res = buff
        return it

    def print_res(self, log_f = ""):
        if log_f != "":
            for i in range(len(self.res)):
                try:
                    nut.tee(log_f, f"[{i}]\t-> {self.res[i][1]}")
                except IndexError:
                    nut.tee(log_f, f"[{i}]\t-> {self.res[i][0]}")
        else:
            for i in range(len(self.res)):
                try:
                    print(f"[{i}]\t-> {self.res[i][1]}")
                except IndexError:
                    print(f"[{i}]\t-> {self.res[i][0]}")

    def surf_page(self):
        options = "[surf_page]> [q]uit, [s]earch, [i]magesearch, [h]ome [0-9]goto reference, [v]iew"
        options = nut.cli["BLUE"] + options + nut.cli["RESET"]
        self.home()
        while True:
            ref = ("_" if (ref := input(f"{options}\n[{self.get_site()}]>")) == "" else ref)
            try:
                self.lrsp(int(ref))
            except ValueError:
                if ref[0] == "q":
                    return
                elif ref[0] == "s":
                    regex = ("." if (in_ := input("search term: ")) ==  "" else in_)
                    self.sp(regex)
                elif ref[0] == "i":
                    print("entered condition; skipped except...")
                    self.search_img()
                    self.dl_n_show_img(self.url)
                elif ref[0] == "h":
                    self.home()
                elif ref[0] == "v":
                    self.view("firefox")
                else:
                    print(f"{ref} not found!")

    def dl_n_show_img(self, url):
        from PIL import Image
        img_name = "soup.jpg"
        img_data = requests.get(url).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
        img = Image.open(img_name)
        img.show()

    def get_site(self):
        return self.url[len(bs.domain):]

    @nut.func_info
    def sp(self, regex = ".", log_f = ""):
        it = self.search_links(regex)
        self.print_res(log_f)
        return it
    @nut.func_info
    def lrsp(self, index, regex = ".", log_f = ""):
        self.load_ref(index)
        return self.sp(regex, log_f)
    @nut.func_info
    def ldsp(self,site, regex = ".", log_f = ""):
        self.load_doc(site)
        return self.sp(regex, log_f)

    def view(self, browser= "links"):
        import os
        os.system(f"{browser} {self.url}")

    def open_in_vim(self):
        import os
        with open("soup.txt", "w") as html:
            html.write(self.req.text)
        os.system("b vim soup.txt")

'''Parser Class'''
class BSParser(Parser):

    @nut.func_info
    def find_all_series(self):
        self.load_doc("andere-serien")
        return self.search_links("serie")

    def home(self):
        bs.ldsp("andere-serien")

    def p(self, *args, **kwargs):
        col = "CYAN"
        if "col" in kwargs:
            col = kwargs["col]"]
        p_head = nut.cli[col] + f"[tst - {self.get_site()}]> {self.url}\n >"
        print(p_head, *args, **kwargs)

    '''methods for testing'''
    @nut.func_info
    def tst_load_img(self, search = "Sponge"):
        with (tmr := nut.Timer(f"img search {search}")):
            self.home()
            self.sp(search)
            self.p("searched sponge")
            tmr.stamp("search sponge")
            self.lrsp(0)
            self.p("applied url")
            tmr.stamp("applied url")
            self.search_img()
            self.print_res()
            self.p("searched img")
            tmr.stamp("searched img")
            self.lrsp(0)
            self.p("applied url")
            tmr.stamp("applied url")
            self.dl_n_show_img(self.url)

    @nut.func_info
    def tst_load_raw(self, search = "Sponge"):
        with (tmr := nut.Timer(f"img search {search}")):
            self.home()
            self.sp(search)
            self.lrsp(0)
            self.search_img()
            self.print_res()
            self.lrsp(0)
            self.dl_n_show_img(self.url)

    @nut.func_info
    def tst_series(self, n_tests = 0):
        ret = {}
        rgx ={"FIND_SERIES_AMOUNT": r"[/]\d\D?[/][a-z][a-z]"}
        def p(*args, **kwargs):
            col = "CYAN"
            if "col" in kwargs:
                col = kwargs["col]"]
            p_head = nut.cli[col] + "[tst]> res size:{len(bs.res)}\n >"
            print(p_head, *args, **kwargs)

        ret["n_tot_res"] = self.find_all_series()
        search_res = self.res
        p(f"found_all_series() -> {ret['n_tot_res']}")
        for i in range(ret["n_tot_res"]):
            print()
            p(f"testing itr -> {i}")
            try:
                self.url_ = self.url
                self.url = self.domain + search_res[i][1]
            except KeyError:
                p(f"coudn't koad : '{self.url}''", col="RED")
                continue
            p(nut.cli["CYAN"] + f"[{i}] -> loading '{self.url}'...")
            self.load_doc(search_res[i][1])
            search = self.url[len(self.domain):]# + rgx["FIND_SERIES_AMOUNT"]
            p(f"[{i} - self.res[i][1]] -> searching for {search}..")
            n_res = self.sp(search, log_f = "soup.log")
            try:
                ret[self.res[i][1]] = self.res
            except:
                p(f"coud not store results")
            p(f"[{i} - self.res[i][1]] -> test done!")
            p(f"[{i} - self.res[i][1]] -> found: {n_res} results")
            if n_tests != 0 and i == n_tests:
                break
        p("all tests done!")
        p(nut.cli["RESET"])
        return ret

'''main'''
bs = BSParser("https://bs.to","andere-serien")
@nut.func_info
def main():
    if len(sys.argv) < 2:
        arg = input("searchterm: ")
    else:
        arg = sys.argv[1]
    bs.search_links(arg)
    for v in bs.res:
        print(v, "-> ", bs.res[v][0]["href"], "\n")
    in_ = nut.int_input("enter a number!", "select serie: ", max=(len(bs.res)-1))
    print(bs.res[in_][0]["href"])

