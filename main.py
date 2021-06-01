import time, os, sys, getpass, re, string

fp = input('FilePath: ')

if '.pys' in fp:#hmmmm
  try:
    f = open(f'{fp}')
  except:
    raise Exception("No Such File Exists!")
else:
  raise Exception("The file isn't a '.pys' file!")

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

#all errors
class InvalidVariableError(Exception):
  pass
class InvalidSyntaxError(Exception):
  pass
class InvalidIndentationError(Exception):
  pass
class InvalidModuleError(Exception):
  pass
class InvalidStringIntError(Exception):
  pass

class TemplateError(Exception):
  pass

allvars = {}
line = 0
read_line=0
PASS = False
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"
functions = ["os.userinfo(","time.strftime(","window.alert(","console.print(","alert(","console.input(","window.prompt(","prompt("]


def timeTIME():
  if time_module == 1:
        wrd = "time.time("
        res = lines.partition(wrd)[2]
        res = res.replace(");","")
        print(res)

        if type(res) == str:
          if res == " " or res == "":
            time.time()#this won't do anything of course, unless you print it ;)
          else:
            raise InvalidStringIntError("'time.time' must be empty!")
        else:
          raise InvalidStringIntError("'time.time' must be empty!")
  else:
    raise InvalidModuleError("The 'time' module isn't imported or it doesn't exist!")

def osSYSTEM():
  if os_module == 1:
    wrd = "os.system("
    res = lines.partition(wrd)[2]

    if res[-3] == "\"" and res[0] == "\'" or res[-3] == "'" and res[0] == "\"":
      raise InvalidSyntaxError("The 'os.system' starting quotations and ending quotations are different!")
    else:
      if "\"" in res:
          split_string = res.split("\");", -1)
      elif "'" in res:
          split_string = res.split("\');", -1)
      else:
          raise InvalidSyntaxError("The 'os.system' statement is missing quotations!")
      res = res.replace("\"", "")
      res = res.replace("'", "")
      res = res.replace(");", "")
      
      #print(res)
      try:
        os.system(str(res))
      except:
        raise InvalidModuleError(f"'{res}' command doesn't exist!")
  else:
    raise InvalidModuleError("The 'os' module isn't imported or it doesn't exist!")

def osUSERINFO():
  if os_module == 1:
    wrd = "os.userinfo("
    global res
    res = lines.partition(wrd)[2]

    if "  " in res:
      raise InvalidSyntaxError("'os.userinfo' cannot include spaces!")
    else:
      if ");" in res:
        res = res.replace(");","")
      else:
        raise InvalidSyntaxError("'os.userinfo' must have ');'!")
      if res == "" or res == " ":
        try:
          print(os.environ["REPL_OWNER"])
        except:
          raise InvalidModuleError("This function does not exist on your device!")
      else:
        raise InvalidModuleError("'os.userinfo' must be empty!")
  else:
    raise InvalidModuleError("The 'os' module isn't imported or it doesn't exist!")
    

'''
Note that ascii characters are used like this in pyscript:
/1234 or /u1243
Of course, those are examples ;) Another thing I should mention is that not all characters have been made yet ;)
'''

