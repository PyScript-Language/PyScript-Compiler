import time, os, sys, getpass, re, string

fp = input('FilePath: ')

if '.ps' in fp:
  try:
    f = open(f'{fp}')
  except:
    exit()
else:
  exit()

content = f.read()
colist = content.split("\n")

def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
      if somepredicate(*args, **kwargs): return True
      time.sleep(period)
    return False

allvars = {}
line = 0
read_line=0
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"


def pTAG():
  try:
    if '</p>' in lines:#maybe replace </p> with </>?
      wrd = '<p>'
      res = lines.partition(wrd)[2]
      res = res.replace('</p>', '')
      #res = res.replace(' ', '')
      res = res.replace('{getChar1}', getChar1)
      res = res.replace('{getChar2}', getChar2)
      res = res.replace('{getChar3}', getChar3)
      res = res.replace("{{input1}}", input1)
      res = res.replace("{{input2}}", input2)
      res = res.replace("{{input3}}", input3)
      res = res.replace("{{var1}}", var1)

      if "{{" in res:
        if "}}" in res:
          start = "{{"
          end = "}}"
          check = res[res.find(start) + len(start):res.rfind(end)]
              
          if check in allvars:
            res = res.replace('{{','')
            res = res.replace('}}','')
            e = allvars[check]
            res = res.replace(check, str(e))
          else:
            exit()#add error

      #wait_until("</p>", 0)
      split_string = res.split("</p>", -1)
      res = split_string[0]
      print(res)
    else:
      pass
  except:
    exit()


newvar = 0
file = open(fp)
readline2 = 0
for lines in file.readlines():
    if "/*" in lines:
      wait_until("*/", 0)
      readline2=1
    if readline2 == 1:
      continue
    if "//" in lines:#maybe change to /#
      readline2=1
    
    line+=1
    lines = lines.replace('\n','')
    lines = lines.replace('\t','')
    if lines == '': 
      pass
    elif lines in string.whitespace:
      pass
    elif "/*" in lines:
      wait_until("*/", 0)
      pass
    elif "//" in lines:
      pass
    lines = lines.rstrip()

    if "var " in lines:
      wrd = "var "
      newvar = lines.partition(wrd)[2]
      split_string = newvar.split("\")", -1)
      newvar.replace(")","")
      newvar.replace('\"', '')
      newvar = split_string[0]
      allvars[newvar] = 0
    
    if "//" in lines:
      pass
      read_line = 0
    elif "window.prompt(" in lines:
      wrd = "window.prompt("
      var = lines.partition(wrd)[2]
      split_string = var.split(");", -1)
      var.replace(');','')
      var.replace('\"',"")
      var = split_string[0]
      var.strip(");")

      if var in allvars:
        var = input()
        allvars[newvar] = var
      else:
        if var not in allvars:
          exit()#error
        else:
          exit()#error

    else:
      pass