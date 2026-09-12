export EDITOR="${EDITOR:-vim}"
export LESS="-R"
export HISTSIZE=100000
export HISTFILESIZE=100000
export HISTCONTROL=ignoreboth:erasedups
export HISTTIMEFORMAT="%F %T  "
[ -n "$BASH_VERSION" ] && shopt -s histappend checkwinsize 2>/dev/null
