import sys

mt=1
msf=-1000000
lmt=1
for line in sys.stdin:
    for x in line.split():
        x=int(x)
        if x==-999999:
            print(int(msf))
            mt=1
            msf=-1000000
            lmt=1
        else:
            mt=mt*x
            if mt==0:
                msf=max(msf,mt)
                mt=1
                lmt=1
            elif mt>0:
                msf=max(msf,mt)
            else:
                msf=max(msf,mt//lmt)
            if x!=0 and lmt>0:
                lmt=lmt*x
# import sys
# lastMinusMul=1;
# currentMax=-999999
# currentMul=1
#
# for line in sys.stdin:
#     for x in line.split():
#         x=int(x)
#         if x==-999999:
#             print(int(currentMax))
#             lastMinusMul=1
#             currentMax=-999999
#             currentMul=1
#         else:
#            currentMul*=x;
#            if currentMul >= 0:
#                currentMax=max(currentMax,currentMul)
#                if currentMul==0:
#                    currentMul=1
#                    lastMinusMul=1
#            elif currentMul < 0:
#                currentMax=max(currentMax,currentMul//lastMinusMul)
#                if lastMinusMul==1:
#                    lastMinusMul=currentMul