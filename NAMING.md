# Naming

> @ "the place"_

Machines are named after Star Wars planets. 
The rule below means a hostname tells you what a box is and where it physically lives, and it means the next machine names itself without another conversation.

## The rule

| Kind | Pattern | Examples |
|---|---|---|
| physical host | Star Wars planet, ≤6 characters, lowercase | `byss` `kejim` `endor` `kuat` |
| virtual machine | `<host-planet><NN>`, zero-padded | `byss01` `endor02` |
| ephemeral VM | `taris<NN>` | `taris01` |
| logical (namespace, dataset, pool) | plain and descriptive, unthemed | `bay-example` `tank/hangar` |
| personal device | Star Wars planet | `yavin` `kashyyyk` |

## Already Reserved

`yavin` primary laptop · `kashyyyk` work laptop · `kamino` iPhone · `naboo` wife's
· `bespin` gaming PC · `dagobah` work NAS · `byss` `kejim` `endor`
`kuat` — the lab.

## Bench Names

`scarif` · `ryloth` · `lothal` · `fondor` · `mortis` · `narkina`
