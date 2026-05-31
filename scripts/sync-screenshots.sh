#!/usr/bin/env sh
set -eu

SRC="${MINDSTATE_SCREENSHOTS:-$HOME/Projects/Flutter/mindstate/screenshots/mindstate-phone-apple}"
DST="src/assets/images"
PREFIX="mindstate-phone-apple"

# Store listing order (see mindstate/docs/screenshots.md)
# dest_base -> maestro screen suffix
screens="
phone_session_player:1_session_player
phone_session_browser:2_session_browser
phone_tone_editor:3_tone_editor
phone_simple_session_editor:4_simple_session_editor
phone_qr_display:5_qr_display
phone_add_track_modal:6_add_track_modal
phone_full_session_editor:7_full_session_editor
phone_rituals_list:8_rituals_list
phone_ritual_edit:9_ritual_edit
"

for theme in light dark; do
  for pair in $screens; do
    dest="${pair%%:*}"
    screen="${pair#*:}"
    src_file="$SRC/$theme/${PREFIX}_${screen}_${theme}.png"
    out_file="$DST/${dest}_${theme}.png"
    if [ ! -f "$src_file" ]; then
      echo "missing: $src_file" >&2
      exit 1
    fi
    cp "$src_file" "$out_file"
    echo "copied $out_file"
  done
done
