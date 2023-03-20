from lib.funding_round import *
from lib.venture_capitalist import *
from lib.startup import *
import ipdb;
# code here
# e.g.


s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
vc2 = VentureCapitalist('Erlich Baughman', 2000000000)
fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )







# do not remove
ipdb.set_trace()
