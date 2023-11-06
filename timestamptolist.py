def time_manipulation(s):
    # Write code here
    timeparts=s.split(":")
    hours=int(timeparts[0])
    minutes=int(timeparts[1][:2])
    if 'AM' in s and hours ==12:
        hours=0
    if 'PM' in s and hours!=12:
        hours=hours+12
    print([hours,minutes])

if __name__ == '__main__':
    s=input()
    time_manipulation(s)    