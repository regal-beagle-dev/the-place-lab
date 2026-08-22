## The Place
Infrastructure for my home and other projects at home.

> @ "the place"

📄 **The Place Lab

### The roster

| | | |
|---|---|---|
| `byss` | Old Tower | NAS · ZFS mirror · KVM host · GTX 1070 |
| `kejim` | EliteDesk 800 G2 | k3s control plane, bare metal |
| `endor` | Lemur Pro | KVM host for throwaway workers |
| `kuat` | UniFi USW-Flex-2.5G-8 | the switch everything docks to |

Worker VMs are satellites of their host: `byss01`, `endor02`. See [NAMING.md](NAMING.md).

### Inventory for nodes
[`inventory/nodes.yml`](inventory/nodes.yml) is the only file edited by hand. Everything in
`build/` is generated from it and committed, so a pull request shows the intent and the effect.

```sh
mise run render         # regenerate build/
mise run check          # fail if build/ is stale
mise run reservations   # for now, addressed entered by hand on Nokia app
```

To reach the nodes by name, add to `~/.ssh/config`:

```
Include ~/code/regal-beagle/the-place-lab/build/ssh_config
```

### Addressing

The house router is an ISP-managed Nokia with a locked LAN page and a DHCP pool spanning the
whole subnet, because dadgummit... 
The lab's addresses are carved out with per-MAC reservations entered in its mobile
app (because it grabs identity better than their web-ui). 

That step is manual; `mise run reservations` renders the list.