def WINDOWalert():#add f'string
  try:
    if '");' in lines or "');" in lines or "`);" in lines:
      wrd = "window.alert("
      res = lines.partition(wrd)[2]
      #print(res)
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "\"" and res[0] == "`" or res[-3] == "'" and res[0] == "\"" or res[-3] == "'" and res[0] == "`" or res[-3] == "`" and res[0] == "\"" or res[-3] == "`" and res[0] == "'":
        raise InvalidSyntaxError("The 'window.alert' starting quotations and ending quotations are different!")
      else:
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        if "\"" in res:
          split_string = res.split("\");", -1)
        elif "'" in res:
          split_string = res.split("\');", -1)
        elif "`" in res:
          split_string = res.split("`);", -1)
        else:
          raise InvalidSyntaxError("The 'window.alert' statement is missing quotations!")
        res = split_string[0]
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        #colors: res = res.replace("{red}", red)
        res = res.replace('"', "")
        res = res.replace("'", "")
        res = res.replace("`", "")
        res = res.replace(");","")

        if "{{" in res:
          if "}}" in res:
            start = "{{"
            end = "}}"
            check = res[res.find(start) + len(start):res.rfind(end)]
            if check in allvars:
              res = res.replace("{{", "")
              res = res.replace("}}", "")
              dffdfdfdf = allvars[check]
              res = res.replace(check, str(dffdfdfdf))
            else:
              global PASS
              PASS = False
              if "time.time(" in check:
                if check[-1] == "(":
                  print(time.time())
                  PASS = True
                else:
                  raise InvalidSyntaxError("'time.time' must be empty!")
              elif "time.strftime(" in check:
                #print(timeSTRFTIME())
                PASS = True
              else:
                #print(var)
                #print(res)
                raise InvalidVariableError(f"'{var}' variable does not exist!")
        if PASS:
          pass
        else:
          print(res, end="")
          print()
    else:
      raise InvalidSyntaxError("The 'window.alert' statement must have a closing ');!")
  except:
    raise InvalidSyntaxError("The 'window.alert' statement must have a closing ');!")

def alert():
  try:
    if '");' in lines or "');" in lines or "`);" in lines:
      wrd = "alert("
      res = lines.partition(wrd)[2]
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "\"" and res[0] == "`" or res[-3] == "'" and res[0] == "\"" or res[-3] == "'" and res[0] == "`" or res[-3] == "`" and res[0] == "\"" or res[-3] == "`" and res[0] == "'":
        raise InvalidSyntaxError("The 'alert' starting quotations and ending quotations are different!")
      else:
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        if "\"" in res:
          split_string = res.split("\");", -1)
        elif "'" in res:
          split_string = res.split("\');", -1)
        elif "`" in res:
          split_string = res.split("`);", -1)
        else:
          raise InvalidSyntaxError("The 'alert' statement is missing quotations!")
        res = split_string[0]
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        #colors: res = res.replace("{red}", red)
        res = res.replace('"', "")
        res = res.replace("'", "")
        res = res.replace("`", "")
        res = res.replace(");","")

        if "{{" in res:
          if "}}" in res:
            start = "{{"
            end = "}}"
            check = res[res.find(start) + len(start):res.rfind(end)]
            if check in allvars:
              res = res.replace("{{", "")
              res = res.replace("}}", "")
              dffdfdfdf = allvars[check]
              res = res.replace(check, str(dffdfdfdf))
            else:
              global PASS
              PASS = False
              if "time.time(" in check:
                if check[-1] == "(":
                  print(time.time())
                  PASS = True
                else:
                  raise InvalidSyntaxError("'time.time' must be empty!")
              elif "time.strftime(" in check:
                #print(timeSTRFTIME())
                PASS = True
              else:
                raise InvalidVariableError(f"'{var}' variable does not exist!")
        if PASS:
          pass
        else:
          print(res, end="")
          print()
    else:
      raise InvalidSyntaxError("The 'alert' statement must have a closing ');!")
  except:
    raise InvalidSyntaxError("The 'alert' statement must have a closing ');!")

def CONSOLEprint():
  try:
    if '");' in lines or "');" in lines or "`);" in lines:
      wrd = "console.print("
      res = lines.partition(wrd)[2]
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "\"" and res[0] == "`" or res[-3] == "'" and res[0] == "\"" or res[-3] == "'" and res[0] == "`" or res[-3] == "`" and res[0] == "\"" or res[-3] == "`" and res[0] == "'":
        raise InvalidSyntaxError("The 'console.print' starting quotations and ending quotations are different!")
      else:
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        if "\"" in res:
          split_string = res.split("\");", -1)
        elif "'" in res:
          split_string = res.split("\');", -1)
        elif "`" in res:
          split_string = res.split("`);", -1)
        else:
          raise InvalidSyntaxError("The 'console.print' statement is missing quotations!")
        res = split_string[0]
        res = res.replace("\");","")
        res = res.replace('`);',"")
        res = res.replace('\');',"")
        res = res.replace("/n", "\n")
        res = res.replace("/t", "\t")
        #colors: res = res.replace("{red}", red)
        res = res.replace('"', "")
        res = res.replace("'", "")
        res = res.replace("`", "")
        res = res.replace(");","")

        if "{{" in res:
          if "}}" in res:
            start = "{{"
            end = "}}"
            check = res[res.find(start) + len(start):res.rfind(end)]
            if check in allvars:
              res = res.replace("{{", "")
              res = res.replace("}}", "")
              dffdfdfdf = allvars[check]
              res = res.replace(check, str(dffdfdfdf))
            else:
              global PASS
              PASS = False
              if "time.time(" in check:
                if check[-1] == "(":
                  print(time.time())
                  PASS = True
                else:
                  raise InvalidSyntaxError("'time.time' must be empty!")
              elif "time.strftime(" in check:
                #print(timeSTRFTIME())
                PASS = True
              else:
                raise InvalidVariableError(f"'{var}' variable does not exist!")
        if PASS:
          pass
        else:
          print(res, end="")
          print()
    else:
      raise InvalidSyntaxError("The 'console.print' statement must have a closing ');!")
  except:
    raise InvalidSyntaxError("The 'console.print' statement must have a closing ');!")



newvar = 0
time_module = 0
file = open(fp)
readline2 = 0
for lines in file.readlines():

    #print(lines)

    if "/#" in lines:
      readline2=1
      #print(wait_until("*/", 0))
      wait_until("#/", 0)
    if readline2 == 1:
      readline2 = 0
      continue
    if "//" in lines:#maybe change to /#
      readline2=1
    
    line+=1
    lines = lines.replace('\n','')
    lines = lines.replace('\t','')

    #print(lines)

    if lines == '': 
      pass
    elif lines in string.whitespace:
      raise InvalidIndentationError("Your indentation does not fit the other statements!")
    elif "/#" in lines:
      wait_until("#/", 0)
      readline2 = 1
    elif "//" in lines:
      pass
    lines = lines.rstrip()

    #print(lines[:2])

    '''
    elif " " in lines or "\t" in lines or "  " in lines:
      raise InvalidIndentationError(f"line {line}, the indentation does not fit the other statements!")
    '''

    '''
    Note that `;`'s are strictly required in this language
    '''
    
    if lines[:2] == "//" or "//" in lines:
      pass
      read_line = 0
    elif "import(\"time\");" in lines or "import('time');" in lines:#add semicolon error
      time_module = 1
    elif "import(\"os\");" in lines or "import('os');" in lines:
      os_module = 1
    elif "var " in lines:
      wrd = "var "
      newvar = lines.partition(wrd)[2]
      split_string = newvar.split("\")", -1)
      newvar.replace(")","")
      newvar.replace('\"', '')
      newvar = split_string[0]
      #newvar = variable;
      if newvar[-1] == ";":
        if ";" in newvar[:-1]:
          for i in newvar[:-1]:
            if "'" == i or "\"" == i or "`" == i:
              pass
            else:
              raise InvalidSyntaxError("You must only include one semi-colon!")
        else:
          newvarTEST = newvar[-1]
          newvar = newvar.replace(";","")#make ; disappear into blank space
      else:
        raise InvalidSyntaxError("Variable statement is missing semi-colon!")
      
      if " " in newvar:
        if "=" in newvar:
          idk = []
          Continue = True
          for i in newvar:
            if Continue:
              if i == "=":
                idk.append(i)
                Continue = False
              else:
                idk.append(i)
            else:
              if i == " ":
                idk.append(i)
                break
              else:
                break
          idk = "".join(idk)
          newvar = newvar.replace(idk, "")
            
          if "'" in newvar or "\"" in newvar or "`" in newvar or "os.userinfo(" in newvar:
            if newvar in functions:
              if "console.print(" in newvar:
                CONSOLEprint()
              elif "window.alert(" in newvar:
                WINDOWalert()
              elif "alert(" in newvar:
                alert()
              
              elif "window.prompt(" in newvar:
                e
              elif "prompt(" in newvar:
                e
              elif "console.input(" in newvar:
                e

              elif "os.userinfo(" in newvar:
                  osUSERINFO()
                  allvars[res] = os.environ["REPL_OWNER"]
              
              elif "time.strftime(" in newvar:
                if time_module == 1:
                  timeSTRFTIME()
                  #allvars[] = time.strftime()
                else:
                  raise InvalidModuleError("The 'time' module isn't imported or it doesn't exist!")

            else:
              newvar = str(newvar) # makes sure its a string
              if newvar[-1] == "'" and newvar[0] == "'" or newvar[-1] == "\"" and newvar[0] == "\"" or newvar[-1] == "`" and newvar[0] == "`":
                newvar = newvar.replace(newvar[-1], "")
                #newvar = newvar.replace(newvar[0], "")
              elif "os.userinfo(" in newvar:
                pass
              else:
                raise InvalidSyntaxError("Starting quotations and end quotations must be the same!")
              allvars[newvar] = newvar
          elif newvar == "true":
            allvars[newvar] = True
          elif newvar == "false":
            allvars[newvar] = False

          else:
            raise InvalidSyntaxError("Variables must be named after there is a equal sign!")
        else:
          raise InvalidSyntaxError("Variables cannot include spaces!")
      else:
        allvars[newvar] = 0
      


    elif "window.prompt(" in lines:
      wrd = "window.prompt("
      var = lines.partition(wrd)[2]
      if var[-1] == ";":
        split_string = var.split(");", -1)
        var.replace(');','')
        var.replace('\"',"")
        var.replace('\'',"")
        var.replace('`',"")
        var = split_string[0]
        var.strip(");")

        if var in allvars:
          var = input()
          allvars[newvar] = var
        else:
          if var not in allvars:
            raise InvalidVariableError(f"'{var}' variable does not exist!")
          else:
            pass
      else:
        raise InvalidSyntaxError("'window.prompt' statement is missing semi-colon!")
    elif "prompt(" in lines:
      wrd = "prompt("
      var = lines.partition(wrd)[2]
      if var[-1] == ";":
        split_string = var.split(");", -1)
        var.replace(');','')
        var.replace('\"',"")
        var.replace('\'',"")
        var.replace('`',"")
        var = split_string[0]
        var.strip(");")

        if var in allvars:
          var = input()
          allvars[newvar] = var
        else:
          if var not in allvars:
            raise InvalidVariableError(f"'{var}' variable does not exist!")
          else:
            pass
      else:
        raise InvalidSyntaxError("'prompt' statement is missing semi-colon!")
    elif "console.input(" in lines:
      wrd = "console.input("
      var = lines.partition(wrd)[2]
      if var[-1] == ";":
        split_string = var.split(");", -1)
        var.replace(');','')
        var.replace('\"',"")
        var.replace('\'',"")
        var.replace('`',"")
        var = split_string[0]
        var.strip(");")

        if var in allvars:
          var = input()
          allvars[newvar] = var
        else:
          if var not in allvars:
            raise InvalidVariableError(f"'{var}' variable does not exist!")
          else:
            pass
      else:
        raise InvalidSyntaxError("'console.input' statement is missing semi-colon!")


    elif "window.alert(" in lines:
      WINDOWalert()
    elif "console.print(" in lines:
      CONSOLEprint()
    elif "alert(" in lines:
      alert()

    
    elif "if " in lines:
      e


    elif "time.sleep(" in lines:
      if time_module == 1:
        wrd = "time.sleep("
        res = lines.partition(wrd)[2]
        
        if res[-1] == ";":
          try:
            res = res.replace(");","")
            for i in res:
              if i in ["1","2","3","4","5","6","7","8","9","0"]:
                time.sleep(int(res))
              else:
                raise InvalidStringIntError("Strings cannot be inside integer values!")
          except:
            raise InvalidSyntaxError("There must be only one semi-colon!")
        else:
          raise InvalidSyntaxError("'time.sleep' is missing semi-colon!")
      else:
        raise InvalidModuleError("The 'time' module isn't imported or it doesn't exist!")

    elif "time.time(" in lines:#remember to NOT print. It only prints when you do print
      timeTIME()#this doesnt really do anything.

    elif "time.strftime(" in lines:
      timeSTRFTIME()
      if time_module == 1:
        wrd = "time.strftime("

    
    elif "os.system(" in lines:
      osSYSTEM()
    
    elif "os.userinfo(" in lines:
      osUSERINFO()

    

    else:
      pass
