#!/bin/sh
sudo apt update && sudo apt upgrade -y
mkdir grove
cd grove
echo "verderen configuratie nodig"
curl -kl curl -kL dexterindustries.com/update_grovepi | bash
sudo apt --fix-broken install 
curl -kl curl -kL dexterindustries.com/update_grovepi | bash
cd /home/pi/grove/Dexter/GrovePi/Firmware
bash firmware_update.sh

echo "DE PI IS NU UPTODATE SUDO APT UPDATE IS NIET NODIG!!!!"
echo "----------------------------------------------------------------------------------------------"
echo "maakt directory genaamd grove"
echo "vervolgens zorgt hij er voor dat de software word gedownload en gebuild."
echo "dan fixt hij de download, Sommigen packages zijn fout Gedownload en start hij hem opnieuw op"
echo "nu lukt het wel aangezien hij niet meer hoeft te builden allen plaatsen"
echo "en tot slot update hij alle firmware van grove."


# maakt directory genaamt grove
# vervolgens zorgt hij er voor dat de software word gedownload en gebuild.
# dan fixt hij de download packages die fout zijn gegaan en start hij hem opnieuw
# nu lukt het wel aangezien hij niet meer hoeft te builden allen plaatsen
# en tot slot update hij alle firmware
