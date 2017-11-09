
# Execute this script by the user "ddbj"!! Do not use "sudo" !!!
# 

cd /mnt/raid_vol_1/Plone5/zeocluster/
bin/zeoserver start
bin/instance start
nohup bin/pcelery worker parts/instance/etc/zope.conf > /dev/null &




