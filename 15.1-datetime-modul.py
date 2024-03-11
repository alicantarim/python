from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

result = dir(datetime)
# result = dir(datetime.time)
# result = dir(datetime.date)


simdi = datetime.now()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y') # yıl bilgisini verir.
result = datetime.strftime(simdi,'%X') # saat bilgisini verir.
result = datetime.strftime(simdi,'%d') # gün bilgisini verir.
result = datetime.strftime(simdi,'%A') # gün bilgisini string verir.
result = datetime.strftime(simdi,'%B') # Ay bilgisini string verir.
result = datetime.strftime(simdi,'%Y %B %A') # Yıl Ay ve Gün bilgisini verir.


# t = '21 Nisan 2019'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year
# print(result)

birtday = datetime(1983,5,9,15,10,15)

result = datetime.timestamp(birtday)  #İlgili tarih objesi bize saniye cinsinden getirilir. 421330215.0
result = datetime.fromtimestamp(result) # Saniyeyi datetime olarak verir. 1983-05-09 15:10:15
result = datetime.fromtimestamp(0) # 1970-01-01 03:00:00 PC milat bilgisi getirilir.

result = simdi - birtday #timedelta objesi

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

result = simdi + timedelta(days=10) # Şu anki tarihin üzerine 10 gün ekler.
result = simdi + timedelta(days=730, minutes=10) #Şu anki tarihe 730 gün ve 10 dk ekler.
reuslt = simdi - timedelta(days=10) # Şu anki tarihden 10 gün öncesine gider.

print(result)