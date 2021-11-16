#!/usr/bin/python3
import os, sys, getopt, re
from configparser import ConfigParser

def db(*args, **kwargs):
    if True:
        print(*args, **kwargs)

class GitPush():

    def usage(self):
        print("usage: -h | -i <inifile> | -m <commit msg>")
        sys.exit(0)

    def fetch_args(self):
        if not os.path.exists(".gitignore"):
            os.system("touch .gitignore")
        with (f := open(".gitignore", "r+")):
            lns = f.readlines()
            if "push.ini\n" not in lns:
                f.write("push.ini\n")

        self.git_token = open(os.path.expanduser('~') + "/py/git_access.token").read()[:-1]
        
        self.msg, self.ini_file = "", "push.ini"
        opts, argv = getopt.getopt(sys.argv[1:], "m:i:h")
        for k, v in opts:
            if k == "-i":self.ini_file  = v
            if k == "-m":self.msg       = v
            if k == "-h":self.usage()
        db(f"{self.ini_file=}, {self.msg=}")

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
                    ,"repository":os.getcwd().split("/")[-1]
                    ,"confirm":"1"
                    ,"request_msg":"1"
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
        if self.msg == "" and bool(int(self.ini["push"]["request_msg"])): self.msg = input("commit msg>")
        self.msg = self.ini["push"]["pre_msg"] + self.msg + self.ini["push"]["post_msg"]
        cmds = [
                f"git commit -m \"{self.msg}\""
                ,f"git push https://{self.git_token}@github.com/nlsg/{self.ini['push']['repository']}"
                ]
        
        db("printing chain...")
        for cmd in self.ini.options("chain"):db(self.ini["chain"][cmd])
        for cmd in cmds                     :db(cmd)

        def commit():
            for cmd in self.ini.options("chain"):os.system(self.ini["chain"][cmd])
            for cmd in cmds                     :os.system(cmd)

        if bool(int(self.ini["push"]["confirm"])):
            if not input("[c]ommit\n>") == "c":
                sys.exit(0)
        commit()



gt = GitPush()
gt.fetch_args()
gt.parse_ini()
gt.exec_()
