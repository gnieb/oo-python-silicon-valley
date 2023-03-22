from lib.funding_round import *
from lib.venture_capitalist import *
from lib.startup import *
import ipdb;
# code here
# e.g.


s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
s2 = Startup( 'Hooli', 'Gavin Belson', 'www.hooli_is_cooli.com' )
vc1 = VentureCapitalist( 'Peter Gregory', 1100000000 )
vc2 = VentureCapitalist('Erlich Bachman', 2000000000)
fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( s1, vc2, 'Pre-Seed', 100000.00 )
fr3 = FundingRound( s1, vc2, 'Seed', 200000.00 )
fr4 = FundingRound( s1, vc2, 'Series A', 300000.00 )
fr5 = FundingRound( s1, vc2, 'Series B', 400000.00 )








# do not remove
ipdb.set_trace()
