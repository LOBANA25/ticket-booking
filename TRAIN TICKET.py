class TicketReservation:
    def __init__(self):
        self.booking={}
        self.cancels={}
        self.chart_dis={}
        self.waiting={}
        self.max_seats=8
        self.booked_seats=0
        self.stations=['A','B','C','D','E']
        
    #BOOKING 
    def book(self,pnr,ch,sou_sta,des,seats):
        if(self.checkAvailability(sou_sta,des,seats) and seats<=self.max_seats):

            book_={"choice":ch,"source_station":sou_sta,"destination":des,"seats":seats,"status":"confirmed"}
            self.booking[pnr]=book_
            self.updateChart(ch,sou_sta,des,seats)
            return "BOOKING SUCCESFUL with PNR" ,pnr
        elif(seats<=2 and self.booked_seats>=self.max_seats+2):
            book_={"choice":ch,"source_station":sou_sta,"destination":des,"seats":seats,"status":"waiting"}
        return "BOOKING FAILED"
            
    #CANCELLING       
    def cancel(self,ch,pnr,seats):
        if(pnr in list(self.booking.keys())):
            #print("yes")
            cancel_={"choice":ch,"seats":seats}
            self.cancels[pnr]=cancel_
            booked_source=self.booking[pnr]["source_station"]
            booked_des=self.booking[pnr]["destination"]
            self.updateChart(ch,booked_source,booked_des,seats)
            self.booking[pnr]["seats"]-=seats
            return "CANCELLED SUCCESSFULLY"
        return "CAN NOT BE CANCELLED"

    #CHART CREATION    
    def chart(self):
        #station=['A','B','C','D','E']
        for seat in range(1,9):
            sta={}
            for s in self.stations:
                sta[s]=(".")
            self.chart_dis[seat]=sta
        #print(chart_dis)

    #CHECKING AVAILABLITY OF TICKETS   
    def checkAvailability(self,sou_sta,des,seats):
      self.booked_seats+=seats
      if(self.booked_seats<self.max_seats and self.booked_seats+seats<=self.max_seats):
        
        for i in range(self.booked_seats,(self.booked_seats+seats)):
            for j in range(self.stations.index(sou_sta),self.stations.index(des)+1):
                if(self.chart_dis[i][self.stations[j]]!="."):
                    return False
        return True
      #sreturn False
    
    def updateChart(self,ch,source,des,seats):
        
        if(ch=="book"):
            if(self.booked_seats<self.max_seats and self.booked_seats+seats<=self.max_seats):
                for i in range(self.booked_seats,self.booked_seats+seats+1):
                    for j in range(self.stations.index(source),self.stations.index(des)+1):
                        self.chart_dis[i][self.stations[j]]="*"
        elif(ch=="cancel"):
            self.booked_seats-=seats
            for i in range(self.booked_seats,self.booked_seats+seats):
                for j in range(self.stations.index(source),self.stations.index(des)+1):
                    self.chart_dis[i][self.stations[j]]="."

    def printChart(self):
        #station=['A','B','C','D','E']
        for seat in range(1,9):
            for s in self.stations:
                print(self.chart_dis[seat][s], end=" ")
            print()
pnr=0  
tt=TicketReservation()
tt.chart()
while(True):
    ch=input("Enter you Choice: ").lower()
    print(ch)
    if(ch=="book"):
        pnr+=1
        source_station=input("Your Station: ")
        des=input("Your Destination: ")
        no_seat=int(input("No.of.seats: "))
        print(tt.book(pnr,ch,source_station,des,no_seat))
        
    elif(ch=="cancel"):
        pnr=int(input("Enter you PNR number: "))
        no_tic=int(input("No.of seats you want to cancel: "))
        print(tt.cancel(ch,pnr,no_tic))

    elif(ch=="summary"):
        tt.printChart()
        
    elif(ch=="exit"):
        break
#print(chart_dis)
