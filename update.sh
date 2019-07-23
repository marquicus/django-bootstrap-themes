#!/bin/sh
set -e
#
# Bootstrap 3 / 4 theme updater
#
# dependencies: linux shell, busybox <https://busybox.net/>, jq <https://stedolan.github.io/jq/>
#
# usage: ./update.sh
#

DIRNAME=$(dirname $0)
THEMEPATH="${DIRNAME}/bootstrap_themes/static/bootstrap/themes"
btversions=("https://bootswatch.com/api/3.json" "https://bootswatch.com/api/4.json")
btreleases="https://api.github.com/repos/twbs/bootstrap/releases"
csstypes=("css" "cssMin")

for btversion in ${btversions[@]}; do
   for csstype in ${csstypes[@]}; do
       curl $btversion | jq -r ".themes[]|.${csstype}" | while read url; do wget -P "$THEMEPATH" -x -nH $url; done
   done
done

for ver in 3 4; do
   lv="$(curl -s $btreleases | jq '.[].assets[].browser_download_url' | sort | pcregrep "bootstrap-${ver}[\.\d]+-dist.zip" | tail -1 | tr -d \")"
   [ -d "$THEMEPATH/${ver}/default" ] && rm -rf "$THEMEPATH/${ver}/default"
   wget -qO- $lv | busybox unzip -qd "$THEMEPATH/${ver}" - && mv $THEMEPATH/${ver}/bootstrap-${ver}* "$THEMEPATH/${ver}/default"
done

# End of file
# vim: set ts=2 sw=2 noet:
