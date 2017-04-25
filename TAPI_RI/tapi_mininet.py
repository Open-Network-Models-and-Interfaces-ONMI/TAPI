#!/usr/bin/python
####################################
#  README
#
#  THIS FILE NEEDS TO BE COPIED IN mininet/custom FOLDER
#
####################################
import sys

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel, info, warn
from mininet.cli import CLI


setLogLevel( 'info' )
net = Mininet()

info( '*** Adding controller\n' )
c0 = RemoteController( 'c0', ip='0.0.0.0', port=6633)
net.addController( c0 )

#info( '*** Adding hosts\n' )
#h1 = net.addHost( 'h1', ip='10.0.0.1' )

# creating switches
info( '*** Adding switch\n' )
s1 = net.addSwitch( 's1' )
s2 = net.addSwitch( 's2' )
s3 = net.addSwitch( 's3' )
s4 = net.addSwitch( 's4' )

# creating links  
info( '*** Creating links\n' )
net.addLink( s1, s3 )
net.addLink( s3, s1 )
net.addLink( s1, s4 )
net.addLink( s4, s1 )
net.addLink( s2, s3 )
net.addLink( s3, s2 )
net.addLink( s2, s4 )
net.addLink( s4, s2 )


info( '*** Starting network\n' )
net.start()
CLI( net )
net.stop()
    

