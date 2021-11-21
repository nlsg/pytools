#!/usr/bin/python3
import os, sys, getopt, re
import nls_util as nut
from configparser import ConfigParser

def db(*args, **kwargs):
    if True:
        print(*args, **kwargs)

class GitPush():

    def usage(self):
        print("usage: -h | -i <inifile> | -m <commit msg> | -f[irefox] <file> | -a[dd cmd] <cmd> ")
        nut.quiet_exit()

    def open_in(file="",browser="firefox"):
        self.parse_ini()
        url = f"https://github.com/nlsg/{self.ini['push'].get('repository')}/"
        if file != "":
            url += "blob/main/"
            url += file
        print(f"{browser} {url}")
        os.system(f"{browser} {url}")
        nut.quiet_exit()

    def get_args(self):
        if not os.path.exists(".gitignore"):
            os.system("touch .gitignore")
        with (f := open(".gitignore", "r+")):
            lns = f.readlines()
            if "push.ini\n" not in lns:
                f.write("push.ini\n")
        self.git_token = open(os.path.expanduser('~') + "/py/git_access.token").read()[:-1]
        self.msg, self.ini_file = "", "push.ini"
        opts, argv = getopt.getopt(sys.argv[1:], "m:i:a:hf")
        for k, v in opts:
            if k == "-i":self.ini_file  = v
            if k == "-m":self.msg       = v
            if k == "-h":self.usage()
            if k == "-v":self.open_in("qutwbrowser")
            if k == "-a":self.add_cmd(v)
        db(f"{self.ini_file=}, {self.msg=}")

    def add_cmd(self,cmd):
        self.ini = ConfigParser()
        self.ini.read(self.ini_file)
        chain = self.ini["chain"]
        splts = cmd.split("=")
        if len(splts) == 1:
            chain[f"cmd{len(chain)}"] = cmd 
        else:
            cmd = "" 
            for splt in splts[1:]: cmd += splt
            chain[f"{splts[0]}"] = cmd
        self.ini.write(open(self.ini_file, "w"))
        nut.quiet_exit()

    def parse_ini(self):
        write_flg = False
        if not os.path.exists(self.ini_file):
            os.system(f"touch {self.ini_file}")
            write_flg = True
        self.ini = ConfigParser()
        self.ini.read(self.ini_file)

        if "push" not in self.ini:
            write_flg = True
            push_cfgs = {
                    "pre_msg":""
                    ,"post_msg":""
                    ,"default_msg":""
                    ,"repository":os.getcwd().split("/")[-1]
                    ,"confirm_before_push":"True"
                    }
            self.ini.add_section("push")
            for cfg in push_cfgs:
                if cfg not in self.ini["push"]:
                    self.ini["push"][cfg] = push_cfgs[cfg]
                db(f"key: {cfg}, val: {push_cfgs[cfg]}")

        if "chain" not in self.ini:
            write_flg = True
            self.ini.add_section("chain")

        if write_flg:
            self.ini.write(open(self.ini_file, "w"))
            db("ini_writen!")

    def exec_(self):
        cf = self.ini["push"]
        if self.msg == "":
            self.msg = cf["default_msg"]
            if self.msg == "":
                self.msg = input("commit msg>")
        self.msg = cf["pre_msg"] + self.msg + cf["post_msg"]

        cmds = [f"git commit -m \"{self.msg}\""
                ,f"git push https://{self.git_token}@github.com/nlsg/{cf['repository']}"
                ]

        def commit(func):
            for cmd in self.ini.options("chain"):func(self.ini["chain"][cmd])
            for cmd in cmds                     :func(cmd)

        commit(print)

        if cf.getboolean("confirm_before_push"):
            if not input("[c]ommit\n>") == "c":
                nut.quiet_exit()
        commit(os.system)


gt = GitPush()

def main():
    gt.get_args()
    gt.parse_ini()
    gt.exec_()

if __name__ == "__main__":
    main()

    for cf in gt.ini["push"]:
        print(cf)

    cf = gt.ini["push"]
    cf.get("repository")




