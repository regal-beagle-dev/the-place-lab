place() {
    printf '%-6s %s\n' \
        host "${PLACE_NODE:-$(hostname -s)}" \
        role "${PLACE_ROLE:-unknown}" \
        addr "$(hostname -I 2>/dev/null | awk '{print $1}')" \
        up "$(uptime -p 2>/dev/null)"
}

logs() { journalctl -u "$1" -f --no-hostname; }
listening() { ss -tulpn 2>/dev/null | awk 'NR==1 || /LISTEN/'; }

# Attach to a session or create it. Default name: lab.
lab() { tmux attach -t "${1:-lab}" 2>/dev/null || tmux new -s "${1:-lab}"; }
