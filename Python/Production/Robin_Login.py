# MY STUFF
import RobinhoodAPI
import datetime
from RobinhoodAPI import login
from RobinhoodAPI import get_holdings
from RobinhoodAPI import build_profile

print ("Loggin into Robinhood...")
print (datetime.date.today())
login("benjnkns@gmail.com", "Guitarist474747123")

print (get_holdings())
print (build_profile())
