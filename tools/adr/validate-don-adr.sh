#!/usr/bin/env bash

set -uo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "$script_dir/.." && pwd)"
directories=(
    "docs/standaard/autorisaties/ac/1.1.x/1.1.0"
    "docs/standaard/besluiten/brc/1.1.0"
    "docs/standaard/catalogi/ztc/1.4.x/1.4.0"
    "docs/standaard/documenten/drc/1.8.x/1.8.0"
    "docs/standaard/notificaties/nrc/1.1.0"
    "docs/standaard/zaken/zrc/1.8.x/1.8.0"
)

if (($# != 0)); then
    printf 'This script uses the directory list configured near the top of the file and accepts no arguments.\n' >&2
    exit 1
fi

status=0
output_file="$script_dir/adr-output.txt"

if ! : > "$output_file"; then
    printf 'Cannot write output file: %s\n' "$output_file" >&2
    exit 1
fi

printf 'DON checker ADR validation output\n' | tee -a "$output_file"
printf 'Combined output file: %s\n\n' "$output_file" | tee -a "$output_file"

for directory in "${directories[@]}"; do
    printf '%s\n' "===== $directory =====" | tee -a "$output_file"

    if [[ "$directory" = /* ]]; then
        target_dir="$directory"
    else
        target_dir="$repo_root/$directory"
    fi
    if [[ ! -d "$target_dir" ]]; then
        printf 'Directory not found: %s\n\n' "$directory" | tee -a "$output_file" >&2
        status=1
        continue
    fi

    if [[ ! -f "$target_dir/openapi.yaml" ]]; then
        printf 'openapi.yaml not found in: %s\n\n' "$directory" | tee -a "$output_file" >&2
        status=1
        continue
    fi

    if ! (cd -- "$target_dir" && npx @developer-overheid-nl/don-checker@latest validate --standard adr --input ./openapi.yaml) 2>&1 | tee -a "$output_file"; then
        status=1
    fi

    printf '\n' | tee -a "$output_file"
done

exit "$status"
