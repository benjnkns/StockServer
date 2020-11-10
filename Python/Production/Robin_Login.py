# MY STUFF
import RobinhoodAPI
from RobinhoodAPI import login
from RobinhoodAPI import get_holdings


print ("Loggin into Robinhood...")
login("benjnkns@gmail.com", "Guitarist474747123")

print (get_holdings())
