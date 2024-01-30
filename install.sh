#!/bin/sh
sudo apt update && sudo apt upgrade -y
mkdir grove
cd grove
echo "verderen configuratie nodig"
curl -kl curl -kL dexterindustries.com/update_grovepi | bash


