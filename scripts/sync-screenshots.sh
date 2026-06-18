#!/usr/bin/env sh
set -eu

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
SRC_LIGHT="${MINDSTATE_SCREENSHOTS_LIGHT:-$ROOT/screenshots/google_play/phone}"
SRC_DARK="${MINDSTATE_SCREENSHOTS_DARK:-$HOME/Projects/Flutter/mindstate/screenshots/app-store/phone/dark}"
DST="$ROOT/src/assets/images"

# Website asset base -> Maestro screenshot basename (see mindstate/docs/screenshots.md)
screens="
phone_mix_player:1_session_player
phone_mix_browser:2_session_browser
phone_tone_editor:3_tone_editor
phone_add_track_modal:4_add_track_modal
phone_quick_mix_editor:5_simple_session_editor
phone_full_mix_editor:6_full_session_editor
phone_ritual_edit:7_ritual_edit
phone_qr_display:8_qr_display
phone_rituals_list:8_rituals_list
"

copy_if_present() {
	src_file="$1"
	out_file="$2"
	label="$3"

	if [ -f "$src_file" ]; then
		cp "$src_file" "$out_file"
		echo "copied $out_file"
	elif [ -f "$out_file" ]; then
		echo "keeping existing $out_file ($label not in source set)"
	else
		echo "missing: $src_file (and no existing $out_file)" >&2
		exit 1
	fi
}

for pair in $screens; do
	dest="${pair%%:*}"
	screen="${pair#*:}"
	copy_if_present "$SRC_LIGHT/${screen}.png" "$DST/${dest}_light.png" "$screen light"
	copy_if_present "$SRC_DARK/${screen}.png" "$DST/${dest}_dark.png" "$screen dark"
done

node "$ROOT/scripts/frame-screenshots.mjs"
