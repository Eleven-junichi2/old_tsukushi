#!/usr/bin/env bash

needs_update=true

export LC_ALL=C.UTF-8

. ~/.last_revision 2>/dev/null || true
if [ "$SNAP_DESKTOP_LAST_REVISION" = "$SNAP_REVISION" ]; then
  needs_update=false
fi
[ $needs_update = true ] && echo "SNAP_DESKTOP_LAST_REVISION=$SNAP_REVISION" > ~/.last_revision

if [ "$SNAP_ARCH" == "amd64" ]; then
  ARCH="x86_64-linux-gnu"
elif [ "$SNAP_ARCH" == "armhf" ]; then
  ARCH="arm-linux-gnueabihf"
else
  ARCH="$SNAP_ARCH-linux-gnu"
fi

# Tell libGL where to find the drivers
export LIBGL_DRIVERS_PATH=$SNAP/usr/lib/$ARCH/dri
export XLOCALEDIR="$SNAP/usr/share/X11/locale"
export LD_LIBRARY_PATH=$SNAP/usr/lib/$ARCH/dri:$LD_LIBRARY_PATH

export PYTHONIOENCODING=UTF-8

python3 -V
python3.7 "$SNAP/main.py" "$@"
