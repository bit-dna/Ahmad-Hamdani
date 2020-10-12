import speedtest

server=speedtest.Speedtest()

option=int(input(
    1) upload speed
    2) download speed
    3) ping
    what do you want to know : ))
    
if option==1:
    print(s.upload())

elif option==2:
    print(s.download())
    
elif option==3:
    server=[]
    s.get_server(server)
    print(s.results.ping)

else :
    print("invalid option")