[ -n "$BASH_VERSION" ] || return 0
case "$-" in *i*) ;; *) return 0 ;; esac

case "${PLACE_COLOR:-white}" in
    green)  __place_c='\[\e[32m\]' ;;
    red)    __place_c='\[\e[31m\]' ;;
    cyan)   __place_c='\[\e[36m\]' ;;
    yellow) __place_c='\[\e[33m\]' ;;
    *)      __place_c='\[\e[37m\]' ;;
esac

__place_mark='$'
[ "$(id -u)" -eq 0 ] && __place_mark='#'

PS1="${__place_c}\[\e[1m\]${PLACE_NODE:-\h}\[\e[0m\] \[\e[2m\]\w\[\e[0m\] ${__place_c}${__place_mark}\[\e[0m\] "
