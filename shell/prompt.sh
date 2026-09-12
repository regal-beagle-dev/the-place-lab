[ -n "$BASH_VERSION" ] || return 0
case "$-" in *i*) ;; *) return 0 ;; esac

case "${PLACE_COLOR:-white}" in
    green)  __place_c='\[\e[32m\]' ;;
    red)    __place_c='\[\e[31m\]' ;;
    cyan)   __place_c='\[\e[36m\]' ;;
    yellow) __place_c='\[\e[33m\]' ;;
    *)      __place_c='\[\e[37m\]' ;;
esac

# Root keeps a distinct signal, in colour rather than a different glyph.
__place_mark_c="$__place_c"
[ "$(id -u)" -eq 0 ] && __place_mark_c='\[\e[1;31m\]'

# ~/.bashrc sets PS1 after /etc/profile.d runs, so assigning it here loses.
# PROMPT_COMMAND is evaluated before each prompt, once all sourcing is done.
__place_ps1() {
    PS1="\[\e[2m\]\u@\[\e[0m\]${__place_c}\[\e[1m\]${PLACE_NODE:-\h}\[\e[0m\] \[\e[2m\]\w\[\e[0m\] ${__place_mark_c}❯\[\e[0m\] "
}

case "${PROMPT_COMMAND:-}" in
    *__place_ps1*) ;;
    *) PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND; }__place_ps1" ;;
esac
